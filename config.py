import yaml
import os

CONFIG_FILE = "config.yaml"
EXAMPLE_CONFIG_FILE = "config.example.yaml"

def load_config():
    if not os.path.exists(CONFIG_FILE):
        print(f"Config file '{CONFIG_FILE}' not found! Using example config.")
        CONFIG_FILE_PATH = EXAMPLE_CONFIG_FILE
    else:
        CONFIG_FILE_PATH = CONFIG_FILE

    with open(CONFIG_FILE_PATH, "r") as file:
        return yaml.safe_load(file)

config = load_config()

IMAP_SERVER = config.get("IMAP_SERVER", "outlook.office365.com")
EMAIL = config.get("EMAIL", "your_email@example.com")
PASSWORD = config.get("PASSWORD", "")
MAILBOX = config.get("MAILBOX", "inbox")
