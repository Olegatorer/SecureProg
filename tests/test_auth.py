import bcrypt
from auth import hash_password

def test_password_hashing_and_verification(monkeypatch):
    password = "secure123"
    hashed = hash_password(password)
    assert bcrypt.checkpw(password.encode(), hashed)

    monkeypatch.setattr("getpass.getpass", lambda _: password)
    from auth import verify_password
    assert verify_password(hashed)