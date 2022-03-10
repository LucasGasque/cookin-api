from datetime import datetime as dt
from http import HTTPStatus

from app.configs.database import db
from app.models.recipes_model import Recipe
from flask import jsonify, request
from flask_jwt_extended import get_jwt_identity, jwt_required
from sqlalchemy.orm.session import Session
from werkzeug.exceptions import NotFound, BadRequest, Conflict
from app.models.user_private_recipes_model import UserPrivateRecipe
from app.schemas.user_recipes.update_private_recipe_schema import UpdatePrivateRecipeSchema
from marshmallow.exceptions import ValidationError
from  app.services.update_private_recipe_services import (
    verify_recipe_title, 
    verify_repeated_ingredients, 
    verify_repeated_instructions
    )


@jwt_required()
def update_private_recipe(recipe_id):
    try:
        data = request.get_json()
        session: Session = db.session
        
        data['recipe_id'] = recipe_id
        
        UpdatePrivateRecipeSchema().load(data)

        user_id = get_jwt_identity()
        private_recipe: UserPrivateRecipe = UserPrivateRecipe.query.filter_by(
            recipe_id=recipe_id, user_id=user_id["id"]
        ).first()

        if not private_recipe:
            raise NotFound(
                description={"Error": "recipe from the id informed is not from this user or do not exist."}
            )

        verify_recipe_title(data.get('title'))
        
        verify_repeated_ingredients(data.get('ingredients'))
       
        verify_repeated_instructions(data.get('instructions'))
        
        recipe_to_update: Recipe = Recipe.query.get(recipe_id)

        for key, value in data.items():
            setattr(recipe_to_update, key, value)

        recipe_to_update.updated_at = str(dt.now())
        
        session.commit()
        
        return "", HTTPStatus.NO_CONTENT

    except NotFound as error:
        return jsonify(error.description), HTTPStatus.NOT_FOUND

    except BadRequest as error:
        return jsonify(error.description), HTTPStatus.BAD_REQUEST
    
    except Conflict as error:
        return jsonify(error.description), HTTPStatus.CONFLICT
    
    except ValidationError as error:
        return jsonify({
            'Error': error.messages
        }),HTTPStatus.BAD_REQUEST
