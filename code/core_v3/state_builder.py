"""Deterministic construction of per-task O_before and O_gold.

A task state is represented as a base ontology snapshot plus a compact mask/delta.
This keeps the benchmark auditable without storing a full ontology per task.
"""
from __future__ import annotations

import copy
import hashlib
import json
from typing import Any, Dict


def _loads(value: Any) -> Any:
    return json.loads(json.dumps(value, ensure_ascii=False))


def _relation(base: Dict[str, Any], rid: str):
    for r in base.get('relations', []):
        if r.get('id') == rid:
            return _loads(r)
    return None


def _class(base: Dict[str, Any], cid: str):
    for c in base.get('classes', []):
        if c.get('id') == cid:
            return _loads(c)
    return None


def _property(base: Dict[str, Any], pid: str):
    for p in base.get('properties', []):
        if p.get('id') == pid:
            return _loads(p)
    return None


def _facts(base: Dict[str, Any], rid: str):
    return [_loads(x) for x in base.get('relation_instances', []) if x.get('relation') == rid]


def _remove_facts(state: Dict[str, Any], relations):
    rels = set(relations or [])
    state['relation_instances'] = [
        x for x in state.get('relation_instances', []) if x.get('relation') not in rels
    ]


def _remove_relation_meta(state: Dict[str, Any], relations):
    rels = set(relations or [])
    state['relations'] = [r for r in state.get('relations', []) if r.get('id') not in rels]


def _remove_individual_attributes(state: Dict[str, Any], properties):
    keys = set()
    for p in properties or []:
        keys.add(str(p).split('.')[-1])
    if not keys:
        return
    for ind in state.get('individuals', []):
        attrs = ind.get('attributes') or {}
        for k in list(attrs):
            if k in keys:
                del attrs[k]


def _restore_individual_attributes(state: Dict[str, Any], base: Dict[str, Any], properties):
    keys = {str(p).split('.')[-1] for p in (properties or [])}
    if not keys:
        return
    base_ind = {x.get('id'): x for x in base.get('individuals', [])}
    for ind in state.get('individuals', []):
        src = base_ind.get(ind.get('id'))
        if not src:
            continue
        src_attrs = src.get('attributes') or {}
        attrs = ind.setdefault('attributes', {})
        for k in keys:
            if k in src_attrs:
                attrs[k] = _loads(src_attrs[k])


def apply_state_spec(base: Dict[str, Any], spec: Dict[str, Any]) -> Dict[str, Any]:
    """Apply one compact state spec to a base ontology snapshot.

    The mask moves the base snapshot to O_before.  The delta then moves O_before
    to O_after.  For `gold_delta.operations`, supported operations are:
      - restore_relation
      - restore_abox_relation
      - restore_class
      - restore_property
      - restore_individual_attribute
      - add_alias_link
    """
    state = _loads(base)
    mask = spec.get('mask') or {}
    remove_relations = list(mask.get('remove_relations') or [])
    remove_classes = list(mask.get('remove_classes') or [])
    remove_properties = list(mask.get('remove_properties') or [])
    remove_alias_links = list(mask.get('remove_alias_links') or [])
    remove_class_parent = list(mask.get('remove_class_parent') or [])
    clear_abox_relations = list(mask.get('clear_abox_relations') or [])

    # Relations removed from T also remove their ABox facts.
    _remove_relation_meta(state, remove_relations)
    _remove_facts(state, set(remove_relations) | set(clear_abox_relations))
    if remove_classes:
        rm = set(remove_classes)
        state['classes'] = [c for c in state.get('classes', []) if c.get('id') not in rm]
    if remove_class_parent:
        rm = set(remove_class_parent)
        for c in state.get('classes', []):
            if c.get('id') in rm:
                c.pop('parent', None)
    if remove_properties:
        rm = set(remove_properties)
        state['properties'] = [p for p in state.get('properties', []) if p.get('id') not in rm]
        _remove_individual_attributes(state, remove_properties)
    if remove_alias_links:
        same_as = state.setdefault('same_as', {})
        for a in remove_alias_links:
            same_as.pop(a, None)

    for op in (spec.get('gold_delta') or {}).get('operations', []):
        kind = op.get('op')
        rid = op.get('id')
        if kind == 'restore_relation' and rid:
            if not any(r.get('id') == rid for r in state.get('relations', [])):
                meta = _relation(base, rid)
                if meta:
                    state.setdefault('relations', []).append(meta)
        elif kind == 'restore_abox_relation' and rid:
            existing = {json.dumps(x, ensure_ascii=False, sort_keys=True) for x in state.get('relation_instances', [])}
            for fact in _facts(base, rid):
                key = json.dumps(fact, ensure_ascii=False, sort_keys=True)
                if key not in existing:
                    state.setdefault('relation_instances', []).append(fact)
                    existing.add(key)
        elif kind == 'restore_class' and rid:
            if not any(c.get('id') == rid for c in state.get('classes', [])):
                meta = _class(base, rid)
                if meta:
                    state.setdefault('classes', []).append(meta)
        elif kind == 'restore_class_parent' and rid:
            meta = _class(base, rid)
            if meta and 'parent' in meta:
                for c in state.get('classes', []):
                    if c.get('id') == rid:
                        c['parent'] = meta['parent']
        elif kind == 'restore_property' and rid:
            if not any(p.get('id') == rid for p in state.get('properties', [])):
                meta = _property(base, rid)
                if meta:
                    state.setdefault('properties', []).append(meta)
        elif kind == 'restore_individual_attribute' and rid:
            _restore_individual_attributes(state, base, [rid])
        elif kind == 'add_alias_link' and op.get('alias'):
            state.setdefault('same_as', {})[op['alias']] = op.get('target')

    return state


def state_stats(state: Dict[str, Any]) -> Dict[str, Any]:
    rel_counts = {}
    for fact in state.get('relation_instances', []):
        rel_counts[fact.get('relation')] = rel_counts.get(fact.get('relation'), 0) + 1
    return {
        'version': state.get('version'),
        'n_classes': len(state.get('classes', [])),
        'n_relations': len(state.get('relations', [])),
        'n_properties': len(state.get('properties', [])),
        'n_relation_instances': len(state.get('relation_instances', [])),
        'relation_counts': dict(sorted(rel_counts.items())),
        'n_same_as': len(state.get('same_as', {})),
    }


def _canonical_state(state: Dict[str, Any]) -> Dict[str, Any]:
    out = _loads(state)
    out['classes'] = sorted(out.get('classes', []), key=lambda x: str(x.get('id') or ''))
    out['properties'] = sorted(out.get('properties', []), key=lambda x: str(x.get('id') or ''))
    out['relations'] = sorted(out.get('relations', []), key=lambda x: str(x.get('id') or ''))
    out['individuals'] = sorted(out.get('individuals', []), key=lambda x: str(x.get('id') or ''))
    uniq = {}
    for x in out.get('relation_instances', []):
        key = json.dumps(x, ensure_ascii=False, sort_keys=True)
        uniq[key] = x
    out['relation_instances'] = sorted(
        uniq.values(),
        key=lambda x: (
            str(x.get('relation') or ''),
            str(x.get('subject') or ''),
            str(x.get('object') or ''),
            str(x.get('role') or ''),
            str(x.get('evidence') or ''),
        ),
    )
    out['same_as'] = dict(sorted((out.get('same_as') or {}).items()))
    return out


def state_hash(state: Dict[str, Any]) -> str:
    payload = json.dumps(_canonical_state(state), ensure_ascii=False, sort_keys=True).encode('utf-8')
    return hashlib.sha256(payload).hexdigest()[:16]
