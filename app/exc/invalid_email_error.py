from werkzeug.exceptions import BadRequest

class InvalidEmailError(BadRequest):
    ...