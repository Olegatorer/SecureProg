import os

def secure_delete(filepath):
    if os.path.exists(filepath):
        with open(filepath, "ba+", buffering=0) as f:
            f.write(b"\x00" * os.path.getsize(filepath))
        os.remove(filepath)