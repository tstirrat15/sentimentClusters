#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import json
# import dataset
# import birdy
import os.path
import settings
import sqlite3

"""All of this really needs to be encapsulated for how much flipping
cross-referencing I'm doing."""

"""Also, I had completely forgotten about dataset. I should refactor this to
use it."""

"""Currently, it seems as though there's an issue with the way I'm defining my
columns. I think it might have something to do with having a column called "text",
which I think is typically reserved for typenames."""

"""Next step is to just do this as a flat table, with user id being just put in
there. It'll require some hardcoding of referenced attributes, but that shouldn't
be too bad if i use getattr()"""

"""Also, change this to make it into a command-line utility - use sysvargs
instead of hardcoding filepaths. Let the command line take care of things."""


def make_table(connection, table_name, table_header_list):
    table_headers = "(" + ",".join(table_header_list) + ")"
    query = "create table if not exists " + table_name + " " + table_headers
    connection.execute(query)


def make_value_list(dictionary):

    # Get all data at first level
    data = [dictionary[key] for key in sorted(dictionary.keys())
            if not isinstance(dictionary[key], dict)]

    # Turn all of this into a tuple and return;
    # should preserve order.
    return data


def table_creation_query_list(column_dict):
    return [key + " " + column_dict[key] for key in sorted(column_dict.keys())]


def make_insertion_tuples(json_entry):
    json_dict = json.loads(json_entry)

    tweet_values = [json_dict[key] for key in sorted(settings.TWEET_ATTRIBUTES.keys()) if not key == "user_id_str"]
    tweet_values += [json_dict["user"]["id_str"]]
    tweet_values = tuple(tweet_values)
    user_values = tuple([json_dict["user"][key] for key in sorted(settings.USER_ATTRIBUTES.keys())])

    return tweet_values, user_values


if __name__ == '__main__':
    file_path = os.path.join(settings.JSON_DIR, 'sample.json')
    db_path = os.path.join(settings.SQL_DIR, 'sample.db')

    user_column_list = table_creation_query_list(settings.USER_ATTRIBUTES)
    tweet_column_list = table_creation_query_list(settings.TWEET_ATTRIBUTES)

    # Append foreign ID to tweets so that tweets are associated with users.
    # Doesn't really make sense in the 1-to-many sense, but oh well.
    tweet_column_list.append("foreign key(user_id_str) references users(id_str)")

    # Also means that I have to be careful to add users before I add associated tweets

    with open(file_path, "r") as json_file:
        with sqlite3.connect(db_path) as con:

            # Create user and tweet tables, if not already done
            make_table(con, "users", user_column_list)
            make_table(con, "tweets", tweet_column_list)

            tweet_data = []
            user_data = []

            # Create all of the queries at once
            for json_entry in json_file:
                tweet_values, user_values = make_insertion_tuples(json_entry)
                tweet_data.append(tweet_values)
                user_data.append(user_values)

            print("First line of user_data:")
            print(user_data[0])
            print("First line of tweet_data:")
            print(tweet_data[0])

            # insert user data
            # Get the length of the user tuple and construct a ? string
            user_qm_string = "(" + ",".join(["?"] * len(user_data[0])) + ")"
            con.executemany("INSERT OR IGNORE INTO users VALUES " + user_qm_string, user_data)

            tweet_qm_string = "(" + ",".join(["?"] * len(tweet_data[0])) + ")"
            con.executemany("INSERT INTO tweets VALUES " + tweet_qm_string, tweet_data)
