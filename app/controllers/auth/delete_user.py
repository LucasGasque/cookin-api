from flask_jwt_extended import jwt_required, get_jwt_identity
from http import HTTPStatus
from app.models.auths_model import Auth
from app.models.users_model import User
from flask import current_app

@jwt_required()
def delete_user():
    user_authorized = get_jwt_identity()

    user_in_auths: Auth = Auth.query.filter_by(
        email=user_authorized["email"]
    ).first()
    
    current_app.db.session.delete(user_in_auths)
    current_app.db.session.commit()

    return {}, HTTPStatus.NO_CONTENT