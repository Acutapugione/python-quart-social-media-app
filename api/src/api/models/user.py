"""
User: username, email, password_hash, profile_picture
Comment: content, user_id, post_id
"""

from msgspec import Struct


class UserIn(Struct, kw_only=True, tag="user"):
    username: str
    email: str
    password_hash: str
    profile_picture: bytes | None = None


class User(UserIn):
    id: int
