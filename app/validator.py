import re

def validate_record(record):

    if record["age"] < 18 or record["age"] > 60:
        return False

    if not record["email"].endswith("@gmail.com"):
        return False

    return True