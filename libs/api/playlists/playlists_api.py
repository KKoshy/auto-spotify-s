"""
Library for Playlists API
"""

import base64
from requests import Response
from libs.api.core.user_session import UserSession
from libs.api.log.log_handler import LogHandler

log_handler = LogHandler.logger


class PlaylistsAPI(UserSession):
    def __init__(self, client_id: str, client_secret: str, refresh_token: str):
        super().__init__(client_id=client_id, client_secret=client_secret, refresh_token=refresh_token)
        self.version = "v1"

    @log_handler
    def get_playlist(self, playlist_id: str, ignore_handle_response: bool = False) -> Response:
        """
        Get a playlist owned by a Spotify user.
        
        :param playlist_id: spotify playlist id
        :param ignore_handle_response: boolean to ignore response handling (Default: False)
        :return: response object
        :reference: https://developer.spotify.com/documentation/web-api/reference/get-playlist
        """
        return self.get(url=self._get_path(f"playlists/{playlist_id}"), ignore_handle_response=ignore_handle_response)

    @log_handler
    def update_playlist_details(self, playlist_id: str, json: dict, ignore_handle_response: bool = False) -> Response:
        """
        Change a playlist's name and public/private state. (The user must own the playlist.)   

        :param playlist_id: spotify playlist id
        :param json: dict containing updated details
        :param ignore_handle_response: boolean to ignore response handling (Default: False)
        :return: response object
        :reference: https://developer.spotify.com/documentation/web-api/reference/change-playlist-details
        """
        return self.put(url=self._get_path(f"playlists/{playlist_id}"), json=json, ignore_handle_response=ignore_handle_response)
    
    @log_handler
    def get_playlist_items(self, playlist_id: str, ignore_handle_response: bool = False) -> Response:
        """
        Get full details of the items of a playlist owned by a Spotify user.
        
        :param playlist_id: spotify playlist id
        :param ignore_handle_response: boolean to ignore response handling (Default: False)
        :return: response object
        :reference: https://developer.spotify.com/documentation/web-api/reference/get-playlists-tracks
        """
        return self.get(url=self._get_path(f"playlists/{playlist_id}/tracks"), ignore_handle_response=ignore_handle_response)

    @log_handler
    def update_playlist_items(self, playlist_id: str, json: dict, ignore_handle_response: bool = False) -> Response:
        """
        Either reorder or replace items in a playlist depending on the request's parameters.
        
        :param playlist_id: spotify playlist id
        :param json: dict containing updated details
        :param ignore_handle_response: boolean to ignore response handling (Default: False)
        :return: response object
        :reference: https://developer.spotify.com/documentation/web-api/reference/reorder-or-replace-playlists-tracks
        """
        return self.put(url=self._get_path(f"playlists/{playlist_id}/tracks"), json=json, ignore_handle_response=ignore_handle_response)

    @log_handler
    def add_playlist_items(self, playlist_id: str, json: dict, ignore_handle_response: bool = False) -> Response:
        """
        Add one or more items to a user's playlist.
        
        :param playlist_id: spotify playlist id
        :param json: dict containing playlist items
        :param ignore_handle_response: boolean to ignore response handling (Default: False)
        :return: response object
        :reference: https://developer.spotify.com/documentation/web-api/reference/add-tracks-to-playlist
        """
        return self.post(url=self._get_path(f"playlists/{playlist_id}/tracks"), json=json, ignore_handle_response=ignore_handle_response)

    @log_handler
    def remove_playlist_items(self, playlist_id: str, json: dict, ignore_handle_response: bool = False) -> Response:
        """
        Remove one or more items from a user's playlist.
        
        :param playlist_id: spotify playlist id
        :param json: dict containing playlist items
        :param ignore_handle_response: boolean to ignore response handling (Default: False)
        :return: response object
        :reference: https://developer.spotify.com/documentation/web-api/reference/remove-tracks-playlist
        """
        return self.delete(url=self._get_path(f"playlists/{playlist_id}/tracks"), json=json, ignore_handle_response=ignore_handle_response)

    @log_handler
    def get_current_user_playlists(self, ignore_handle_response: bool = False) -> Response:
        """
        Get a list of the playlists owned or followed by the current Spotify user.
        
        :param ignore_handle_response: boolean to ignore response handling (Default: False)
        :return: response object
        :reference: https://developer.spotify.com/documentation/web-api/reference/get-a-list-of-current-users-playlists
        """
        return self.get(url=self._get_path(f"me/playlists"), ignore_handle_response=ignore_handle_response)
    
    @log_handler
    def get_user_playlists(self, user_id: str, ignore_handle_response: bool = False) -> Response:
        """
        Get a list of the playlists owned or followed by a Spotify user.

        :param user_id: spotify user id 
        :param ignore_handle_response: boolean to ignore response handling (Default: False)
        :return: response object
        :reference: https://developer.spotify.com/documentation/web-api/reference/get-list-users-playlists
        """
        return self.get(url=self._get_path(f"users/{user_id}/playlists"), ignore_handle_response=ignore_handle_response)

    @log_handler
    def create_playlist(self, user_id: str, json: dict, ignore_handle_response: bool = False) -> Response:
        """
        Create a playlist for a Spotify user.
        
        :param user_id: spotify user id 
        :param json: dict containing playlist details
        :param ignore_handle_response: boolean to ignore response handling (Default: False)
        :return: response object
        :reference: https://developer.spotify.com/documentation/web-api/reference/create-playlist
        """
        return self.post(url=self._get_path(f"users/{user_id}/playlists"), json=json, ignore_handle_response=ignore_handle_response)

    @log_handler
    def get_playlist_cover_image(self, playlist_id: str, ignore_handle_response: bool = False) -> Response:
        """
        Get the current image associated with a specific playlist.

        :param playlist_id: spotify playlist id
        :param ignore_handle_response: boolean to ignore response handling (Default: False)
        :return: response object
        :reference: https://developer.spotify.com/documentation/web-api/reference/get-playlist-cover
        """
        return self.get(url=self._get_path(f"playlists/{playlist_id}/images"), ignore_handle_response=ignore_handle_response)
    
    @log_handler
    def add_custom_playlist_cover_image(self, playlist_id: str, image_path: str, ignore_handle_response: bool = False) -> Response:
        """
        Add Custom Playlist Cover Image.
        
        :param playlist_id: spotify playlist id
        :param image_path: path to the image file (maximum payload size is 256 KB)
        :param ignore_handle_response: boolean to ignore response handling (Default: False)
        :return: response object
        :reference: https://developer.spotify.com/documentation/web-api/reference/upload-custom-playlist-cover
        """
        self.cu_session.headers["Content-Type"] = 'image/jpeg'
        with open(image_path, "rb") as f:
            image_data = base64.b64encode(f.read()).decode()
        return self.put(url=self._get_path(f"playlists/{playlist_id}/images"), data=image_data, ignore_handle_response=ignore_handle_response)    

    def _get_path(self, path: str) -> str:
        """
        Forms the complete path for the request
        
        :param path: url path
        :return: complete endpoint
        """
        return f"{self.base_url}/{self.version}/{path}"
