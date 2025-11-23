import requests
import time

class ResearchAPIClient:
    """
    A mock client for interacting with a hypothetical research data API.
    """
    
    def __init__(self, base_url="https://api.example.research.msu.edu"):
        self.base_url = base_url
    
    def get_status(self):
        """
        Check API status.
        """
        return {"status": "online", "timestamp": time.time()}
    
    def get_projects(self):
        """
        Retrieve a list of active research projects.
        """
        # Mock response
        return [
            {"id": "PROJ-001", "name": "AI in Education", "pi": "Dr. Smith"},
            {"id": "PROJ-002", "name": "Climate Modeling", "pi": "Dr. Jones"}
        ]
    
    def get_dataset(self, dataset_id):
        """
        Retrieve metadata for a specific dataset.
        """
        return {
            "id": dataset_id,
            "size_mb": 1024,
            "format": "csv",
            "access_level": "restricted"
        }
