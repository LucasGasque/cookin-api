from http import HTTPStatus

from datetime import datetime as dt

from marshmallow import ValidationError

from flask import current_app, jsonify, request
from flask_jwt_extended import get_jwt_identity, jwt_required

from app.models.user_private_recipes_model import UserPrivateRecipe

from app.schemas.user_recipes.create_recipe_schema import RecipeSchema
from app.services.create_private_recipe_services import verify_values


@jwt_required()
def create_private_recipe():
    try:
        data = request.get_json()
        
        user_id = get_jwt_identity()['id']

        data['created_at'] = str(dt.now())
        data['updated_at'] = str(dt.now())
        
        recipe = RecipeSchema().load(data)

        verify_values(recipe.__dict__)

        current_app.db.session.add(recipe)
        current_app.db.session.commit()

        user_private_recipe = UserPrivateRecipe(**dict(user_id=user_id, recipe_id=recipe.id))

        current_app.db.session.add(user_private_recipe)
        current_app.db.session.commit()
   
        return jsonify(recipe), HTTPStatus.CREATED

    except ValidationError as error:
        return jsonify({"Error": error.args}), HTTPStatus.BAD_REQUEST

    except AttributeError as error:
        return jsonify({"Error": error.args[0]}), HTTPStatus.CONFLICT