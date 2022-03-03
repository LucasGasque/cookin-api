from http import HTTPStatus

from flask import current_app
from flask_jwt_extended import get_jwt_identity, jwt_required
from werkzeug.exceptions import NotFound

from app.models.auths_model import Auth
from app.models.recipes_model import Recipe
from app.models.user_private_recipes_model import UserPrivateRecipe


@jwt_required()
def delete_private_recipe(id: str):
    try:
        # pega pelo email do usuário dono do token a auth_id dele
        user_email = get_jwt_identity()
        user_token_id = Auth.query.filter_by(email=user_email["email"]).first()
        auth_id = user_token_id.id

        # ve se a id da receita existe
        filtered_recipe = Recipe.query.get_or_404(id)

        # pega o registro na tabela user_private_recipes
        owner_of_searched_recipe = UserPrivateRecipe.query.filter_by(
            recipe_id=id
        ).first()

        # checa se a id de usuário correspondente a id da receita bate com a auth_id do token
        if owner_of_searched_recipe.user_id == auth_id:
            current_app.db.session.delete(filtered_recipe)
            current_app.db.session.commit()
            return {}, HTTPStatus.NO_CONTENT

        else:
            return {
                "error": "you are not allowed to delete this recipe"
            }, HTTPStatus.BAD_REQUEST

    except NotFound:
        return {"msg": "recipe not found"}, HTTPStatus.NOT_FOUND