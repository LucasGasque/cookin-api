from http import HTTPStatus

from flask import current_app
from flask_jwt_extended import get_jwt_identity, jwt_required
from werkzeug.exceptions import NotFound

from app.models.recipes_model import Recipe
from app.models.user_private_recipes_model import UserPrivateRecipe
from app.schemas.user_recipes import ShareRecipeSchema
from marshmallow import ValidationError

@jwt_required()
def update_share(recipe_id: str):
    try:
        ShareRecipeSchema().load({"recipe_id": recipe_id})
        user = get_jwt_identity()
        auth_id = user["id"]

        filtered_recipe = Recipe.query.get_or_404(recipe_id)

        owner_of_searched_recipe = UserPrivateRecipe.query.filter_by(
            recipe_id=recipe_id, user_id=auth_id
        ).one_or_none()

        if not owner_of_searched_recipe:
            return {
                "error": "you are not allowed to share/unshare this recipe"
            }, HTTPStatus.BAD_REQUEST
        
        new_state_of_sharing = not filtered_recipe.public
        filtered_recipe.public = new_state_of_sharing

        filtered_recipe.public = new_state_of_sharing

        current_app.db.session.add(filtered_recipe)
        current_app.db.session.commit()

        return "", HTTPStatus.NO_CONTENT

    except NotFound:
        return {"msg": "recipe not found"}, HTTPStatus.NOT_FOUND
    
    except ValidationError as error:
        return {"Error": error.args}, HTTPStatus.BAD_REQUEST
