"""
Post: content, user_id, created_at
"""

from datetime import datetime
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey
from ..mixins import AutoTableNameMixin
from . import Base


class Post(Base, AutoTableNameMixin):
    content: Mapped[str]
    user: Mapped["User"] = relationship()
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    created_at: Mapped[datetime]
