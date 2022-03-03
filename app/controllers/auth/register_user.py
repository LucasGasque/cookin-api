from http import HTTPStatus

from flask import current_app, jsonify, request
from sqlalchemy.exc import DataError, IntegrityError

from app.exc.missing_valid_keys_error import MissingValidKeysError
from app.exc.wrong_key_sent_error import WrongKeySentError
from app.models.auths_model import Auth
from app.models.users_model import User
from app.services.auth_services import check_keys, check_values_types


def register_user():

    try:
        data = request.get_json()
        new_user_auth_found = None
        check_keys(data.keys())
        check_values_types(data.values())

        name = data.pop("name", None).title()
        gender = data.pop("gender", None).title()
        profile_photo = data.pop("profile_photo", None)

        new_user_auth_table = Auth(**data)

        current_app.db.session.add(new_user_auth_table)
        current_app.db.session.commit()

        new_user_auth_found: Auth = Auth.query.filter_by(
            email=new_user_auth_table.email
        ).first()
        auth_id = new_user_auth_found.id

        new_user_part_users = User(
            name=name, gender=gender, profile_photo=profile_photo, auth_id=auth_id
        )

        current_app.db.session.add(new_user_part_users)
        current_app.db.session.commit()

        return_dict = {
            "name": new_user_part_users.name,
            "email": new_user_part_users.auth.email,
            "gender": new_user_part_users.gender,
            "profile_photo": new_user_part_users.profile_photo,
        }

        return jsonify(return_dict), HTTPStatus.CREATED

    except AttributeError:
        if new_user_auth_found != None:
            current_app.db.session.delete(new_user_auth_found)
            current_app.db.session.commit()
        return {"error": "all value types must be string"}

    except DataError:
        current_app.db.session.rollback()
        if new_user_auth_found != None:
            current_app.db.session.delete(new_user_auth_found)
            current_app.db.session.commit()
        return {
            "error": "gender key only accepts values 'Masculino', 'Feminino' or 'Outro'"
        }

    except IntegrityError:
        return {"error": "e-mail already registered in database"}

    except WrongKeySentError as e:
        if new_user_auth_found != None:
            current_app.db.session.delete(new_user_auth_found)
            current_app.db.session.commit()
        return e.message

    except MissingValidKeysError as e:
        if new_user_auth_found != None:
            current_app.db.session.delete(new_user_auth_found)
            current_app.db.session.commit()
        return e.message