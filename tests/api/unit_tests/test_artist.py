"""
Unit test suite for Artist API
"""

import logging
import pytest
from data.api.response_constants import ResponseConstants
from libs.api.artists.song_constants import ArtistAPIConstants

log = logging.getLogger(__name__)

@pytest.fixture(scope='class')
def artist(artists):
    artist = artists.get_artist(artist_id=ArtistAPIConstants.artist_id,
                                status_code=ResponseConstants.status_200,
                                json_schema=ArtistAPIConstants.artist_schema)
    return artist

@pytest.mark.positive
class TestArtistAPI:
    def test_content_type_header(self, artist):
        log.info("Verifying content type.")
        assert artist.headers.get('content-type') == ArtistAPIConstants.json_content

    def test_cache_control_header(self, artist):
        log.info("Verifying cache control")
        assert artist.headers.get("cache-control") == ArtistAPIConstants.cache_control

    def test_retry_after_header(self, artist):
        log.info("Verifying absence of retry after header")
        assert not artist.headers.get(ArtistAPIConstants.retry_after_header)
        
    def test_fields(self, artist):
        log.info("Validate data fields")
        data = artist.json()
        assert data.get('id') == ArtistAPIConstants.artist_id
        assert data.get('name') == ArtistAPIConstants.artist_name
        assert data.get('uri') == ArtistAPIConstants.artist_uri


@pytest.mark.negative
class TestNegativeArtistAPI:
    @pytest.mark.parametrize("artist_id,status_code,token,message",
                             [("", ResponseConstants.status_400, None, 'Missing required field: ids'),
                              (None, ResponseConstants.status_400, None, 'Invalid base62 id'),
                              (ArtistAPIConstants.artist_id[:-3] + 'abc', ResponseConstants.status_404, None, 'Resource not found'),
                              (ArtistAPIConstants.artist_id, ResponseConstants.status_401, "asdoinsadnfasoidnsione", 'Invalid access token'),],
                              ids=["missing_artist_id", "invalid_id", "incorrect_id", "invalid_token"])
    def test_negative_case(self, artists, artist_id, token, status_code,message):
        log.info("Verifying negative case of Artist API")
        if token:
            artists.token = token
            artists._set_headers()
        artist = artists.get_artist(artist_id=artist_id,
                                    ignore_handle_response=True)
        assert artist.status_code == status_code
        assert artist.json().get('error').get('message') == message
