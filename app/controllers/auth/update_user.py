from http import HTTPStatus
from flask import request
from flask_jwt_extended import jwt_required, get_jwt_identity
from sqlalchemy.orm.session import Session
from sqlalchemy.orm.exc import NoResultFound
from marshmallow import ValidationError

from app.models.auth_model import Auth
from app.configs.database import db
from app.schemas.auth import UpdateUserSchema


@jwt_required()
def update_user():
    try:
        received_data = request.get_json()
        user_token = get_jwt_identity()
        id = user_token["id"]

        data = received_data
        data["auth_id"] = id

        UpdateUserSchema().load(data)

        update_user: Auth = Auth.query.filter_by(id=id).first()

        if not update_user:
            raise NoResultFound

        session: Session = db.session

        for key, value in received_data.items():
            setattr(update_user, key, value)

        for key, value in received_data.items():
            setattr(update_user.user, key, value)

        session.commit()

        return "", HTTPStatus.OK

    except NoResultFound:
        return {"Error": "User not found"}

    except ValidationError as error:
        return {"Error": error.args}, HTTPStatus.BAD_REQUEST
