from datetime import datetime as dt
from http import HTTPStatus
from uuid import UUID

from app.configs.database import db
from app.models.recipes_model import Recipe
from app.models.users_model import User
from flask import current_app, jsonify, request
from flask_jwt_extended import get_jwt_identity, jwt_required
from sqlalchemy.orm.session import Session
from werkzeug.exceptions import NotFound


@jwt_required()
def update_recipe(recipe_id):

    session: Session = current_app.db.session
    received_data = request.get_json()

    user_id = get_jwt_identity()

    try:
        user: User = User.query.filter_by(auth_id=user_id["id"]).first()
        recipe = [
            recipe for recipe in user.private_recipe if recipe.id == UUID(recipe_id)
        ]

        if not recipe:
            raise NotFound

        recipe_to_update: Recipe = Recipe.query.get(recipe_id)
        for key, value in received_data.items():
            setattr(recipe_to_update, key, value)

    except NotFound:
        return jsonify({"error": "Recipe not found"}), HTTPStatus.NOT_FOUND

    recipe_to_update.updated_at = dt.now()

    session.commit()

    return "", HTTPStatus.NO_CONTENT
