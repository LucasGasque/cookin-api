from flask import request, current_app
from http import HTTPStatus
from flask_jwt_extended import jwt_required, get_jwt_identity
from sqlalchemy.orm.session import Session
from app.configs.database import db

from app.models.auths_model import Auth


@jwt_required()
def update_user():
    
    session: Session = current_app.db.session
    received_data = request.get_json()
    
    user_token = get_jwt_identity()    
    update_user: Auth = Auth.query.filter_by(email=user_token['email']).first()    
    
    for key, value in received_data.items():
        setattr(update_user, key, value)
    
    for key, value in received_data.items():
        setattr(update_user.user, key, value) 
    
    session.commit()   
    
    return '', HTTPStatus.OK
    