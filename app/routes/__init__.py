from flask import Flask, Blueprint

from app.routes.recipes_blueprint import bp_recipes

bp_api = Blueprint("api", __name__, url_prefix="/api")

def init_app(app: Flask):
    # bps here

    app.register_blueprint(bp_api)
    
    bp_api.register_blueprint(bp_recipes)
