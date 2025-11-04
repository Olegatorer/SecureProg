# 🔐 Secure File Encryption and Management System

A command-line tool for securely encrypting, decrypting, and deleting files with password-based access control, input validation, and structured logging. Built for ICS0022 Secure Programming (2025 Autumn).

---

## 📦 Features

- **File Encryption & Decryption**  
  Uses AES-128 encryption via `cryptography.Fernet`. Encrypted files are saved as `.enc`, and decrypted files as `.dec`.

- **Secure File Deletion**  
  Overwrites file contents before removal to prevent recovery.

- **Password-Based Authentication**  
  First-time setup prompts for password creation. Passwords are hashed with `bcrypt` and stored securely.

- **Input Validation**  
  Filenames are validated using regex to prevent injection and unsafe characters.

- **Structured Logging**  
  Logs include timestamp, session ID, IP address, event type, and outcome. No secrets or passwords are ever logged.

---

## 🚀 Usage

```bash
python secure_tool.py encrypt <filename>
python secure_tool.py decrypt <filename>.enc
python secure_tool.py delete <filename>
```
- First run: prompts to set a password
- Subsequent runs: requires password to proceed
- Encrypted files: <filename>.enc
- Decrypted files: <filename>.dec





