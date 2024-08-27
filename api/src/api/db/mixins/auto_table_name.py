from sqlalchemy.orm import (
    declared_attr,
    declarative_mixin,
)


@declarative_mixin
class AutoTableNameMixin:
    @declared_attr
    def __tablename__(cls):
        return cls.__name__.lower() + "s"
