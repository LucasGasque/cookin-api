from http import HTTPStatus

from flask_jwt_extended import get_jwt_identity, jwt_required
from marshmallow import ValidationError
from sqlalchemy.orm import Session
from app.configs.database import db

from sqlalchemy.orm.exc import NoResultFound

from app.models.recipes_rating_model import RecipesRating
from app.schemas.recipes_rating.delete_recipes_rating_schema import (
    RatingRecipeDeleteSchema,
)


@jwt_required()
def delete_recipes_rating(recipe_id: str):

    try:
        user_authorized = get_jwt_identity()
        auth_id = user_authorized["id"]

        RatingRecipeDeleteSchema().load({"recipe_id": recipe_id, "auth_id": auth_id})

        recipe_rate_to_be_deleted: RecipesRating = RecipesRating.query.filter_by(
            recipe_id=recipe_id, user_id=auth_id
        ).one_or_none()

        if not recipe_rate_to_be_deleted:
            raise NoResultFound

        session: Session = db.session

        session.delete(recipe_rate_to_be_deleted)
        session.commit()

        return "", HTTPStatus.NO_CONTENT

    except ValidationError as error:
        return {"Error": error.args}, HTTPStatus.BAD_REQUEST

    except NoResultFound:
        return {"Error": "User cannot delete this rating"}, HTTPStatus.NOT_FOUND
