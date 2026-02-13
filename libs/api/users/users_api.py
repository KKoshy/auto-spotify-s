"""
Library for Users API
"""

from typing import Optional

from requests import Response

from libs.api.core.user_session import UserSession
from libs.api.log.log_handler import LogHandler

log_handler = LogHandler.logger


class UsersAPI(UserSession):
    def __init__(self, client_id: str, client_secret: str, refresh_token: str):
        super().__init__(
            client_id=client_id,
            client_secret=client_secret,
            refresh_token=refresh_token,
        )
        self.version = "v1"

    @log_handler
    def follow_playlist(
        self,
        playlist_id: str,
        json: dict,
        ignore_handle_response: bool = False,
        status_code: Optional[int] = None,
    ) -> Response:
        """
        Add the current user as a follower of a playlist.

        :param playlist_id: spotify playlist id
        :param json: dict with details
        :param ignore_handle_response: boolean to ignore response handling (Default: False)
        :return: response object
        :reference: https://developer.spotify.com/documentation/web-api/reference/follow-playlist
        """
        return self.process_request(
            request_method=self.cu_session.put,
            url=self._get_path(f"playlists/{playlist_id}/followers"),
            json=json,
            ignore_handle_response=ignore_handle_response,
            status_code=status_code,
        )

    @log_handler
    def unfollow_playlist(
        self,
        playlist_id: str,
        ignore_handle_response: bool = False,
        status_code: Optional[int] = None,
    ) -> Response:
        """
        Remove the current user as a follower of a playlist.

        :param playlist_id: spotify playlist id
        :param json: dict with details
        :param ignore_handle_response: boolean to ignore response handling (Default: False)
        :return: response object
        :reference: https://developer.spotify.com/documentation/web-api/reference/unfollow-playlist
        """
        return self.process_request(
            request_method=self.cu_session.delete,
            url=self._get_path(f"playlists/{playlist_id}/followers"),
            ignore_handle_response=ignore_handle_response,
            status_code=status_code,
        )

    def _get_path(self, path: str) -> str:
        """
        Forms the complete path for the request

        :param path: url path
        :return: complete endpoint
        """
        return f"{self.base_url}/{self.version}/{path}"
