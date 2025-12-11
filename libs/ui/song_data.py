import string
import secrets
from dataclasses import dataclass, field

@dataclass
class PlaylistData:
    rand: str = "".join(secrets.choice(string.ascii_lowercase) for _ in range(7))
    name: str = field(init=False, default=f"{rand} playlist")
    pl_id: str = field(init=False, default="")
    description: str = field(init=False, default=f"{rand} playlist description")
