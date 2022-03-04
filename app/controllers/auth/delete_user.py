from http import HTTPStatus

from flask import current_app
from flask_jwt_extended import get_jwt_identity, jwt_required

from app.models.auth_model import Auth


@jwt_required()
def delete_user():
    user_authorized = get_jwt_identity()

    user_in_auth: Auth = Auth.query.filter_by(email=user_authorized["email"]).first()

    current_app.db.session.delete(user_in_auth)
    current_app.db.session.commit()

    return {}, HTTPStatus.NO_CONTENT