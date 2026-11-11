import json, re, requests
from . import config

def key_from(path, pattern):
    return re.search(pattern, path.read_text(errors='ignore')).group(0)

def extract_json(raw):
    if not raw: return None
    t = raw.strip()
    if t.startswith('```'):
        t = re.sub(r'^```(?:json)?\s*', '', t)
        t = re.sub(r'\s*```$', '', t)
    for start in (0, t.find('{')):
        if start < 0: continue
        try:
            return json.JSONDecoder().raw_decode(t[start:])[0]
        except Exception:
            pass
    return None

def call_openrouter(messages, model, max_tokens=None, temperature=0.0, reasoning={'enabled': False}):
    key = key_from(config.OPENROUTER_KEY_PATH, r'sk-or-v1-[A-Za-z0-9]+')
    payload = {'model': model, 'messages': messages,
               'max_tokens': max_tokens or config.DEFAULT_MAX_TOKENS,
               'temperature': temperature, 'reasoning': reasoning}
    r = requests.post('https://openrouter.ai/api/v1/chat/completions',
                      headers={'Authorization': f'Bearer {key}', 'Content-Type': 'application/json'},
                      json=payload, timeout=config.DEFAULT_TIMEOUT)
    return r.status_code, r.text

def call_qwen(messages, model=None, max_tokens=None, temperature=0.0, enable_thinking=False):
    payload = {'model': model or config.QWEN_MODEL, 'messages': messages,
               'max_tokens': max_tokens or config.DEFAULT_MAX_TOKENS,
               'temperature': temperature,
               'chat_template_kwargs': {'enable_thinking': enable_thinking}}
    r = requests.post(config.QWEN_URL, json=payload, timeout=config.DEFAULT_TIMEOUT)
    return r.status_code, r.text
