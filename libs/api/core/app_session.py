"""
Library for AppSession of Spotify
"""

from libs.api.core.base_session import Session

class AppSession(Session):
    def __init__(self, client_id: str, client_secret: str):
        super().__init__()
        self.token_url = "https://accounts.spotify.com/api/token"
        self.client_id = client_id
        self.client_secret = client_secret
        self.token = None
        self._get_token()
        self._set_headers()
    
    def _get_token(self):    
        params = {"grant_type": "client_credentials",
                  "client_id": self.client_id,
                  "client_secret": self.client_secret}
        self._set_headers()
        response = self.post(url=self.token_url, params=params)
        self.token = response.json().get("access_token")
        self._set_headers()

    def _set_headers(self):
        self.cu_session.headers["Content-Type"] = "application/x-www-form-urlencoded"
        if self.token:
            self.cu_session.headers["Authorization"] = f"Bearer {self.token}"
