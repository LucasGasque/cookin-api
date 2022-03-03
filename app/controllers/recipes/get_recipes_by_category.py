from http import HTTPStatus

from flask import current_app, jsonify

from werkzeug.exceptions import NotFound

from app.models.recipes_model import Recipe

def get_recipes_by_category(category):
    try:
        base_query = current_app.db.session.query(Recipe)
        recipes = base_query.filter_by(category=category).all()

        if not recipes:
            raise NotFound

        return jsonify(recipes), HTTPStatus.OK
    
    except NotFound:
        return dict(error="Category not found!"), HTTPStatus.NOT_FOUND