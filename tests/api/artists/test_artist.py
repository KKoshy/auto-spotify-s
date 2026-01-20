import os
import json
import logging
import pytest
from requests import Response
from jsonschema import validate
from libs.api.artists.song_constants import ArtistAPIConstants

log = logging.getLogger(__name__)

@pytest.fixture(scope='class')
def artist(artists):
    artist = artists.get_artist(artist_id=ArtistAPIConstants.artist_id)
    return artist

@pytest.mark.positive
class TestArtistAPI:
    def test_response_code(self, artist):
        log.info("Verifying response code")
        assert artist.status_code == 200

    def test_content_type_header(self, artist):
        log.info("Verifying content type")
        assert artist.headers.get('content-type') == ArtistAPIConstants.json_content

    def test_cache_control_header(self, artist):
        log.info("Verifying cache control")
        assert artist.headers.get("cache-control") == ArtistAPIConstants.cache_control

    def test_retry_after_header(self, artist):
        log.info("Verifying absence of retry after header")
        assert not artist.headers.get(ArtistAPIConstants.retry_after_header)

    def test_json_schema(self, artist):
        log.info("Verifying JSON schema")
        validate(instance=artist.json(), 
                 schema=json.load(open(os.path.join("data", "json_schema", "artist_schema.json"))))
        
    def test_fields(self, artist):
        log.info("Validate data fields")
        data = artist.json()
        assert data.get('id') == ArtistAPIConstants.artist_id
        assert data.get('name') == ArtistAPIConstants.artist_name
        assert data.get('uri') == ArtistAPIConstants.artist_uri


@pytest.mark.negative
class TestNegativeArtistAPI:

    def test_missing_artist_id(self, artists):
        log.info("Verifying Artist API with absence of artist_id path parameter")
        artist: Response = artists.get_artist(artist_id="", 
                                    ignore_handle_response=True)
        assert artist.status_code == 400
        assert artist.json().get('error').get('message') == 'Missing required field: ids'
    
    def test_invalid_artist_id(self, artists):
        log.info("Verifying Artist API with invalid artist_id: None")
        artist = artists.get_artist(artist_id=None, 
                                    ignore_handle_response=True)
        assert artist.status_code == 400
        assert artist.json().get('error').get('message') == 'Invalid base62 id'

    def test_incorrect_artist_id(self, artists):
        incorrect_id = ArtistAPIConstants.artist_id[:-3] + 'abc'
        log.info("Verifying Artist API with incorrect artist_id")
        artist = artists.get_artist(artist_id=incorrect_id, 
                                    ignore_handle_response=True)
        assert artist.status_code == 404
        assert artist.json().get('error').get('message')  == 'Resource not found'

    def test_invalid_token(self, artists):
        log.info("Verifying Artist API with invalid access token")
        artists.token = "abcdefghtijks"
        artists._set_headers()
        artist = artists.get_artist(artist_id=ArtistAPIConstants.artist_id,
                                    ignore_handle_response=True)
        assert artist.status_code == 401
        assert artist.json().get('error').get('message') == 'Invalid access token'
