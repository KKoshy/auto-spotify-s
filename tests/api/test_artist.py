import os
import json
import logging
import pytest
from jsonschema import validate
from libs.api.song_constants import ArtistAPIConstants

log = logging.getLogger(__name__)

@pytest.fixture(scope='class')
def artist(artists):
    artist = artists.get_artist(artist_id=ArtistAPIConstants.artist_id)
    return artist


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
