import os
from pathlib import Path

CODE = Path(__file__).resolve().parents[1]
PAPER_EN = CODE.parent
# Standalone package: put mineru_md under package root; monorepo: use cern_qa root.
ROOT = PAPER_EN if (PAPER_EN / 'output' / 'mineru_md').exists() else PAPER_EN.parent
DATA = PAPER_EN / 'data'
CORPUS_MD = ROOT / 'output' / 'mineru_md'
DOCS_MD = DATA / 'docs'
ANNOTATIONS = DATA / 'raw' / 'doc_annotations.jsonl'
ONTOLOGY = DATA / 'ontology_v2.json'
LEGACY_DATASET = DATA / 'tiers' / 'dataset_v2_exact.jsonl'
DATASET = DATA / 'tiers' / 'dataset_v3_corrected.jsonl'
RESULTS = DATA / 'results_v3'

KEY_DIR = Path(os.environ.get('API_KEY_DIR', str(Path.home() / 'API_KEY')))
OPENROUTER_KEY_PATH = Path(os.environ.get('OPENROUTER_KEY_PATH', str(KEY_DIR / 'openrouter')))
PANSHI_KEY_PATH = Path(os.environ.get('PANSHI_KEY_PATH', str(KEY_DIR / 'panshi.txt')))
QWEN_URL = os.environ.get('QWEN_URL', 'http://127.0.0.1:8000/v1/chat/completions')
QWEN_MODEL = os.environ.get('QWEN_MODEL', 'Qwen3.8-27B')
DEFAULT_MAX_TOKENS = int(os.environ.get('MAX_TOKENS', '4000'))
DEFAULT_TIMEOUT = int(os.environ.get('REQUEST_TIMEOUT', '300'))
