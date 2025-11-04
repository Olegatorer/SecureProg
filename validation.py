import re

def validate_filename(filename):
    if not re.match(r'^[\w\-. ]+$', filename):
        raise ValueError("Invalid filename format.")
    return filename