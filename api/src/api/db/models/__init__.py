"""
Base: id, __tablename__
User: username, email, password_hash, profile_picture
Post: content, user_id, created_at
Like: user_id, post_id
Comment: content, user_id, post_id
"""

from .base import Base
from .user import User
from .post import Post
from .comment import Comment
from .like import Like
