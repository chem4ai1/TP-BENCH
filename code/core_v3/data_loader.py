import json, csv, re
from . import config

def load_json(path):
    return json.loads(path.read_text(encoding='utf-8'))

def load_jsonl(path):
    return [json.loads(l) for l in path.read_text(encoding='utf-8').splitlines() if l.strip()]

def load_resources():
    ann = {d['doc_id']: d for d in load_jsonl(config.ANNOTATIONS)}
    md = {}
    for d in ann:
        for p in (config.DOCS_MD / f'{d}.md', config.CORPUS_MD / d / f'{d}.md'):
            if p.exists():
                md[d] = p.read_text(encoding='utf-8', errors='ignore')
                break
        md.setdefault(d, '')
    onto = load_json(config.ONTOLOGY)
    tasks = load_jsonl(config.DATASET)
    return ann, md, onto, tasks

def gold_type(answer, status):
    if status == 'expert_design': return 'expert_behavior'
    if isinstance(answer, bool): return 'bool'
    if isinstance(answer, (int, float)):
        return 'ratio' if isinstance(answer, float) and not float(answer).is_integer() else 'count'
    if isinstance(answer, dict): return 'structured'
    if isinstance(answer, list): return 'list'
    if isinstance(answer, str): return 'text'
    return 'unknown'

def split_task(t):
    """Strictly separate model input from gold. No gold field enters task_input."""
    gold = t.get('gold', {}) or {}
    evaluation = t.get('evaluation') or {'answer': True, 'members': True, 'denominator_count': False, 'reasons': []}
    oe = t.get('ontology_editing', {}) or {}
    trig = oe.get('trigger_annotation', {}) if isinstance(oe.get('trigger_annotation'), dict) else oe
    gt = trig.get('trigger_class')
    if gt == 'verified': gt = None
    x = {
        'id': t.get('id'),
        'tier': t.get('tier'),
        'group': t.get('group'),
        'question': t.get('question_zh') or t.get('question'),
        'population_spec': t.get('population_spec', {}) or {},
    }
    y = {
        'id': t.get('id'),
        'tier': t.get('tier'),
        'group': t.get('group'),
        'status': gold.get('status'),
        'members': set(gold.get('members') or []),
        'answer': gold.get('answer'),
        'numerator': gold.get('numerator'),
        'denominator': gold.get('denominator'),
        'trigger_class': gt,
        'trigger_type': trig.get('trigger_type'),
        'gold_type': gold_type(gold.get('answer'), gold.get('status')),
        'evaluation': evaluation,
        'legacy_id': t.get('legacy_id'),
        'source_status': t.get('source_status'),
        'reference_repaired': t.get('reference_repaired', False),
        'denominator_members': gold.get('denominator_members') or [],
    }
    return x, y
