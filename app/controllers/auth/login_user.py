from datetime import timedelta
from http import HTTPStatus
from flask import jsonify, request
from flask_jwt_extended import create_access_token
from werkzeug.exceptions import Unauthorized
from marshmallow import ValidationError
from sqlalchemy.orm.exc import NoResultFound


from app.models.auth_model import Auth
from app.schemas.auth import LoginUserSchema


def login_user():
    try:
        data_recivied = request.get_json()
        data = LoginUserSchema().load(data_recivied)

        login_user: Auth = Auth.query.filter_by(email=data["email"]).first()

        if not login_user:
            raise NoResultFound

        if not login_user.check_password(data["password"]):
            raise Unauthorized

        access_token = create_access_token(
            login_user, expires_delta=timedelta(hours=24)
        )

        return (
            jsonify(
                {
                    "name": login_user.user.name,
                    "gender": login_user.user.gender,
                    "profile_photo": login_user.user.profile_photo,
                    "access_token": access_token,
                }
            ),
            HTTPStatus.OK,
        )

    except ValidationError as error:
        return {"Error": error.args}, HTTPStatus.BAD_REQUEST

    except NoResultFound:
        return {"Error": "Email and password missmatch"}, HTTPStatus.UNAUTHORIZED

    except Unauthorized:
        return {"Error": "Email and password missmatch"}, HTTPStatus.UNAUTHORIZED
