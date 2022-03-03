from http import HTTPStatus

from flask import current_app, jsonify

from app.models.recipes_model import Recipe

def get_recipes():
    base_query = current_app.db.session.query(Recipe)
    recipes = base_query.all()

    return jsonify(recipes), HTTPStatus.OK