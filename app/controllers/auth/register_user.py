from http import HTTPStatus
from flask import request
from marshmallow import ValidationError
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm.session import Session

from app.models.auth_model import Auth
from app.schemas.auth.register_user_schema import RegisterUserSchema
from app.schemas.user.user_schema import UserSchema
from app.configs.database import db


def register_user():
    try:
        data = request.get_json()
        new_user_auth_found = None

        name = data.pop("name", None)
        gender = data.pop("gender", None)
        profile_photo = data.pop("profile_photo", None)

        new_user_auth_table = RegisterUserSchema().load(data)

        print(data)

        session: Session = db.session
        session.add(new_user_auth_table)

        new_user_auth_found = Auth.query.filter_by(
            email=new_user_auth_table.email
        ).first()
        auth_id = new_user_auth_found.id

        new_user_part_users = UserSchema().load(
            {
                "name": name,
                "gender": gender,
                "profile_photo": profile_photo,
                "auth_id": auth_id,
            }
        )

        session.add(new_user_part_users)
        session.commit()

        return "", HTTPStatus.CREATED

    except ValidationError as error:
        return {"Error": error.args}, HTTPStatus.BAD_REQUEST

    except IntegrityError:
        return {"Error": "E-mail already registered in database"}, HTTPStatus.CONFLICT
