from sqlalchemy.orm import DeclarativeBase, sessionmaker
from sqlalchemy import create_engine


from .models import (
    Base,
    User,
    Post,
    Comment,
    Like,
)


class DBConfig:
    ENGINE = create_engine("sqlite:///my_db.db", echo=True)
    BASE = Base
    SESSION = sessionmaker(bind=ENGINE)

    @classmethod
    def up(cls):
        cls.BASE.metadata.create_all(bind=cls.ENGINE)

    @classmethod
    def down(cls):
        cls.BASE.metadata.drop_all(bind=cls.ENGINE)
