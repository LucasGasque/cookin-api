from flask import Blueprint

from app.controllers.recipes import get_public_recipes

bp_recipes = Blueprint("bp_recipes", __name__, url_prefix="/recipes")

bp_recipes.get("")(get_public_recipes)