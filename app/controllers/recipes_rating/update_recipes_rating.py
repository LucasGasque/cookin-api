from http import HTTPStatus
from pytest import Session
from sqlalchemy.exc import DataError
from sqlalchemy.orm import Session
from app.configs.database import db

from flask import request
from flask_jwt_extended import get_jwt_identity, jwt_required
from marshmallow import ValidationError

from app.models.user_private_recipes_model import UserPrivateRecipe
from app.schemas.recipes_rating.create_recipe_rating_schema import RecipeRateSchema
from app.models.recipes_rating_model import RecipesRating


@jwt_required()
def update_recipes_rating(recipe_id):

    try:
        user_authorized = get_jwt_identity()
        auth_id = user_authorized["id"]

        data = request.get_json()

        data["user_id"] = auth_id
        data["recipe_id"] = recipe_id

        RecipeRateSchema().load(data)

        owner_of_searched_recipe = UserPrivateRecipe.query.filter_by(
            recipe_id=recipe_id, user_id=auth_id
        ).one_or_none()

        if owner_of_searched_recipe:
            return {
                "Error": "you are not allowed to rate your own recipe"
            }, HTTPStatus.UNAUTHORIZED

        rating = RecipesRating.query.filter_by(user_id=auth_id, recipe_id=recipe_id).one_or_none()

        if not rating:
            return {"Error":"this recipe is not rated yet"}, HTTPStatus.BAD_REQUEST

        setattr(rating, "rating", data.get('rating'))

        session: Session = db.session
        session.add(rating)
        session.commit()

        return "", HTTPStatus.NO_CONTENT

    except DataError:
        return {"Error": "recipe not found"}, HTTPStatus.NOT_FOUND

    except ValidationError as e:
        return {"Error": e.args}, HTTPStatus.BAD_REQUEST