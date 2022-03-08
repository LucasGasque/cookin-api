from http import HTTPStatus
from flask import jsonify, request
from sqlalchemy import and_

from marshmallow import ValidationError
from sqlalchemy.orm.exc import NoResultFound

from app.models.recipes_model import Recipe
from app.schemas.recipes import GetPublicRecipesSchema


def get_public_recipes():
    try:
        page = request.args.get("page", 1, type=int)
        per_page = request.args.get("per_page", 10, type=int)

        category = request.args.get("category", None, type=str)
        preparation_time = request.args.get("preparation_time", None, type=int)
        difficulty = request.args.get("difficulty", None, type=str)
        portion_size = request.args.get("portion_size", None, type=int)

        data = {}

        data["page"] = page
        data["per_page"] = per_page
        data["category"] = category
        data["preparation_time"] = preparation_time
        data["difficulty"] = difficulty
        data["portion_size"] = portion_size

        GetPublicRecipesSchema().load(data)
        not_null_filters = [Recipe.public is True]

        if category:
            not_null_filters.append(Recipe.category is category)

        if preparation_time:
            not_null_filters.append(Recipe.preparation_time <= preparation_time)

        if difficulty:
            not_null_filters.append(Recipe.difficulty is difficulty)

        if portion_size:
            not_null_filters.append(Recipe.portion_size <= portion_size)

        if len(not_null_filters) > 0:
            recipes = Recipe.query.filter(and_(*not_null_filters)).paginate(page, per_page)

        recipes = Recipe.query.filter(Recipe.public == True).paginate(page, per_page)

        if not recipes:
            raise NoResultFound
       
        return jsonify(recipes.items), HTTPStatus.OK

    except ValidationError as error:
        return {"Error": error.args}, HTTPStatus.BAD_REQUEST

    except NoResultFound:
        return {"Error": "No recipes found"}, HTTPStatus.NOT_FOUND
