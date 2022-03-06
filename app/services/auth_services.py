from app.exc.missing_valid_keys_error import MissingValidKeysError
from app.exc.wrong_key_sent_error import WrongKeySentError


def check_keys(keys):
    valid_keys = ["name", "email", "gender", "password", "profile_photo"]
    valid_keys_missing = []
    for key in keys:
        if key not in valid_keys:
            raise WrongKeySentError(valid_keys)

    for valid_key in valid_keys:
        if valid_key not in keys and valid_key != "profile_photo":
            valid_keys_missing.append(valid_key)

    if len(valid_keys_missing) != 0:
        raise MissingValidKeysError(valid_keys, valid_keys_missing)