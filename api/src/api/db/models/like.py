"""
Like: user_id, post_id
"""

from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey
from ..mixins import AutoTableNameMixin
from . import Base


class Like(Base, AutoTableNameMixin):
    user: Mapped["User"] = relationship()
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    post: Mapped["Post"] = relationship()
    post_id: Mapped[int] = mapped_column(ForeignKey("posts.id"))
