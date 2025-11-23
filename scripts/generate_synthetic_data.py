import pandas as pd
import numpy as np
import os
import random
from datetime import datetime, timedelta

# Set fixed random seed for reproducibility
SEED = 42
np.random.seed(SEED)
random.seed(SEED)

DATA_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'data'))
TEXT_DIR = os.path.join(DATA_DIR, 'sample_texts')
TABULAR_DIR = os.path.join(DATA_DIR, 'sample_tabular')

def ensure_dirs():
    os.makedirs(TEXT_DIR, exist_ok=True)
    os.makedirs(TABULAR_DIR, exist_ok=True)

def generate_articles(n=100):
    print(f"Generating {n} articles...")
    titles = [
        f"Study on {topic} {suffix}" 
        for topic in ["Neural Networks", "Climate Change", "Social Dynamics", "Quantum Computing", "Genomics"]
        for suffix in ["Analysis", "Review", "Survey", "Experiments", "Methodology"]
    ]
    # Ensure we have enough unique titles or just sample with replacement if needed, 
    # but for 100 rows we can generate random strings if needed. 
    # Let's make them a bit more dynamic to reach N.
    
    data = []
    for i in range(n):
        article_id = f"ART-{i:04d}"
        title = f"{random.choice(['Advanced', 'Novel', 'Comparative', 'Longitudinal'])} Study of {random.choice(['AI', 'Biology', 'Sociology', 'Economics'])}: {random.randint(1, 1000)}"
        abstract = f"This paper explores {title.lower()}. We find significant results in area {random.randint(1, 10)}. The methodology involves {random.choice(['qualitative', 'quantitative', 'mixed-methods'])} analysis."
        data.append({"article_id": article_id, "title": title, "abstract": abstract})
    
    df = pd.DataFrame(data)
    output_path = os.path.join(TEXT_DIR, 'articles_sample.csv')
    df.to_csv(output_path, index=False)
    print(f"Saved {len(df)} rows to {output_path}")

def generate_notes(n=100):
    print(f"Generating {n} notes...")
    data = []
    for i in range(n):
        note_id = f"NOTE-{i:04d}"
        note_text = f"Observation {i}: The subject demonstrated {random.choice(['high', 'low', 'moderate'])} engagement. Follow-up required on {random.choice(['Monday', 'Tuesday', 'Wednesday'])}."
        data.append({"note_id": note_id, "note_text": note_text})
    
    df = pd.DataFrame(data)
    output_path = os.path.join(TEXT_DIR, 'notes_sample.csv')
    df.to_csv(output_path, index=False)
    print(f"Saved {len(df)} rows to {output_path}")

def generate_experiments(n=100):
    print(f"Generating {n} experiment records...")
    data = []
    start_date = datetime(2023, 1, 1)
    for i in range(n):
        experiment_id = f"EXP-{i:04d}"
        condition = random.choice(["control", "treatment_A", "treatment_B"])
        metric_value = round(random.uniform(0, 100), 2)
        # Random timestamp within last year
        timestamp = start_date + timedelta(days=random.randint(0, 365), hours=random.randint(0, 23), minutes=random.randint(0, 59), seconds=random.randint(0, 59))
        data.append({
            "experiment_id": experiment_id,
            "condition": condition,
            "metric_value": metric_value,
            "timestamp": timestamp.isoformat()
        })
    
    df = pd.DataFrame(data)
    output_path = os.path.join(TABULAR_DIR, 'experiments_sample.csv')
    df.to_csv(output_path, index=False)
    print(f"Saved {len(df)} rows to {output_path}")

def generate_metrics(n=100):
    print(f"Generating {n} metric records...")
    data = []
    for i in range(n):
        record_id = f"REC-{i:04d}"
        category = random.choice(["throughput", "accuracy", "latency", "error_rate"])
        value = round(random.uniform(0, 1) if category == "error_rate" else random.uniform(10, 1000), 4)
        data.append({"record_id": record_id, "category": category, "value": value})
    
    df = pd.DataFrame(data)
    output_path = os.path.join(TABULAR_DIR, 'metrics_sample.csv')
    df.to_csv(output_path, index=False)
    print(f"Saved {len(df)} rows to {output_path}")

def main():
    ensure_dirs()
    generate_articles(150)
    generate_notes(120)
    generate_experiments(180)
    generate_metrics(200)
    print("Synthetic data generation complete.")

if __name__ == "__main__":
    main()
