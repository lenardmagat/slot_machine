import os
import json

BASE_DIR = os.path.join(os.getcwd(), "accounts_data")
FILE = {"accounts" : "account.json"}
def ensure_file(filepath, default):
    if not os.path.exists(filepath):
        with open(filepath, "w") as f:
            json.dump(default, f, indent=4)
    return filepath
def data_setup():
    paths = {}
    os.makedirs(BASE_DIR, exist_ok=True)
    for key, value in FILE.items():
        if key == "accounts":
            default = {}
        paths[key] = ensure_file(os.path.join(BASE_DIR, value), default)
    return paths

class account_data:
   def load_accounts(self):
        with open(data_setup()["accounts"], "r") as f:
            return json.load(f)