from http import HTTPStatus
from flask import jsonify
from flask_jwt_extended import get_jwt_identity, jwt_required
from app.models.user_private_recipes_model import UserPrivateRecipe

def get_private_recipes():
    
    user = get_jwt_identity()
    recipes = UserPrivateRecipe.query.filter_by(user_id = user["id"]).all()

    if not user["id"]:
        return jsonify({"error": "user not found"}), HTTPStatus.NOT_FOUND

    return jsonify(recipes), HTTPStatus.OK

