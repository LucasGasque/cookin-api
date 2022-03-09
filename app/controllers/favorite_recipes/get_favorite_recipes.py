from http import HTTPStatus

from flask import jsonify
from flask_jwt_extended import get_jwt_identity, jwt_required
from marshmallow import ValidationError
from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy.orm.session import Session

from app.configs.database import db
from app.models.favorite_recipes_model import FavoriteRecipe
from app.models.recipes_model import Recipe
from app.models.user_private_recipes_model import UserPrivateRecipe
from app.schemas.favorite_recipes import GetFavoriteRecipesSchema


@jwt_required()
def get_favorite_recipes():
    try:
        user = get_jwt_identity()
        auth_id = user["id"]

        GetFavoriteRecipesSchema().load({"auth_id": auth_id})

        session: Session = db.session
        recipes_list = session.query(FavoriteRecipe).filter_by(user_id=auth_id).all()

        recipes_ids_list = [item.recipe_id for item in recipes_list]

        user_id_and_recipe_list = (
            session.query(UserPrivateRecipe)
            .filter(UserPrivateRecipe.recipe_id.in_(recipes_ids_list))
            .all()
        )

        recipes_ids_owned_by_logged_user = [
            item.recipe_id
            for item in user_id_and_recipe_list
            if str(item.user_id) == auth_id
        ]

        favorite_recipes_list = (
            session.query(Recipe).filter(Recipe.id.in_(recipes_ids_list)).all()
        )

        favorite_recipes_and_public_list = [
            item
            for item in favorite_recipes_list
            if item.public == True or item.id in recipes_ids_owned_by_logged_user
        ]

        if not favorite_recipes_and_public_list:
            raise NoResultFound

        return jsonify(favorite_recipes_and_public_list), HTTPStatus.OK

    except ValidationError as error:
        return {"Error": error.args}, HTTPStatus.BAD_REQUEST
    except NoResultFound:
        return {"Error": "No favorite recipes found"}, HTTPStatus.NOT_FOUND
