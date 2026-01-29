import logging
import pytest
from data.api.response_constants import ResponseConstants
from libs.api.playlists.playlists_api import PlaylistsAPI
from libs.api.playlists.playlist_constants import PlaylistAPIConstants
from libs.api.users.users_api import UsersAPI

log = logging.getLogger(__name__)

SNAPSHOT_ID = None

@pytest.mark.positive
class TestPlaylistsAPI:
    @pytest.mark.dependency(name='follow')
    def test_follow_playlist(self, playlists: PlaylistsAPI, users: UsersAPI):
        log.info("Verifying follow playlist")
        users.follow_playlist(playlist_id=PlaylistAPIConstants.nightly_playlist_id, 
                              json=PlaylistAPIConstants.follow_playlist_payload,
                              status_code=ResponseConstants.status_200)
        user_playlists  = playlists.get_current_user_playlists(
            status_code=ResponseConstants.status_200,
            json_schema=PlaylistAPIConstants.current_user_playlist_schema)
        playlist_ids = [item['id'] for item in user_playlists.json()['items']]
        assert PlaylistAPIConstants.nightly_playlist_id in playlist_ids

    @pytest.mark.dependency(name='add_items', depends=['follow'])
    def test_add_playlist_items(self, playlists: PlaylistsAPI):
        log.info("Verifying adding items to playlist")
        add_items = playlists.add_playlist_items(playlist_id=PlaylistAPIConstants.nightly_playlist_id, 
                                                 json=PlaylistAPIConstants.add_items_payload,
                                                 status_code=ResponseConstants.status_201,
                                                 json_schema=PlaylistAPIConstants.add_delete_playlist_items_schema)
        global SNAPSHOT_ID
        SNAPSHOT_ID = add_items.json().get('snapshot_id')
        current_user_items = playlists.get_playlist_items(playlist_id=PlaylistAPIConstants.nightly_playlist_id,
                                                     status_code=ResponseConstants.status_200,
                                                     json_schema=PlaylistAPIConstants.playlist_items_schema)
        uris = [item['track']['uri'] for item in current_user_items.json()['items']]
        assert set(PlaylistAPIConstants.add_items_payload['uris']).issubset(set(uris))

    @pytest.mark.dependency(depends=['add_items'])
    def test_remove_playlist_items(self, playlists: PlaylistsAPI):
        log.info("Verifying removal of items from playlist")
        PlaylistAPIConstants.remove_items_payload["snapshot_id"] = SNAPSHOT_ID
        remove_items = playlists.remove_playlist_items(playlist_id=PlaylistAPIConstants.nightly_playlist_id,
                                                       json=PlaylistAPIConstants.remove_items_payload,
                                                       status_code=ResponseConstants.status_200,
                                                       json_schema=PlaylistAPIConstants.add_delete_playlist_items_schema)
        current_user_items = playlists.get_playlist_items(playlist_id=PlaylistAPIConstants.nightly_playlist_id,
                                                     status_code=ResponseConstants.status_200,
                                                     json_schema=PlaylistAPIConstants.playlist_items_schema)
        uris = [item['track']['uri'] for item in current_user_items.json()['items']]
        assert set(PlaylistAPIConstants.add_items_payload['uris']).isdisjoint(set(uris))

    @pytest.mark.dependency(depends=['follow'])
    def test_unfollow_playlist(self, playlists: PlaylistsAPI, users: UsersAPI):
        log.info("Verifying unfollow playlist")
        users.unfollow_playlist(playlist_id=PlaylistAPIConstants.nightly_playlist_id,
                                status_code=ResponseConstants.status_200)
        user_playlists = playlists.get_current_user_playlists(status_code=ResponseConstants.status_200,
                                             json_schema=PlaylistAPIConstants.current_user_playlist_schema)
        playlist_ids = [item['id'] for item in user_playlists.json()['items']]
        assert PlaylistAPIConstants.nightly_playlist_id not in playlist_ids
