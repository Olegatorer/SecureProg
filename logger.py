import logging
from datetime import datetime
from session import SESSION_ID, get_ip_address

logging.basicConfig(filename="secure.log", level=logging.INFO)

def log_event(event, outcome="success"):
    timestamp = datetime.now().isoformat()
    ip = get_ip_address()
    logging.info(f"{timestamp} | {event} | {SESSION_ID} | {ip} | {outcome}")