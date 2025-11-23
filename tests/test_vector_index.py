import pytest
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from app.config import ARTICLES_PATH

def test_vector_index_build_and_query():
    df = pd.read_csv(ARTICLES_PATH)
    texts = df['abstract'].fillna('')
    
    vectorizer = TfidfVectorizer(stop_words='english')
    tfidf_matrix = vectorizer.fit_transform(texts)
    
    assert tfidf_matrix.shape[0] == len(df)
    
    query = "study"
    query_vec = vectorizer.transform([query])
    scores = cosine_similarity(query_vec, tfidf_matrix).flatten()
    
    assert len(scores) == len(df)
    assert scores.max() >= 0
