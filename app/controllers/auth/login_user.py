from os import access
from flask import jsonify, request
from http import HTTPStatus
from werkzeug.exceptions import Unauthorized
from flask_jwt_extended import create_access_token

from app.models.auths_model import Auth
from app.models.users_model import User


def login_user():

    data_received = request.get_json()
    
    try:
        login_user: Auth = Auth.query.filter_by(email=data_received['email']).first()
        if not login_user.check_password(data_received['password']):
            raise Unauthorized
    
    except Unauthorized:
        return {
            'error': 'email and password missmatch'
        }, HTTPStatus.UNAUTHORIZED
    
    except KeyError as err:
        return {
            'error': f'Missing {err} key.'
        }, HTTPStatus.BAD_REQUEST
    
    
    
    access_token = create_access_token(login_user)
    
    return jsonify({
        "access_token": access_token
    }), HTTPStatus.OK
