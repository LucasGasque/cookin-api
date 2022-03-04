from http import HTTPStatus
from flask import jsonify
from flask_jwt_extended import jwt_required
from app.models.recipes_model import Recipe

@jwt_required
def get_recipe_by_id(recipe_id: str):
    try:
        recipe = Recipe.query.filter_by(id=recipe_id).one_or_none()
        return jsonify(recipe), HTTPStatus.OK
    except:
        return jsonify({"error": "recipe not found"}), HTTPStatus.NOT_FOUND