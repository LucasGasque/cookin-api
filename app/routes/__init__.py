from flask import Flask, Blueprint

from app.routes.auth_route import bp_auth
from app.routes.users_route import bp_users
from app.routes.recipes_route import bp_recipes
from app.routes.recipes_favorite_route import bp_recipes_favorite
from app.routes.recipes_rating_route import bp_recipes_rating
from app.routes.users_recipes_route import bp_users_recipes
from app.routes.error_route import bp_error

bp_api = Blueprint("api", __name__, url_prefix="/api")

def init_app(app: Flask):

    # bps here
    bp_api.register_blueprint(bp_auth)
    bp_api.register_blueprint(bp_users)
    bp_api.register_blueprint(bp_recipes)
    bp_api.register_blueprint(bp_recipes_favorite)
    bp_api.register_blueprint(bp_recipes_rating)
    bp_api.register_blueprint(bp_users_recipes)
    bp_api.register_blueprint(bp_error)
    
    app.register_blueprint(bp_api)
