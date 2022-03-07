
from http import HTTPStatus

from flask import current_app
from flask_jwt_extended import get_jwt_identity, jwt_required
from marshmallow import ValidationError
from sqlalchemy.exc import DataError

from app.models.recipes_model import Recipe
from app.models.recipes_rating_model import RecipesRating
from app.models.user_private_recipes_model import UserPrivateRecipe
from app.schemas.recipes_rating.delete_recipes_rating_schema import \
    RatingRecipeDeleteSchema


@jwt_required
def delete_recipes_rating(recipe_id: str):

    try:

        user_authorized = get_jwt_identity()
        auth_id = user_authorized["id"]

        Recipe.query.get_or_404(recipe_id)

        owner_of_searched_recipe = UserPrivateRecipe.query.filter_by(
                recipe_id=recipe_id, user_id=auth_id
            ).one_or_none()

        if owner_of_searched_recipe:
                return {
                    "Error": "you are not allowed to delete this recipe rate"
                }, HTTPStatus.BAD_REQUEST

        RatingRecipeDeleteSchema().load({"recipe_id": recipe_id, "auth_id": auth_id})

        recipe_rate_to_be_deleted: RecipesRating = RecipesRating.query.filter_by(
                recipe_id=recipe_id, user_id=auth_id
            ).one_or_none()

        current_app.db.session.delete(recipe_rate_to_be_deleted)
        current_app.db.session.commit()

        return "", HTTPStatus.NO_CONTENT

    except ValidationError as error:
        return {"Error": error.args}, HTTPStatus.BAD_REQUEST

    except DataError:
        return {"Error": "recipe not found"}, HTTPStatus.NOT_FOUND