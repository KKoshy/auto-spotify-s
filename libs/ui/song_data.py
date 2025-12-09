import string
import random
from dataclasses import dataclass, field

@dataclass
class PlaylistData:
    rand: str = "".join(random.choices(string.ascii_lowercase, k=7))
    name: str = field(init=False, default=f"{rand} playlist")
    description: str = field(init=False, default=f"{rand} playlist description")
