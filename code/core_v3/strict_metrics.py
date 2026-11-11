"""Strict answers, separately named partial scores, and applicable population metrics."""
import math
from statistics import mean


def canonical(value, key=""):
    if isinstance(value, dict):
        return {k: canonical(v, k) for k, v in value.items()}
    if isinstance(value, list):
        result = [canonical(v) for v in value]
        if key == "cells" or key.endswith("_docs"):
            return sorted(result, key=repr)
        return result
    return value


def equal(reference, prediction, key=""):
    if isinstance(reference, bool):
        return isinstance(prediction, bool) and reference == prediction
    if isinstance(reference, (int, float)):
        if isinstance(prediction, bool) or not isinstance(prediction, (int, float)):
            return False
        return math.isfinite(float(prediction)) and math.isclose(reference, prediction, rel_tol=1e-6, abs_tol=1e-6)
    if isinstance(reference, dict):
        return isinstance(prediction, dict) and all(k in prediction and equal(v, prediction[k], k) for k, v in reference.items())
    if isinstance(reference, list):
        if not isinstance(prediction, list) or len(reference) != len(prediction):
            return False
        a, b = canonical(reference, key), canonical(prediction, key)
        return all(equal(x, y) for x, y in zip(a, b))
    return type(reference) is type(prediction) and reference == prediction


def population_metrics(reference, prediction):
    g, p = set(reference), set(prediction)
    tp, fp, fn = len(g & p), len(p - g), len(g - p)
    f1 = 2 * tp / (2 * tp + fp + fn) if (g or p) else 1.0
    return {"tp": tp, "fp": fp, "fn": fn, "gold_size": len(g), "pred_size": len(p),
            "precision": tp / len(p) if p else None, "recall": tp / len(g) if g else None,
            "f1": f1, "set_exact": int(g == p)}


def evaluate(reference, prediction):
    gold = reference["gold"]
    policy = reference["evaluation"]
    answer = gold.get("answer")
    if reference.get("group") == "evidence_verification" and answer in (0, 1):
        answer = bool(answer)
    available = prediction.get("status") != "abstain"
    strict = int(available and equal(answer, prediction.get("answer"))) if policy["answer"] else None
    partial = None
    if policy["answer"] and isinstance(answer, dict):
        p = prediction.get("answer") if isinstance(prediction.get("answer"), dict) else {}
        partial = sum(k in p and equal(v, p[k], k) for k, v in answer.items()) / max(1, len(answer))
    population = population_metrics(gold.get("members") or [], prediction.get("members") or []) if policy["members"] else None
    denominator = int(available and equal(gold.get("denominator"), prediction.get("denominator_count"))) if policy["denominator_count"] else None
    denominator_set = population_metrics(gold["denominator_members"], prediction.get("denominator_members") or []) if policy["denominator_count"] and "denominator_members" in gold else None
    if not available:
        for metric in (population, denominator_set):
            if metric is not None:
                metric.update(f1=0.0, set_exact=0)
    return {"id": reference["id"], "group": reference["group"], "strict_answer": strict,
            "structured_field_score": partial, "population": population, "denominator_count_exact": denominator,
            "denominator_set": denominator_set,
            "abstain": not available, "partial_evidence": prediction.get("status") == "partial"}


def avg(values):
    values = [v for v in values if v is not None]
    return mean(values) if values else None


def summarize(rows):
    pop = [r["population"] for r in rows if r["population"] is not None]
    nonempty = [r for r in pop if r["gold_size"] > 0]
    empty = [r for r in pop if r["gold_size"] == 0]
    denominator_sets = [r["denominator_set"] for r in rows if r.get("denominator_set") is not None]
    tp, fp, fn = (sum(p[k] for p in pop) for k in ("tp", "fp", "fn"))
    return {"tasks": len(rows), "answer_n": sum(r["strict_answer"] is not None for r in rows),
            "strict_answer_accuracy": avg(r["strict_answer"] for r in rows),
            "structured_field_score": avg(r["structured_field_score"] for r in rows),
            "population_n": len(pop), "population_macro_f1": avg(p["f1"] for p in pop),
            "nonempty_population_n": len(nonempty), "nonempty_population_f1": avg(p["f1"] for p in nonempty),
            "empty_population_n": len(empty), "empty_population_exact": avg(p["set_exact"] for p in empty),
            "population_micro_precision": tp / (tp + fp) if tp + fp else None,
            "population_micro_recall": tp / (tp + fn) if tp + fn else None,
            "population_micro_f1": 2 * tp / (2 * tp + fp + fn) if 2 * tp + fp + fn else None,
            "denominator_n": sum(r["denominator_count_exact"] is not None for r in rows),
            "denominator_count_accuracy": avg(r["denominator_count_exact"] for r in rows),
            "denominator_set_n": len(denominator_sets),
            "denominator_set_exact": avg(r["set_exact"] for r in denominator_sets),
            "denominator_set_f1": avg(r["f1"] for r in denominator_sets),
            "abstain_rate": avg(r["abstain"] for r in rows), "partial_evidence_rate": avg(r["partial_evidence"] for r in rows)}
