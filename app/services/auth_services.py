from app.exc.missing_valid_keys_error import MissingValidKeysError
from app.exc.wrong_key_sent_error import WrongKeySentError


def check_keys(keys):
    valid_keys = ["name", "email", "gender", "password", "profile_photo"]
    valid_keys_missing = []
    for key in keys:
        if key not in valid_keys:
            raise WrongKeySentError(
                {
                    "error": "invalid keys are being sent",
                    "valid_keys": f"{valid_keys}",
                }
            )

    for valid_key in valid_keys:
        if valid_key not in keys and valid_key != "profile_photo":
            valid_keys_missing.append(valid_key)

    if len(valid_keys_missing) != 0:
        raise MissingValidKeysError(
            {
                "error": "there are valid keys missing",
                "missing keys": f"{valid_keys_missing}",
                "valid_keys": f"{valid_keys}",
            }
        )
