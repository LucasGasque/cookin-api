from datetime import datetime as dt
from http import HTTPStatus
from uuid import UUID

from app.configs.database import db
from app.models.recipes_model import Recipe
from app.models.users_model import User
from flask import current_app, jsonify, request
from flask_jwt_extended import get_jwt_identity, jwt_required
from sqlalchemy.orm.session import Session
from werkzeug.exceptions import NotFound, BadRequest
from app.models.user_private_recipes_model import UserPrivateRecipe
from app.utils.is_uuid import is_uuid


@jwt_required()
def update_recipe(recipe_id):

    session: Session = current_app.db.session
    received_data = request.get_json()

    user_id = get_jwt_identity()

    try:
        if not is_uuid(recipe_id):
            raise BadRequest(description={
                'error': 'recipe id type missmatch'
            })
        
        private_recipe: UserPrivateRecipe = UserPrivateRecipe.query.filter_by(recipe_id=recipe_id, user_id=user_id['id']).first()
        
        if not private_recipe:
            raise NotFound(description={
                'error': 'recipe informed is not from this user'
            })        

        recipe_to_update: Recipe = Recipe.query.get(recipe_id)
        for key, value in received_data.items():
            setattr(recipe_to_update, key, value)

        recipe_to_update.updated_at = dt.now()

        session.commit()

        return "", HTTPStatus.NO_CONTENT
    
    except NotFound as e:
        return jsonify(e.description), HTTPStatus.NOT_FOUND
    
    except BadRequest as e:
        return jsonify(e.description), HTTPStatus.BAD_REQUEST
