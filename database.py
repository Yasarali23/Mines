import json
import os
from datetime import datetime

USERS_FILE = "users.json"
LOG_FILE = "accuracy.json"

def load_json(file):
    if not os.path.exists(file):
        with open(file, "w") as f:
            json.dump({}, f)
    with open(file, "r") as f:
        return json.load(f)

def save_json(file, data):
    with open(file, "w") as f:
        json.dump(data, f, indent=2)

def is_vip(user_id):
    users = load_json(USERS_FILE)
    return str(user_id) in users.get("vip", [])

def is_banned(user_id):
    users = load_json(USERS_FILE)
    return str(user_id) in users.get("banned", [])

def add_vip(user_id):
    users = load_json(USERS_FILE)
    users.setdefault("vip", []).append(str(user_id))
    save_json(USERS_FILE, users)

def remove_vip(user_id):
    users = load_json(USERS_FILE)
    users.setdefault("vip", []).remove(str(user_id))
    save_json(USERS_FILE, users)

def ban_user(user_id):
    users = load_json(USERS_FILE)
    users.setdefault("banned", []).append(str(user_id))
    save_json(USERS_FILE, users)

def unban_user(user_id):
    users = load_json(USERS_FILE)
    users.setdefault("banned", []).remove(str(user_id))
    save_json(USERS_FILE, users)

def log_accuracy(user_id, username, accuracy):
    logs = load_json(LOG_FILE)
    logs.setdefault(str(user_id), []).append({
        "username": username,
        "accuracy": accuracy,
        "time": datetime.now().isoformat()
    })
    save_json(LOG_FILE, logs)
