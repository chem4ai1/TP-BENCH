import re
from collections import Counter, defaultdict
from .object_inventory import anchors_of

GROUP_ALL_DOCS = {'top_k', 'trend', 'crosstab', 'statistical', 'granularity', 'ontology_trigger'}

def _short(s, n=180):
    return re.sub(r'\s+', ' ', str(s or '')).strip()[:n]

def _doc_anchors(d, x, md, anchors):
    hits = []
    blob_parts = []
    for s in x.get('stations', []):
        blob_parts += [str(s.get('name_raw','')), str(s.get('name_norm','')), str(s.get('type_norm','')), str(s.get('evidence',''))]
    for m in x.get('models', []):
        blob_parts += [str(m.get('name_norm','')), str(m.get('evidence',''))]
    for u in x.get('data_uses', []):
        blob_parts += [str(u.get('data_type_norm','')), str(u.get('theme','')), str(u.get('evidence',''))]
    for u in x.get('usages', []):
        blob_parts += [str(u.get('usage_norm','')), str(u.get('evidence',''))]
    text = ' '.join(blob_parts) + ' ' + md.get(d, '')
    for a in anchors:
        if a and a in text: hits.append(a)
    return hits

def _snippets(d, x, md, anchors):
    out = []
    for a in anchors:
        if not a: continue
        for s in x.get('stations', []):
            if a in str(s.get('name_raw','')) or a in str(s.get('name_norm','')) or a in str(s.get('type_norm','')):
                out.append({'anchor': a, 'kind': 'station', 'text': _short(s.get('evidence',''))})
        for m in x.get('models', []):
            if a in str(m.get('name_norm','')):
                out.append({'anchor': a, 'kind': 'model', 'text': _short(m.get('evidence',''))})
        for u in x.get('data_uses', []):
            if a in str(u.get('data_type_norm','')) or a in str(u.get('theme','')):
                out.append({'anchor': a, 'kind': 'data', 'text': _short(u.get('evidence',''))})
        if not any(o['anchor'] == a for o in out) and a in md.get(d, ''):
            i = md[d].find(a)
            out.append({'anchor': a, 'kind': 'md', 'text': _short(md[d][max(0,i-60):i+120])})
    seen = set(); uniq = []
    for o in out:
        k = (o['kind'], o['text'])
        if k in seen: continue
        seen.add(k); uniq.append(o)
    return uniq[:5]

def _corpus_summary(ann, group):
    model = Counter(); stype = Counter(); themes = Counter(); years = Counter(); usages = Counter(); cells = Counter()
    for d, x in ann.items():
        if x.get('year'): years[str(x['year'])] += 1
        for m in x.get('models', []):
            if m.get('name_norm'): model[m['name_norm']] += 1
        for s in x.get('stations', []):
            if s.get('relation') == '使用' and s.get('type_norm'): stype[s['type_norm']] += 1
        for u in x.get('data_uses', []):
            if u.get('theme'): themes[u['theme']] += 1
        for u in x.get('usages', []):
            if u.get('usage_norm'): usages[u['usage_norm']] += 1
            for s in x.get('stations', []):
                if s.get('type_norm'): cells[(u.get('usage_norm'), s.get('type_norm'))] += 1
    return {
        'model_counts': model.most_common(20),
        'station_type_counts': stype.most_common(),
        'theme_counts': themes.most_common(),
        'year_counts': years.most_common(),
        'usage_counts': usages.most_common(),
        'usage_type_cells': [[a,b,c] for (a,b),c in cells.most_common(30)],
    }

def build_evidence(task_input, inv, ann, md, max_docs=12):
    anchors = anchors_of(task_input, inv)
    group = task_input.get('group', '')
    scored = []
    for d, x in ann.items():
        hits = _doc_anchors(d, x, md, anchors)
        richness = len(x.get('stations', [])) + len(x.get('models', [])) + len(x.get('data_uses', [])) + len(x.get('usages', []))
        if hits:
            scored.append((len(hits), richness, d, hits))
        elif group in GROUP_ALL_DOCS and richness:
            scored.append((0, richness, d, []))
    scored.sort(key=lambda z: (-z[0], -z[1], z[2]))
    selected = scored[:max_docs]
    evidence = []
    for _, _, d, hits in selected:
        evidence.append({'doc_id': d, 'anchors': hits, 'snippets': _snippets(d, ann[d], md, anchors)})
    return {
        'anchors': anchors,
        'candidate_docs': [e['doc_id'] for e in evidence],
        'evidence': evidence,
        'corpus_summary': _corpus_summary(ann, group) if group in GROUP_ALL_DOCS else None,
        'build_policy': 'annotation+md evidence only; no gold/source_docs used',
    }
