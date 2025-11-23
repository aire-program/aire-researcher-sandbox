import pytest
import numpy as np
from api.python.client_rest_api import ResearchAPIClient
from api.python.client_embeddings import EmbeddingsClient

def test_rest_api_client():
    client = ResearchAPIClient()
    status = client.get_status()
    assert status['status'] == 'online'
    
    projects = client.get_projects()
    assert isinstance(projects, list)
    assert len(projects) > 0
    assert 'id' in projects[0]

def test_embeddings_client():
    client = EmbeddingsClient()
    texts = ["Hello world", "Test sentence"]
    embeddings = client.embed(texts)
    
    assert isinstance(embeddings, np.ndarray)
    assert embeddings.shape[0] == 2
    assert embeddings.shape[1] > 0
