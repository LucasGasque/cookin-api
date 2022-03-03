from http import HTTPStatus

from flask import jsonify
from sqlalchemy.orm.session import Session

from app.configs.database import db
from app.models.users_model import User


def get_users():

    session: Session = db.session
    user = session.query(User).all()

    if len(user) == 0:
        return {"msg": "No users found"}, HTTPStatus.NOT_FOUND

    return jsonify({"Users": user}), HTTPStatus.OK