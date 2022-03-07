from http import HTTPStatus

from flask import current_app, request
from flask_jwt_extended import get_jwt_identity, jwt_required
from werkzeug.exceptions import NotFound

from app.models.recipes_model import Recipe
from app.models.user_private_recipes_model import UserPrivateRecipe
from app.schemas.recipe_rate_schema import RecipeRateSchema
from app.utils.is_uuid import is_uuid


@jwt_required()
def register_recipes_rating(recipe_id: str):

    if not is_uuid(recipe_id):
        return {"Error": f"id:{recipe_id} sent is not uuid"}, HTTPStatus.BAD_REQUEST

    try:

        user_authorized = get_jwt_identity()
        auth_id = user_authorized["id"]

        Recipe.query.get_or_404(recipe_id)

        owner_of_searched_recipe = UserPrivateRecipe.query.filter_by(
            recipe_id=recipe_id, user_id=auth_id
        ).one_or_none()

        if owner_of_searched_recipe:
            return {
                "Error": "you are not allowed to rate your own recipe"
            }, HTTPStatus.BAD_REQUEST

        data = request.get_json()

        data["user_id"] = user_authorized
        data["recipe_id"] = recipe_id

        recipe_rated = RecipeRateSchema().load(data)

        current_app.db.session.add(recipe_rated)
        current_app.db.session.commit()

        return "", HTTPStatus.NO_CONTENT

    except NotFound:
        return {"Error": "recipe not found"}, HTTPStatus.NOT_FOUND