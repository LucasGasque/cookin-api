from flask import Blueprint
from app.controllers.user_recipes import create_recipe, get_recipes, get_recipe_by_id, delete_recipe, update_recipe, share_recipe

bp_users_recipes = Blueprint("user_recipes", __name__, url_prefix="/users/recipes")

bp_users_recipes.post("")(create_recipe)
bp_users_recipes.get("")(get_recipes)
bp_users_recipes.get("/<string:recipe_id>")(get_recipe_by_id)
bp_users_recipes.delete("/<string:recipe_id>")(delete_recipe)
bp_users_recipes.patch("/<string:recipe_id>")(update_recipe)
bp_users_recipes.patch("/<string:recipe_id>/share")(share_recipe)