from flask import Blueprint

from app.controllers.recipes_rating import register_recipes_rating, update_recipes_rating

bp_recipes_rating = Blueprint("bp_recipes_rating", __name__, url_prefix="/recipes")

bp_recipes_rating.post("/<int:recipe_id>/rating")(register_recipes_rating)

bp_recipes_rating.patch("/<int:recipe_id>/rating")(update_recipes_rating)