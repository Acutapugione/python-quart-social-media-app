"""
Post: content, user_id, created_at
"""

from datetime import datetime
from msgspec import Struct
from . import UserIn


class PostIn(Struct, kw_only=True, tag="post"):
    content: str
    user: UserIn
    created: datetime | None = None


class Post(PostIn):
    id: int
