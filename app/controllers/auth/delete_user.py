from http import HTTPStatus

from flask_jwt_extended import get_jwt_identity, jwt_required
from sqlalchemy.orm.session import Session

from app.models.auth_model import Auth
from app.configs.database import db


@jwt_required()
def delete_user():
    user_authorized = get_jwt_identity()
    session: Session = db.session()

    user_in_auth: Auth = Auth.query.filter_by(email=user_authorized["email"]).first()

    session.delete(user_in_auth)
    db.session.commit()

    return {}, HTTPStatus.NO_CONTENT
