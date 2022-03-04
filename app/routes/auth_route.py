from flask import Blueprint

from app.controllers.auth import register_user, login_user, update_user, delete_user

bp_auth = Blueprint("auth", __name__, url_prefix="/auth")

bp_auth.post("")(register_user)
bp_auth.post("/login")(login_user)
bp_auth.patch("")(update_user)
bp_auth.delete("")(delete_user)