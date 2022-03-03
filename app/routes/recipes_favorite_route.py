from flask import Blueprint

from app.controllers.favorite_recipes import favorite_recipe, get_favorite_recipe, delete_favorite_recipe

bp_recipes_favorite = Blueprint("bp_recipes_favorite", __name__, url_prefix="/recipes")

bp_recipes_favorite.post("/<string:recipe_id>/favorites")(favorite_recipe)
bp_recipes_favorite.get("/<string:recipe_id>/favorites")(get_favorite_recipe)
bp_recipes_favorite.delete("/<string:recipe_id>/favorites")(delete_favorite_recipe)
