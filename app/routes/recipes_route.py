from flask import Blueprint

from app.controllers.recipes import get_recipes, get_recipes_by_category

bp_recipes = Blueprint("bp_recipes", __name__, url_prefix="/recipes")

bp_recipes.get("")(get_recipes)

bp_recipes.get("/<string:category>")(get_recipes_by_category)