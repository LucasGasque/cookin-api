from http import HTTPStatus

from app.configs.database import db
from app.schemas.favorite_recipes import AddToFavoriteRecipeSchema
from flask import jsonify
from flask_jwt_extended import get_jwt_identity, jwt_required
from marshmallow.exceptions import ValidationError
from psycopg2.errors import ForeignKeyViolation, UniqueViolation
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm.session import Session


@jwt_required()
def favorite_recipe(recipe_id):

    try:
        session: Session = db.session
        user_id = get_jwt_identity()["id"]

        data = {"user_id": user_id, "recipe_id": recipe_id}

        add_to_favorite = AddToFavoriteRecipeSchema().load(data)

        session.add(add_to_favorite)
        session.commit()

        return (
            jsonify({"message": "Recipe added to user favorite recipes"}),
            HTTPStatus.CREATED,
        )

    except IntegrityError as error:
        if isinstance(error.orig, UniqueViolation):
            return (
                jsonify({"Error": "Recipe already in favorites"}),
                HTTPStatus.CONFLICT,
            )
        elif isinstance(error.orig, ForeignKeyViolation):
            return (
                jsonify({"Error": "Recipe not found or invalid id."}),
                HTTPStatus.BAD_REQUEST,
            )

    except ValidationError as error:
        return jsonify({"Error": error.args}), HTTPStatus.BAD_REQUEST
