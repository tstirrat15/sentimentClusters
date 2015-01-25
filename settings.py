import os

# Desired tweet attributes
# The key is the name of the field, and the
# value is the SQLite type of that particular information.

TWEET_ATTRIBUTES = {
    "text": "text",
    "id_str": "text primary key",  # Recommended by Twitter API
    "retweeted": "integer",
    "coordinates": "text",
    "created_at": "integer",
    "retweet_count": "integer",
    "truncated": "integer",
    "user_id_str": "text",
}

# Desired user attributes. Keys and values are
# the same as above.

USER_ATTRIBUTES = {
    "created_at": "integer",
    "description": "text",
    "followers_count": "integer",
    "friends_count": "integer",
    "id_str": "text primary key",
    "location": "text",
    "screen_name": "text",
    "statuses_count": "integer",
    "time_zone": "text",
    "utc_offset": "integer",
    "verified": "integer",
}

# Directory structure settings
BASE_DIR = os.getcwd()
DATA_DIR = os.path.join(BASE_DIR, "data")

ID_DIR = os.path.join(DATA_DIR, "ids")
SQL_DIR = os.path.join(DATA_DIR, "sqlite")
JSON_DIR = os.path.join(DATA_DIR, "json")
