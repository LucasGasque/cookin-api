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
    
    from app.models.recipes_model import RecipesModel
    
    from app.models.auths_model import Auth
