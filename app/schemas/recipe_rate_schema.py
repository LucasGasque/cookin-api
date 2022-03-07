from http import HTTPStatus
from http.client import BAD_REQUEST
from marshmallow import Schema, fields, post_load, pre_load

from app.models.recipes_rating_model import RecipesRating

class RecipeRateSchema(Schema):
    recipe_id = fields.UUID(required=True) 
    rating = fields.Integer(required=True)
    user_id = fields.UUID(required=True) 

    # @pre_load
    # def request_body_data(self, data, **kwargs):
    #     rating = data.get("rating")
    #     if type(rating) != int:
    #         return {"Error": f"Input value most be integer, it was {type(rating)}!"}, HTTPStatus.BAD_REQUEST
    #     return data

    # @post_load
    # def create_recipe_rate(self, data, **kwargs):
    #     return RecipesRating(**data)