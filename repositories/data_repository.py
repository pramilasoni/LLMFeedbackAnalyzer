import json
import os

DATA_FILE = "data.json"


def initialize_file():
    if not os.path.exists(DATA_FILE):
        with open(DATA_FILE, "w") as f:
            json.dump([], f)


def save_record(record: dict):
    initialize_file()

    with open(DATA_FILE, "r") as f:
        existing = json.load(f)

    existing.append(record)

    with open(DATA_FILE, "w") as f:
        json.dump(existing, f, indent=2)


def get_all_records():
    initialize_file()

    with open(DATA_FILE, "r") as f:
        return json.load(f)