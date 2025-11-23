from sklearn.feature_extraction.text import TfidfVectorizer
import numpy as np

class EmbeddingsClient:
    """
    A mock client for generating text embeddings using local TF-IDF.
    """
    
    def __init__(self):
        self.vectorizer = TfidfVectorizer(max_features=768)
        # Fit on some dummy data to initialize vocabulary
        self.vectorizer.fit(["dummy text to initialize vectorizer vocabulary with some words"])
        
    def embed(self, texts):
        """
        Generate embeddings for a list of texts.
        
        Args:
            texts (list of str): Texts to embed.
            
        Returns:
            numpy.ndarray: Matrix of embeddings.
        """
        if isinstance(texts, str):
            texts = [texts]
        
        # In a real client, this would call an external API.
        # Here we use local TF-IDF for demonstration.
        return self.vectorizer.transform(texts).toarray()
