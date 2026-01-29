"""
Library for Base session for handling Spotify APIs
"""

import json
import requests
import logging
from typing import Optional, Callable
from jsonschema import validate

log = logging.getLogger(__name__)

class Session:
    def __init__(self):
        self.base_url = "https://api.spotify.com"
        self.cu_session = requests.Session()

    @staticmethod
    def verify_response(response: requests.Response, status_code: int, json_schema: Optional[str]= None):
        log.info("Verifying status code")
        assert response.status_code == status_code
        if json_schema:
            log.info("Verifying JSON schema of response")
            validate(instance=response.json(), 
                 schema=json.load(open(json_schema)))
    
    def process_request(self, 
                        request_method: Callable, 
                        url: str, 
                        json: Optional[dict] = None,
                        data: Optional[dict] = None,
                        params: Optional[dict] = None,
                        status_code: Optional[int] = None,
                        json_schema: Optional[str] = None,
                        ignore_handle_response: bool=False, 
                        ):
        response: requests.Response = request_method(url=url, params=params, json=json, data=data)
        if not ignore_handle_response:
            response.raise_for_status()
        if status_code:
            self.verify_response(response, status_code=status_code, json_schema=json_schema)
        return response
