from http import HTTPStatus

from flask import jsonify
from flask_jwt_extended import get_jwt_identity, jwt_required
from marshmallow import ValidationError
from sqlalchemy.orm.session import Session

from app.configs.database import db
from app.models.favorite_recipes_model import FavoriteRecipe
from app.models.recipes_model import Recipe
from app.schemas.favorite_recipes import GetFavoriteRecipesSchema


@jwt_required()
def get_favorite_recipes():
    try:
        session: Session = db.session
        user = get_jwt_identity()
        auth_id = user["id"]

        GetFavoriteRecipesSchema().load({"auth_id": auth_id})

        recipes_list = session.query(FavoriteRecipe).filter_by(user_id=auth_id).all()

        recipes_ids_list = [item.recipe_id for item in recipes_list]

        favorites_list = (
            session.query(Recipe).filter(Recipe.id.in_(recipes_ids_list)).all()
        )

        favorites_public_list = [item for item in favorites_list if item.public == True]

        return jsonify(favorites_public_list), HTTPStatus.OK

    except ValidationError as error:
        return {"Error": error.args}, HTTPStatus.BAD_REQUEST
