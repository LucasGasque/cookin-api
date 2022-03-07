from http import HTTPStatus

from flask import jsonify
from flask_jwt_extended import get_jwt_identity, jwt_required
from sqlalchemy.orm.session import Session

from app.configs.database import db
from app.models.favorite_recipes_model import FavoriteRecipe
from app.models.recipes_model import Recipe
from app.schemas.favorite_recipes import GetFavoriteRecipesSchema
from marshmallow import ValidationError


@jwt_required()
def get_favorite_recipes():
    try:
        session: Session = db.session
        user = get_jwt_identity()
        auth_id = user["id"]

        GetFavoriteRecipesSchema().load({"auth_id": auth_id})

        array_of_user_favorites = []

        recipes_list = session.query(FavoriteRecipe).filter_by(user_id=auth_id).all()

        for item in recipes_list:
            recipe_found_in_recipes = (
                session.query(Recipe).filter_by(id=item.recipe_id).first()
            )
            if recipe_found_in_recipes.public == True:
                array_of_user_favorites.append(recipe_found_in_recipes)

        return jsonify(array_of_user_favorites), HTTPStatus.OK
    
    except ValidationError as error:
        return {"Error": error.args}, HTTPStatus.BAD_REQUEST
