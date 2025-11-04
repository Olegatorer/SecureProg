import uuid
import socket

SESSION_ID = str(uuid.uuid4())

def get_ip_address():
    try:
        hostname = socket.gethostname()
        return socket.gethostbyname(hostname)
    except Exception:
        return "127.0.0.1"

