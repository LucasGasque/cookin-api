import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def init_app(app: Flask):
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DB_URI')
    app.config['JSON_SORT_KEYS'] = False

    db.init_app(app)
    app.db = db

    
    # imports here
    
    from app.models.recipes_model import Recipe
    from app.models.users_model import User
    from app.models.auths_model import Auth
    from app.models.user_private_recipes_model import UserPrivateRecipe
    from app.models.favorite_recipes_model import FavoriteRecipe
    from app.models.recipes_rating_model import RecipesRating

