import requests

class Session:
    def __init__(self, client_id: str, client_secret: str):
        self.cu_session = requests.Session()
        self.base_url = "https://api.spotify.com"
        self.client_id = client_id
        self.client_secret = client_secret
        self.token = None
        self._get_token()
        self._set_headers()

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

    def _get_token(self):
        token_url = "https://accounts.spotify.com/api/token"
        params = {"grant_type": "client_credentials",
                  "client_id": self.client_id,
                  "client_secret": self.client_secret}
        self._set_headers()
        response = self.post(url=token_url, params=params)
        self.token = response.json().get("access_token")
        self._set_headers()


    def _set_headers(self):
        self.cu_session.headers["Content-Type"] = "application/x-www-form-urlencoded"
        if self.token:
            self.cu_session.headers["Authorization"] = f"Bearer {self.token}"
