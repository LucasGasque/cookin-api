from flask import request, current_app

from flask_jwt_extended import jwt_required, get_jwt_identity
from sqlalchemy.orm.session import Session
from app.configs.database import db

from app.models.auths_model import Auth
from app.models.users_model import User


@jwt_required()
def update_user():
    
    session: Session = current_app.db.session
    received_data = request.get_json()
    
    user_token = get_jwt_identity()
    
    update_user = Auth.query.filter_by(email=user_token['email']).first()
    
    
    