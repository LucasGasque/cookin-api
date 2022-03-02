from flask import Blueprint

from app.controllers import auth

bp_auth = Blueprint("auth", __name__, url_prefix="/auth")

bp_auth.post("")(auth.register_user)
bp_auth.post("/login")(auth.login_user)
bp_auth.patch("")(auth.update_user)
bp_auth.delete("")(auth.delete_user)