from flask import Blueprint

from app.controllers import favorite_recipes

bp_recipes_favorite = Blueprint("bp_recipes_favorite", __name__, url_prefix="/recipes")

bp_recipes_favorite.post("/<string:recipe_id>/favorites")(favorite_recipes.favorite_recipe)

bp_recipes_favorite.get("/<string:recipe_id>/favorites")(favorite_recipes.get_favorite_recipe)

bp_recipes_favorite.delete("/<string:recipe_id>/favorites")(favorite_recipes.delete_favorite_recipe)
