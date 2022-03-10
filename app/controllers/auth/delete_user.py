from http import HTTPStatus

from flask_jwt_extended import get_jwt_identity, jwt_required
from sqlalchemy.orm.session import Session
from marshmallow import ValidationError
from sqlalchemy.orm.exc import NoResultFound

from app.models.auth_model import Auth
from app.configs.database import db
from app.schemas.auth import DeleteUserSchema


@jwt_required()
def delete_user():
    try:
        user_authorized = get_jwt_identity()
        id = user_authorized["id"]

        DeleteUserSchema().load({"userId": id})

        user_in_auth: Auth = Auth.query.filter_by(id=id).first()

        if not user_in_auth:
            raise NoResultFound

        session: Session = db.session()
        session.delete(user_in_auth)
        session.commit()

        return "", HTTPStatus.NO_CONTENT

    except ValidationError as error:
        return {"Error": error.args}, HTTPStatus.BAD_REQUEST

    except NoResultFound:
        return {"Error": "User not found"}, HTTPStatus.NOT_FOUND
