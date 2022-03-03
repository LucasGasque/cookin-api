from flask import Blueprint

from app.controllers.user import get_user_by_id, get_users

bp_users = Blueprint("users", __name__, url_prefix="/users")

bp_users.get("")(get_users)
bp_users.get("/<string:user_id>")(get_user_by_id)