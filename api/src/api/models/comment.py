"""Like: user_id, post_id"""

from msgspec import Struct
from . import UserIn, PostIn


class CommentIn(Struct, kw_only=True, tag="comment"):
    content: str
    post: PostIn
    user: UserIn


class Comment(CommentIn):
    id: int
