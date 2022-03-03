from http import HTTPStatus


class WrongKeySentError(Exception):
    def __init__(self, array_of_keys: list):
        self.message = {
            "error": "invalid keys are being sent",
            "valid_keys": f"{array_of_keys}",
        }, HTTPStatus.BAD_REQUEST

        super().__init__(self.message)
