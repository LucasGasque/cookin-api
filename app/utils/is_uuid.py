from uuid import UUID
from app.exc.invalid_uuid_error import InvalidUuidError

def is_uuid(val):
    try:
        UUID(str(val))
        return True
    except ValueError:
        raise InvalidUuidError
