from http import HTTPStatus


class MissingValidKeysError(Exception):
    def __init__(self, array_of_valid_keys: list, array_of_missing_keys: list):
        self.message = {
            "error": "there are valid keys missing",
            "missing keys": f"{array_of_missing_keys}",
            "valid_keys": f"{array_of_valid_keys}",
        }, HTTPStatus.BAD_REQUEST

        super().__init__(self.message)
