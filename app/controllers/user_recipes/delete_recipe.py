from http import HTTPStatus

from flask import current_app
from flask_jwt_extended import get_jwt_identity, jwt_required
from sqlalchemy.exc import DataError
from werkzeug.exceptions import NotFound

from app.models.recipes_model import Recipe
from app.models.user_private_recipes_model import UserPrivateRecipe


@jwt_required()
def delete_recipe(recipe_id: str):
    try:
        user = get_jwt_identity()
        auth_id = user["id"]

        filtered_recipe = Recipe.query.get_or_404(recipe_id)

        owner_of_searched_recipe = UserPrivateRecipe.query.filter_by(
            recipe_id=recipe_id, user_id=auth_id
        ).one_or_none()

        if owner_of_searched_recipe:
            current_app.db.session.delete(filtered_recipe)
            current_app.db.session.commit()
            return {}, HTTPStatus.NO_CONTENT

        else:
            return {
                "error": "you are not allowed to delete this recipe"
            }, HTTPStatus.NOT_FOUND

    except NotFound:
        return {"msg": "recipe not found"}, HTTPStatus.NOT_FOUND
    except DataError:
        return {"msg": f"id sent is not uuid"}, HTTPStatus.BAD_REQUEST