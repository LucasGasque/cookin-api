from http import HTTPStatus

from flask import jsonify, request

from sqlalchemy.exc import DataError

from app.models.recipes_model import Recipe

def get_recipes():
    try:
        recipes = Recipe.query.all()

        category = request.args.get("category", None, type=str)
        preparation_time = request.args.get("preparation_time", None, type=str)
        difficulty = request.args.get("difficulty", None, type=str)
        portion_size = request.args.get("portion_size", None, type=str)

        if category:
            recipes = Recipe.query.filter_by(category=category).all()

        if preparation_time:
            recipes = Recipe.query.filter_by(preparation_time=preparation_time).all()

        if difficulty:
            recipes = Recipe.query.filter_by(difficulty=difficulty).all()

        if portion_size:
            recipes = Recipe.query.filter_by(portion_size=portion_size).all()

        return jsonify(recipes), HTTPStatus.OK

    except DataError as e:
        return jsonify(dict(error=' '.join(e.orig.pgerror.split()[:8]))), HTTPStatus.BAD_REQUEST