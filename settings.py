import os

# Directory structure settings
BASE_DIR = os.getcwd()
DATA_DIR = os.path.join(BASE_DIR, "data")

ID_DIR = os.path.join(DATA_DIR, "ids")
SQL_DIR = os.path.join(DATA_DIR, "sqlite")
JSON_DIR = os.path.join(DATA_DIR, "json")
NETWORK_DIR = os.path.join(DATA_DIR, "networks")
