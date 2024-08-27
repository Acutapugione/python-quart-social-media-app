from quart import Quart
from quart_schema import QuartSchema
from .db import DBConfig

app = Quart(__name__)
QuartSchema(app)
from . import routes


def run() -> None:
    try:
        DBConfig.up()
        app.run()
    finally:
        DBConfig.down()
