from http import HTTPStatus

from flask import current_app
from flask_jwt_extended import get_jwt_identity, jwt_required
from marshmallow import ValidationError
from werkzeug.exceptions import NotFound

from app.models.recipes_model import Recipe
from app.models.user_private_recipes_model import UserPrivateRecipe
from app.schemas.user_recipes import DeletePrivateRecipeSchema


@jwt_required()
def delete_private_recipe(recipe_id: str):
    try:
        user = get_jwt_identity()
        auth_id = user["id"]

        DeletePrivateRecipeSchema().load({"recipe_id": recipe_id, "auth_id": auth_id})

        filtered_recipe = Recipe.query.get_or_404(recipe_id)

        owner_of_searched_recipe = UserPrivateRecipe.query.filter_by(
            recipe_id=recipe_id, user_id=auth_id
        ).one_or_none()

        if not owner_of_searched_recipe:
            return {
                "Error": "You are not allowed to delete this recipe"
            }, HTTPStatus.BAD_REQUEST

        current_app.db.session.delete(filtered_recipe)
        current_app.db.session.commit()
        return "", HTTPStatus.NO_CONTENT

    except NotFound:
        return {"Error": "Recipe not found"}, HTTPStatus.NOT_FOUND

    except ValidationError as error:
        return {"Error": error.args}, HTTPStatus.BAD_REQUEST
