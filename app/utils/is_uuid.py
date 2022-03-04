from uuid import UUID

def is_uuid(val):
    try:
        UUID(str(val))
        return True
    except ValueError:
        return False
