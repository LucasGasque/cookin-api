from http import HTTPStatus
from flask import jsonify, request
from flask_jwt_extended import get_jwt_identity, jwt_required

from app.models.user_private_recipes_model import UserPrivateRecipe
from app.schemas.recipes import GetPublicRecipesSchema


@jwt_required()
def get_private_recipes():
    try:
        page = request.args.get("page", 1, type=int)
        per_page = request.args.get("per_page", 10, type=int)

        category = request.args.get("category", None, type=str)
        preparation_time = request.args.get("preparation_time", None, type=int)
        difficulty = request.args.get("category", None, type=str)
        portion_size = request.args.get("portion_size", None, type=int)

        user = get_jwt_identity()
        recipes = UserPrivateRecipe.query.filter_by(user_id=user["id"]).all()

        if not user["id"]:
            return jsonify({"error": "user not found"}), HTTPStatus.NOT_FOUND

        return jsonify(recipes), HTTPStatus.OK

    except:
        return {"Error"}
