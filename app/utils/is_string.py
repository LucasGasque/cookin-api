from app.exc.wrong_key_sent_error import WrongKeySentError


def is_string(val):
    if type(val) is not str:
        raise WrongKeySentError