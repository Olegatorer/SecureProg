import bcrypt
import getpass
import os

def hash_password(password: str) -> bytes:
    salt = bcrypt.gensalt()
    return bcrypt.hashpw(password.encode(), salt)

def verify_password(stored_hash: bytes) -> bool:
    password = getpass.getpass("Enter password: ")
    return bcrypt.checkpw(password.encode(), stored_hash)

def load_or_create_password():
    if os.path.exists("auth.hash"):
        with open("auth.hash", "rb") as f:
            return verify_password(f.read())
    else:
        password = getpass.getpass("Set new password: ")
        hashed = hash_password(password)
        with open("auth.hash", "wb") as f:
            f.write(hashed)
        return True