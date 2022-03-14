from http import HTTPStatus
from marshmallow import ValidationError
from sqlalchemy.orm.exc import NoResultFound

from flask import jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from sqlalchemy.orm.session import Session

from app.configs.database import db
from app.models.users_model import User
from app.schemas.user.get_users_schema import UserGetSchema


@jwt_required()
def get_users():
    try:

        authorized_user = get_jwt_identity()
        auth_id = authorized_user["id"]

        UserGetSchema().load({"auth_id": auth_id})

        session: Session = db.session
        user = session.query(User).all()

        if not user:
            raise NoResultFound

        return jsonify({"Users": user}), HTTPStatus.OK

    except ValidationError as error:
        return {"Error": error.args}, HTTPStatus.BAD_REQUEST

    except NoResultFound:
        return {"Error": "No users found"}, HTTPStatus.NOT_FOUND
