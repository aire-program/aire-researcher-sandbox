import os

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
DATA_DIR = os.path.join(BASE_DIR, 'data')

ARTICLES_PATH = os.path.join(DATA_DIR, 'sample_texts', 'articles_sample.csv')
NOTES_PATH = os.path.join(DATA_DIR, 'sample_texts', 'notes_sample.csv')
EXPERIMENTS_PATH = os.path.join(DATA_DIR, 'sample_tabular', 'experiments_sample.csv')
METRICS_PATH = os.path.join(DATA_DIR, 'sample_tabular', 'metrics_sample.csv')

PIPELINES_DIR = os.path.join(BASE_DIR, 'pipelines')
