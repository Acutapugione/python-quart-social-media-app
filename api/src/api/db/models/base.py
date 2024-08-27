"""
Base: id, __tablename__
"""

from sqlalchemy.orm import DeclarativeBase
from ..mixins import AutoTableNameMixin, AutoPrimaryKeyMixin


class Base(DeclarativeBase, AutoTableNameMixin, AutoPrimaryKeyMixin): ...
