from app.exc.wrong_key_sent_error import WrongKeySentError


def is_int(val):
    if type(val) is not int:
        raise WrongKeySentError