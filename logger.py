import logging
from datetime import datetime

logging.basicConfig(filename="secure.log", level=logging.INFO)

def log_event(event, user_id="anon", ip="127.0.0.1", outcome="success"):
    timestamp = datetime.utcnow().isoformat()
    logging.info(f"{timestamp} | {event} | {user_id} | {ip} | {outcome}")