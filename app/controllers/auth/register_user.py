from http import HTTPStatus

from flask import current_app, request
from marshmallow import ValidationError
from sqlalchemy.exc import IntegrityError

from app.exc.missing_valid_keys_error import MissingValidKeysError
from app.exc.wrong_key_sent_error import WrongKeySentError
from app.models.auth_model import Auth
from app.schemas.auth_schema import AuthSchema
from app.schemas.user_schema import UserSchema
from app.services.auth_services import check_keys


def register_user():

    try:
        data = request.get_json()
        new_user_auth_found = None
        check_keys(data.keys())

        name = data.pop("name", None)
        gender = data.pop("gender", None)
        profile_photo = data.pop("profile_photo", None)

        new_user_auth_table = AuthSchema().load(data)

        current_app.db.session.add(new_user_auth_table)

        new_user_auth_found: Auth = Auth.query.filter_by(
            email=new_user_auth_table.email
        ).first()
        auth_id = new_user_auth_found.id

        new_user_part_users = UserSchema().load(
            {
                "name": name,
                "gender": gender,
                "profile_photo": profile_photo,
                "auth_id": auth_id,
            }
        )

        current_app.db.session.add(new_user_part_users)
        current_app.db.session.commit()

        return "", HTTPStatus.CREATED

    except ValidationError as e:
        return {"Error": e.args}, HTTPStatus.BAD_REQUEST

    except IntegrityError:
        return {"Error": "e-mail already registered in database"}, HTTPStatus.CONFLICT

    except WrongKeySentError as e:
        return {"Error:": e.args}, HTTPStatus.BAD_REQUEST

    except MissingValidKeysError as e:
        return {"Error": e.args}, HTTPStatus.BAD_REQUEST
