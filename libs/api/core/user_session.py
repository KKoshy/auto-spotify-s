"""
Library for UserSession of Spotify
"""

from libs.api.core.base_session import Session

class UserSession(Session):
    def __init__(self, client_id: str, client_secret: str, refresh_token: str):
        super().__init__()
        self.token_url = "https://accounts.spotify.com/api/token"
        self.client_id = client_id
        self.client_secret = client_secret
        self.refresh_token = refresh_token
        self.token = None
        self._get_token()
        self._set_headers()

    def _get_token(self):
        data = {
            "grant_type": "refresh_token",
            "refresh_token": self.refresh_token,
            "client_id": self.client_id,
            "client_secret": self.client_secret
        }
        response = self.post(self.token_url, data=data)
        response.raise_for_status()
        self.token = response.json()["access_token"]
        self._set_headers()

    def _set_headers(self):
        self.cu_session.headers["Content-Type"] = "application/x-www-form-urlencoded"
        if self.token:
            self.cu_session.headers["Authorization"] = f"Bearer {self.token}"
