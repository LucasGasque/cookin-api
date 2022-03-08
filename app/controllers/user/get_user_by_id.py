from http import HTTPStatus

from flask import jsonify
from sqlalchemy.exc import DataError
from flask_jwt_extended import jwt_required

from app.models.users_model import User


@jwt_required()
def get_user_by_id(user_id: str):
    try:
        user = User.query.filter_by(auth_id=user_id).one_or_none()

        return jsonify(user), HTTPStatus.OK
    except DataError: 
        return {"Error": f"user id {user_id} not found"}, HTTPStatus.NOT_FOUND
       