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
    auth_id = user_in_auths.id
    user_in_users: User = User.query.filter_by(auth_id=auth_id).first()
    name = user_in_users.name
    
    current_app.db.session.delete(user_in_auths)

    current_app.db.session.commit()

    return {"msg": f"User {name} has been deleted."}, HTTPStatus.NO_CONTENT