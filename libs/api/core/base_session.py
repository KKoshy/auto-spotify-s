"""
Library for Base session for handling Spotify APIs
"""

import requests

class Session:
    def __init__(self):
        self.base_url = "https://api.spotify.com"
        self.cu_session = requests.Session()

    def get(self, url: str, ignore_handle_response: bool=False,  **kwargs):
        response = self.cu_session.get(url=url, **kwargs)
        if not ignore_handle_response:
            response.raise_for_status()
        return response
    
    def post(self, url: str, ignore_handle_response: bool=False, **kwargs):
        response = self.cu_session.post(url=url, **kwargs)
        if not ignore_handle_response:
            response.raise_for_status()
        return response
    
    def put(self, url: str, ignore_handle_response: bool=False, **kwargs):
        response = self.cu_session.put(url=url, **kwargs)
        if not ignore_handle_response:
            response.raise_for_status()
        return response
    
    def delete(self, url: str, ignore_handle_response: bool=False, **kwargs):
        response = self.cu_session.delete(url=url, **kwargs)
        if not ignore_handle_response:
            response.raise_for_status()
        return response
