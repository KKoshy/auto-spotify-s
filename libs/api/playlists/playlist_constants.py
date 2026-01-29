import os

class PlaylistAPIConstants:
    nightly_playlist_id = "1Ju3Rs186TgQuou1JCZbjz"
    follow_playlist_payload = {
        "public": True
    }
    add_items_payload = {
        "uris": [
            # believer
            "spotify:track:0pqnGHJpmpxLKifKRmU6WP",
            # blue
            "spotify:track:3be9ACTxtcL6Zm4vJRUiPG",
            # die with a smile
            "spotify:track:2plbrEY59IikOBgBGLjaoe",
        ],
        "position": 0
    }
    remove_items_payload = {
        "tracks": [
            {
                "uri": "spotify:track:0pqnGHJpmpxLKifKRmU6WP",
            },
            {
                "uri": "spotify:track:3be9ACTxtcL6Zm4vJRUiPG",
            },
            {
                "uri": "spotify:track:2plbrEY59IikOBgBGLjaoe",
            }
        ],
        "snapshot_id": "string"
    }
    current_user_playlist_schema = os.path.join("data", "json_schema", "playlists", "current_user_playlist_schema.json")
    add_delete_playlist_items_schema = os.path.join("data", "json_schema", "playlists", "add_delete_playlist_items_schema.json")
    playlist_items_schema = os.path.join("data", "json_schema", "playlists", "playlist_items_schema.json")
