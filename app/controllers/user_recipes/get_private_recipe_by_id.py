from http import HTTPStatus

from flask import jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity

from sqlalchemy.orm.exc import NoResultFound
from marshmallow.exceptions import ValidationError

from app.models.recipes_model import Recipe
from app.schemas.user_recipes.get_private_recipe_by_id_schema import (
    GetPrivateRecipeByIdSchema,
)
from app.models.user_private_recipes_model import UserPrivateRecipe


@jwt_required()
def get_private_recipe_by_id(recipe_id: str):
    try:
        user = get_jwt_identity()
        auth_id = user["id"]
        GetPrivateRecipeByIdSchema().load({"auth_id": auth_id, "recipe_id": recipe_id})

        private_recipe: UserPrivateRecipe = UserPrivateRecipe.query.filter_by(
            recipe_id=recipe_id, user_id=auth_id
        ).first()
        if not private_recipe:
            raise NoResultFound

        recipe = Recipe.query.filter_by(id=recipe_id).first()

        return jsonify(recipe), HTTPStatus.OK

    except NoResultFound:
        return jsonify({"Error": "recipe not found"}), HTTPStatus.NOT_FOUND

    except ValidationError as error:
        return jsonify({"Error": error.args}), HTTPStatus.BAD_REQUEST
