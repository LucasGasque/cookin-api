from flask import Blueprint
from app.controllers.user_recipes import (
    create_private_recipe,
    get_private_recipes,
    get_private_recipe_by_id,
    delete_private_recipe,
    update_private_recipe,
    update_share,
)

bp_users_recipes = Blueprint("user_recipes", __name__, url_prefix="/users/recipes")

bp_users_recipes.post("")(create_private_recipe)
bp_users_recipes.get("")(get_private_recipes)
bp_users_recipes.get("/<string:recipe_id>")(get_private_recipe_by_id)
bp_users_recipes.delete("/<string:recipe_id>")(delete_private_recipe)
bp_users_recipes.patch("/<string:recipe_id>")(update_private_recipe)
bp_users_recipes.patch("/<string:recipe_id>/share")(update_share)
