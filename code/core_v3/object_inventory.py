import re
from collections import Counter

def build_inventory(ann):
    stations, station_types, models, data_types, themes, usages, websites, years = set(), set(), set(), set(), set(), set(), set(), set()
    for d, x in ann.items():
        if x.get('website'): websites.add(str(x['website']))
        if x.get('year'): years.add(str(x['year']))
        for s in x.get('stations', []):
            if s.get('name_norm'): stations.add(s['name_norm'])
            if s.get('type_norm'): station_types.add(s['type_norm'])
        for m in x.get('models', []):
            if m.get('name_norm'): models.add(m['name_norm'])
        for u in x.get('data_uses', []):
            if u.get('data_type_norm'): data_types.add(u['data_type_norm'])
            if u.get('theme'): themes.add(u['theme'])
        for u in x.get('usages', []):
            if u.get('usage_norm'): usages.add(u['usage_norm'])
    return {
        'stations': sorted(stations, key=lambda s: (-len(s), s)),
        'station_types': sorted(station_types),
        'models': sorted(models, key=lambda s: (-len(s), s)),
        'data_types': sorted(data_types, key=lambda s: (-len(s), s)),
        'themes': sorted(themes),
        'usages': sorted(usages),
        'websites': sorted(websites),
        'years': sorted(years),
        'special': ['高寒草甸', '草甸生态系统', '温带草原', '土壤呼吸', 'AlpineMeadow', 'station_has_type', 'uses_station', 'applies_model', 'reports_variable', 'hasStationRole', 'hasModelRole', 'sameAs'],
    }

def anchors_of(task_input, inv):
    q = task_input.get('question', '') or ''
    spec = task_input.get('population_spec', {}) or {}
    blob = q + ' ' + json_spec(spec)
    out = []
    for key in ('stations', 'models', 'data_types', 'station_types', 'special'):
        for v in inv.get(key, []):
            if v and v in blob and v not in out:
                out.append(v)
    m = re.search(r'Station="([^"]+)"', blob)
    if m and m.group(1) not in out: out.insert(0, m.group(1))
    return out[:6]

def json_spec(spec):
    import json
    return json.dumps(spec, ensure_ascii=False)
