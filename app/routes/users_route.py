from flask import Blueprint

from app.controllers import user

bp_users = Blueprint("users", __name__, url_prefix="/users")

bp_users.get("")(user.get_users)
bp_users.get("/<string:user_id>")(user.get_user_by_id)