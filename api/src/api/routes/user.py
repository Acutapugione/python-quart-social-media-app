from quart_schema import validate_request, validate_response
from ..models import UserIn, User
from ..db import User as DBUser, DBConfig
from .. import app


@app.post("/users/")
@validate_request(UserIn)
@validate_response(User)
async def create_todo(data: UserIn) -> User:
    with DBConfig.SESSION.begin() as session:
        user = DBUser(
            username=data.username,
            email=data.email,
            password_hash=data.password_hash,
            profile_picture=data.profile_picture,
        )

        session.add(user)
        session.flush()

        return User(
            id=user.id,
            username=user.username,
            email=user.email,
            password_hash=user.password_hash,
            profile_picture=user.profile_picture,
        )
