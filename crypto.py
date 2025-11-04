from cryptography.fernet import Fernet
import os

def generate_key():
    key = Fernet.generate_key()
    with open("secret.key", "wb") as f:
        f.write(key)

def load_key():
    return Fernet(open("secret.key", "rb").read())

def encrypt_file(filepath):
    fernet = load_key()
    with open(filepath, "rb") as file:
        encrypted = fernet.encrypt(file.read())
    with open(filepath + ".enc", "wb") as file:
        file.write(encrypted)

def decrypt_file(filepath):
    fernet = load_key()
    with open(filepath, "rb") as file:
        decrypted = fernet.decrypt(file.read())
    with open(filepath.replace(".enc", ".dec"), "wb") as file:
        file.write(decrypted)