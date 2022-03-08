from http import HTTPStatus
from flask import jsonify, request
from flask_jwt_extended import get_jwt_identity, jwt_required
from sqlalchemy.orm import Session
from sqlalchemy import and_
from sqlalchemy.orm.exc import NoResultFound
from marshmallow import ValidationError

from app.models.user_private_recipes_model import UserPrivateRecipe
from app.models.recipes_model import Recipe
from app.schemas.user_recipes import GetPrivateRecipesSchema
from app.configs.database import db


@jwt_required()
def get_private_recipes():
    try:
        page = request.args.get("page", 1, type=int)
        per_page = request.args.get("per_page", 10, type=int)

        title = request.args.get("title", None, type=str)
        category = request.args.get("category", None, type=str)
        preparation_time = request.args.get("preparation_time", None, type=int)
        difficulty = request.args.get("category", None, type=str)
        portion_size = request.args.get("portion_size", None, type=int)

        user = get_jwt_identity()
        auth_id = user["id"]

        data = {}

        data["page"] = page
        data["per_page"] = per_page
        data["title"] = title
        data["category"] = category
        data["preparation_time"] = preparation_time
        data["difficulty"] = difficulty
        data["portion_size"] = portion_size
        data["auth_id"] = auth_id

        GetPrivateRecipesSchema().load(data)
        not_null_filters = []

        if title:
            not_null_filters.append(Recipe.title == title)

        if category:
            not_null_filters.append(Recipe.category == category.title())

        if preparation_time:
            not_null_filters.append(Recipe.preparation_time <= preparation_time)

        if difficulty:
            not_null_filters.append(Recipe.difficulty == difficulty.title())

        if portion_size:
            not_null_filters.append(Recipe.portion_size <= portion_size)

        session: Session = db.session

        recipes = (
            session.query(UserPrivateRecipe, Recipe)
            .filter(UserPrivateRecipe.user_id == auth_id)
            .filter(and_(*not_null_filters))
            .limit(per_page)
            .offset(page)
            .all()
        )

        if not recipes:
            raise NoResultFound

        print(recipes)

        return jsonify([recipe.Recipe for recipe in recipes]), HTTPStatus.OK

    except ValidationError as error:
        return {"Error": error.args}, HTTPStatus.BAD_REQUEST

    except NoResultFound:
        return {"Error": "No recipes found"}, HTTPStatus.NOT_FOUND
