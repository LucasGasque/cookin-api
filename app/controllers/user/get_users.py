from http import HTTPStatus

from flask import jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from sqlalchemy.orm.session import Session

from app.configs.database import db
from app.models.users_model import User
from app.schemas.user.get_users_schema import UserGetSchema


@jwt_required()
def get_users():
        
    authorized_user = get_jwt_identity()
    auth_id = authorized_user["id"]

    UserGetSchema().load({"auth_id": auth_id})

    session: Session = db.session
    user = session.query(User).all()

    if not user:
        return {"Error": "No users found"}, HTTPStatus.NOT_FOUND

    return jsonify({"Users": user}), HTTPStatus.OK
