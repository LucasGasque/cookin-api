from http import HTTPStatus

from datetime import datetime as dt

from flask import current_app, jsonify, request
from flask_jwt_extended import get_jwt_identity, jwt_required

from app.models.users_model import User
from app.models.recipes_model import Recipe

from app.schemas.user_recipes.create_recipe_schema import RecipeSchema
from app.services.create_private_recipe_services import verify_values


@jwt_required()
def create_private_recipe():
    try:
        data = request.get_json()

        verify_values(data)
        
        user_id = get_jwt_identity()['id']
        
        user: User = User.query.get(user_id)

        data['created_at'] = str(dt.now())
        data['author'] = user.name

        RecipeSchema().load(data)

        recipe = Recipe(**data)

        current_app.db.session.add(recipe)
        current_app.db.session.commit()

        return jsonify(recipe), HTTPStatus.CREATED

    except AttributeError as e:
        return {"Error": e.args}, HTTPStatus.NOT_FOUND 
