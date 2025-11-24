import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

def search(query_vec, index_matrix, top_k: int = 5):
    """Retrieve top_k documents using cosine similarity."""
    sims = cosine_similarity(query_vec, index_matrix).flatten()
    indices = sims.argsort()[::-1][:top_k]
    return indices, sims[indices]