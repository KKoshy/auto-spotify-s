"""
Library for Artists API
"""

from requests import Response
from typing import Optional
from libs.api.core.app_session import AppSession
from libs.api.log.log_handler import LogHandler

log_handler = LogHandler.logger


class ArtistsAPI(AppSession):
    def __init__(self, client_id: str, client_secret: str):
        super().__init__(client_id=client_id, client_secret=client_secret)
        self.version = "v1"

    @log_handler
    def get_artist(self, artist_id: str, ignore_handle_response: bool = False, status_code: Optional[int] = None, json_schema: Optional[str] = None) -> Response:
        """
        Get Spotify catalog information for a single artist identified by their unique Spotify ID.
        
        :param artist_id: spotify artist id
        :param ignore_handle_response: boolean to ignore response handling (Default: False)
        :param status_code: expected status code
        :param json_schema: path with the expected json schema
        :return: response object
        :reference: https://developer.spotify.com/documentation/web-api/reference/get-an-artist
        """
        return self.process_request(request_method=self.cu_session.get, 
                                    url=self._get_path(f"artists/{artist_id}"), 
                                    ignore_handle_response=ignore_handle_response,
                                    status_code=status_code,
                                    json_schema=json_schema)

    @log_handler
    def get_artists(self, artist_ids: list[str], ignore_handle_response: bool = False) -> Response:
        """
        Get Spotify catalog information for several artists based on their Spotify IDs.        

        :param artist_ids: list of spotify artist ids
        :param ignore_handle_response: boolean to ignore response handling (Default: False)
        :return: response object
        :reference: https://developer.spotify.com/documentation/web-api/reference/get-multiple-artists
        """
        qparams = {"ids": ",".join(artist_ids)}
        return self.process_request(request_method=self.cu_session.get, url=self._get_path("artists"), params=qparams, ignore_handle_response=ignore_handle_response)
    
    @log_handler
    def get_artist_albums(self, 
                          artist_id: str, 
                          include_groups: Optional[list[str]] = None, 
                          market: Optional[str] = None, 
                          limit: Optional[int] = None, 
                          offset: Optional[int] = None,
                          ignore_handle_response: bool = False) ->  Response:
        """
        Get Spotify catalog information about an artist's albums.
        
        :param artist_id: spotify artist id
        :param include_groups: list of album types; valid values are,
                - album
                - single
                - appears_on
                - compilation
        :param market: an ISO 3166-1 alpha-2 country code.
        :param limit: maximum number of items to return;
                - minimum: 1
                - maximum: 50
                - default: 20
        :param offset: index of the first item to return
        :param ignore_handle_response: boolean to ignore response handling (Default: False)
        :return: response object
        :reference: https://developer.spotify.com/documentation/web-api/reference/get-an-artists-albums
        """
        qparams = {}
        if include_groups:
            qparams['include_groups'] = ",".join(include_groups)
        if market:
            qparams['market'] = market
        if limit:
            qparams['limit'] = limit
        if offset:
            qparams['offset'] = offset
        return self.process_request(request_method=self.cu_session.get, url=self._get_path(f"artists/{artist_id}/albums"), params=qparams, ignore_handle_response=ignore_handle_response)

    @log_handler
    def get_artist_top_tracks(self, artist_id: str, market: Optional[str] = None, ignore_handle_response: bool = False) -> Response:
        """
        Get Spotify catalog information about an artist's top tracks by country.
        
        :param artist_id: spotify artist id
        :param market: an ISO 3166-1 alpha-2 country code
        :param ignore_handle_response: boolean to ignore response handling (Default: False)
        :return: response object
        :reference: https://developer.spotify.com/documentation/web-api/reference/get-an-artists-top-tracks
        """
        qparams = {}
        if market:
            qparams["market"] = market
        return self.process_request(request_method=self.cu_session.get, url=self._get_path(f"artists/{artist_id}/top-tracks"), params=qparams, ignore_handle_response=ignore_handle_response)

    @log_handler
    def get_artist_related_artists(self, artist_id: str, ignore_handle_response: bool = False):
        """
        :NOTE: Deprecated
        Get Spotify catalog information about artists similar to a given artist.        

        :param artist_id: spotify artist id
        :param ignore_handle_response: boolean to ignore response handling (Default: False)
        :return: response object
        :reference: https://developer.spotify.com/documentation/web-api/reference/get-an-artists-related-artists
        """
        return self.process_request(request_method=self.cu_session.get, url=self._get_path(f"artists/{artist_id}/related-artists"), ignore_handle_response=ignore_handle_response)
    
    def _get_path(self, path: str) -> str:
        """
        Forms the complete path for the request
        
        :param path: url path
        :return: complete endpoint
        """
        return f"{self.base_url}/{self.version}/{path}"
