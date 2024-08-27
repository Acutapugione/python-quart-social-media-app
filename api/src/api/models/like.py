"""Like: user_id, post_id"""

from msgspec import Struct
from . import UserIn, PostIn


class LikeIn(Struct, kw_only=True, tag="like"):
    post: PostIn
    user: UserIn


class Like(LikeIn):
    id: int
