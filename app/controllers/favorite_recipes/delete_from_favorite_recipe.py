from http import HTTPStatus

from app.configs.database import db
from app.schemas.favorite_recipes.delete_from_favorite_recipe_schema import DeleteFromFavoritesRecipeSchema
from flask import jsonify
from flask_jwt_extended import get_jwt_identity, jwt_required
from marshmallow.exceptions import ValidationError
from sqlalchemy.orm.session import Session
from app.models.favorite_recipes_model import FavoriteRecipe
from werkzeug.exceptions import NotFound


@jwt_required()
def delete_favorite_recipe(recipe_id):

    try:
        session: Session = db.session
        user_id = get_jwt_identity()["id"]
        data = {"user_id": user_id, "recipe_id": recipe_id}
        DeleteFromFavoritesRecipeSchema().load(data)

        recipe_to_delete = FavoriteRecipe.query.filter_by(user_id=user_id, recipe_id=recipe_id).first()
        
        if not recipe_to_delete:
            raise NotFound

        session.delete(recipe_to_delete)
        session.commit()

        return '', HTTPStatus.NO_CONTENT

    except NotFound:        
            return jsonify({"Error": "Recipe not in favorites"}), HTTPStatus.NOT_FOUND            

    except ValidationError as error:
        return jsonify({"Error": error.args}), HTTPStatus.BAD_REQUEST    
