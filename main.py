import argparse
import os

from auth import load_or_create_password
from crypto import encrypt_file, decrypt_file, generate_key
from file_ops import secure_delete
from validation import validate_filename
from logger import log_event

def main():
    parser = argparse.ArgumentParser(description="Secure File Encryption Tool")
    parser.add_argument("action", choices=["encrypt", "decrypt", "delete"], help="Action to perform")
    parser.add_argument("filepath", help="Path to the file")
    args = parser.parse_args()

    if not load_or_create_password():
        print("Authentication failed.")
        return

    try:
        filename = validate_filename(args.filepath)
        if not os.path.exists("secret.key"):
            generate_key()

        if args.action == "encrypt":
            encrypt_file(filename)
            log_event("encrypt", outcome="success")
        elif args.action == "decrypt":
            decrypt_file(filename)
            log_event("decrypt", outcome="success")
        elif args.action == "delete":
            secure_delete(filename)
            log_event("delete", outcome="success")

        print(f"{args.action.capitalize()} operation completed.")
    except Exception as e:
        log_event(args.action, outcome="error")
        print("An error occurred")

if __name__ == "__main__":
    main()