from http import HTTPStatus
from flask import request, current_app
from app.exc.user_cannot_rate_recipe import UserCannotRateOwnRecipeError


from app.exc.wrong_key_sent_error import WrongKeySentError
from app.models.recipes_model import Recipe
from app.models.user_private_recipes_model import UserPrivateRecipe
from app.utils.is_uuid import is_uuid
from flask_jwt_extended import get_jwt_identity, jwt_required

@jwt_required()
def register_recipes_rating(recipe_id: str):

    # fields.ID

    try:
        # is_uuid(recipe_id)  

        user_authorized = get_jwt_identity().auth_id

        data = request.get_json()

        data["user_id"] = user_authorized
        data["recipe_id"] = recipe_id

        # new_user_auth_table = AuthSchema().load(data)
        return '', HTTPStatus.NO_CONTENT

    except:
        ...