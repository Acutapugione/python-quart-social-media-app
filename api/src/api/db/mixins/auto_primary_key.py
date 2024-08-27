from sqlalchemy.orm import (
    Mapped,
    mapped_column,
    declarative_mixin,
)


@declarative_mixin
class AutoPrimaryKeyMixin:
    id: Mapped[int] = mapped_column(primary_key=True)
