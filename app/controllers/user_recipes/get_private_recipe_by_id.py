from http import HTTPStatus

from flask import jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity

from sqlalchemy.orm.exc import NoResultFound

from app.models.recipes_model import Recipe
from app.schemas.user_recipes.get_private_recipe_by_id_schema import GetPrivateRecipeByIdSchema


@jwt_required
def get_private_recipe_by_id(recipe_id: str):
    try:
        user = get_jwt_identity()
        auth_id = user["id"]

        GetPrivateRecipeByIdSchema().load({"auth_id": auth_id, "recipe_id": recipe_id })

        recipe = Recipe.query.filter_by(id=recipe_id).one_or_none()

        if not recipe:
            raise NoResultFound

        return jsonify(recipe), HTTPStatus.OK

    except NoResultFound:
        return jsonify({"Error": "recipe id not found"}), HTTPStatus.NOT_FOUND