class InvalidUuidError(Exception):
     def __init__(self, array_of_keys: list):
        self.message = {
            "Error": "Invalid uuid"
        }

        super().__init__(self.message)