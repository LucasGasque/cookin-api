from http import HTTPStatus

from flask import current_app, jsonify, request
from marshmallow import ValidationError
from sqlalchemy.exc import DataError, IntegrityError

from app.exc.missing_valid_keys_error import MissingValidKeysError
from app.exc.wrong_key_sent_error import WrongKeySentError
from app.models.auth_model import Auth
from app.models.users_model import User
from app.services.auth_services import check_keys, check_values_types
from app.schemas.auth_schema import AuthSchema


def register_user():

    try:
        data = request.get_json()
        new_user_auth_found = None
        check_keys(data.keys())
        check_values_types(data.values())

        name = data.pop("name", None).title()
        gender = data.pop("gender", None).title()
        profile_photo = data.pop("profile_photo", None)

        # new_user_auth_table = Auth(**data)
        new_user_auth_table = AuthSchema().load(data)

        current_app.db.session.add(new_user_auth_table)

        new_user_auth_found: Auth = Auth.query.filter_by(
            email=new_user_auth_table.email
        ).first()
        auth_id = new_user_auth_found.id

        new_user_part_users = User(
            name=name, gender=gender, profile_photo=profile_photo, auth_id=auth_id
        )

        current_app.db.session.add(new_user_part_users)
        current_app.db.session.commit()

        return "", HTTPStatus.CREATED

    except ValidationError as e:
        return {"Error": e.args}, HTTPStatus.BAD_REQUEST

    except AttributeError:
        return {"error": "all value types must be string"}, HTTPStatus.BAD_REQUEST

    except DataError:
        return {
            "error": "gender key only accepts values 'Masculino', 'Feminino' or 'Outro'"
        }, HTTPStatus.BAD_REQUEST

    except IntegrityError:
        return {"error": "e-mail already registered in database"}, HTTPStatus.CONFLICT

    except WrongKeySentError as e:
        return e.message

    except MissingValidKeysError as e:
        return e.message
