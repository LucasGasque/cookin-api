from http import HTTPStatus

from flask import jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from sqlalchemy.orm.exc import NoResultFound
from marshmallow import ValidationError

from app.models.users_model import User
from app.schemas.user.get_user_by_id_schema import UserGetByIdSchema


@jwt_required()
def get_user_by_id(user_id: str):

    try:

        authorized_user = get_jwt_identity()
        auth_id = authorized_user["id"]

        UserGetByIdSchema().load({"auth_id": auth_id, "user_id": user_id})

        user = User.query.filter_by(auth_id=user_id).one_or_none()

        if not user:
            raise NoResultFound

        return jsonify(user), HTTPStatus.OK

    except ValidationError as error:
        return {"Error": error.args}, HTTPStatus.BAD_REQUEST

    except NoResultFound:
        return {"Error": "user id not found"}, HTTPStatus.NOT_FOUND
