"""
User: username, email, password_hash, profile_picture
"""

from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import LargeBinary
from ..mixins import AutoTableNameMixin
from . import Base


class User(Base, AutoTableNameMixin):
    username: Mapped[str]
    email: Mapped[str]
    password_hash: Mapped[str]
    profile_picture: Mapped[bytes | None] = mapped_column(LargeBinary, nullable=True)
