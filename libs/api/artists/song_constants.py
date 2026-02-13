"""
This file holds constants for Artists API
"""

import os


class ArtistAPIConstants:
    artist_id = "0TnOYISbd1XYRBk9myaseg"
    json_content = "application/json; charset=utf-8"
    cache_control = "public, max-age=0"
    retry_after_header = "Retry-After"
    artist_name = "Pitbull"
    artist_uri = "spotify:artist:0TnOYISbd1XYRBk9myaseg"
    artist_schema = os.path.join(
        "data", "json_schema", "artists", "artist_schema.json"
    )
