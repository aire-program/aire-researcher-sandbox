import pytest
import pandas as pd
import json
import os
import jsonschema
from app.config import ARTICLES_PATH, NOTES_PATH, EXPERIMENTS_PATH, METRICS_PATH, DATA_DIR

SCHEMA_DIR = os.path.join(DATA_DIR, 'schemas')

def load_schema(name):
    with open(os.path.join(SCHEMA_DIR, name), 'r') as f:
        return json.load(f)

def validate_dataframe(df, schema):
    records = df.to_dict(orient='records')
    for record in records:
        jsonschema.validate(instance=record, schema=schema)

def test_articles_schema():
    df = pd.read_csv(ARTICLES_PATH)
    schema = load_schema('articles.schema.json')
    validate_dataframe(df, schema)

def test_notes_schema():
    df = pd.read_csv(NOTES_PATH)
    schema = load_schema('notes.schema.json')
    validate_dataframe(df, schema)

def test_experiments_schema():
    df = pd.read_csv(EXPERIMENTS_PATH)
    schema = load_schema('experiments.schema.json')
    validate_dataframe(df, schema)

def test_metrics_schema():
    df = pd.read_csv(METRICS_PATH)
    schema = load_schema('metrics.schema.json')
    validate_dataframe(df, schema)
