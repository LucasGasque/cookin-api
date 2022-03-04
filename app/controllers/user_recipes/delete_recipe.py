from http import HTTPStatus

from flask import current_app
from flask_jwt_extended import get_jwt_identity, jwt_required
from werkzeug.exceptions import NotFound

from app.models.recipes_model import Recipe
from app.models.user_private_recipes_model import UserPrivateRecipe
from app.utils.is_uuid import is_uuid


@jwt_required()
def delete_recipe(recipe_id: str):

    if not is_uuid(recipe_id):
        return {"msg": f"id sent is not uuid"}, HTTPStatus.BAD_REQUEST

    try:
        user = get_jwt_identity()
        auth_id = user["id"]

        filtered_recipe = Recipe.query.get_or_404(recipe_id)

        owner_of_searched_recipe = UserPrivateRecipe.query.filter_by(
            recipe_id=recipe_id, user_id=auth_id
        ).one_or_none()

        if not owner_of_searched_recipe:
            return {
                "error": "you are not allowed to delete this recipe"
            }, HTTPStatus.BAD_REQUEST

        current_app.db.session.delete(filtered_recipe)
        current_app.db.session.commit()
        return {}, HTTPStatus.NO_CONTENT

    except NotFound:
        return {"msg": "recipe not found"}, HTTPStatus.NOT_FOUND
