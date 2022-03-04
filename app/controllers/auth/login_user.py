from datetime import timedelta
from http import HTTPStatus

from app.models.auth_model import Auth
from flask import jsonify, request
from flask_jwt_extended import create_access_token
from werkzeug.exceptions import Unauthorized


def login_user():

    data_received = request.get_json()

    try:
        login_user: Auth = Auth.query.filter_by(email=data_received["email"]).first()
        if not login_user.check_password(data_received["password"]):
            raise Unauthorized

    except Unauthorized:
        return {"error": "email and password missmatch"}, HTTPStatus.UNAUTHORIZED

    except KeyError as err:
        return {"error": f"Missing {err} key."}, HTTPStatus.BAD_REQUEST

    access_token = create_access_token(login_user, expires_delta=timedelta(hours=24))

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
