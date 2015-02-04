#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import json
import dataset
import argparse
from tweet_cleaning import TweetProcessor


class JSONObject(dict):
    # Borrowed from Birdy: https://github.com/inueni/birdy
    # Changed "name in self.iterkeys()" to "name in self.keys()"
    # which fixed things for python3.
    def __getattr__(self, name):
        if name in self.keys():
            return self[name]
        raise AttributeError('%s has no property named %s.'
                             % (self.__class__.__name__, name))

    def __setattr__(self, *args):
        raise AttributeError('%s instances are read-only.'
                             % self.__class__.__name__)
    __delattr__ = __setitem__ = __delitem__ = __setattr__

    def __repr__(self):
        return '<%s: %s>' % (self.__class__.__name__, dict.__repr__(self))


def get_object_hook(data):
    return JSONObject(data)


# Passing down the parser like this is a hack.
def get_tweet_data(json_string, parser):
    tweet_object = json.loads(json_string, object_hook=get_object_hook)
    tweet_dict = get_tweet_dict_from_object(tweet_object, parser)
    return tweet_dict


def get_tweet_dict_from_object(tweet_object, parser):
    tweet_dict = {}

    # Assigning all of the attributes to dictionary values
    tweet_dict["text"] = tweet_object.text
    tweet_dict["id_str"] = tweet_object.id_str
    tweet_dict["was_retweeted"] = tweet_object.retweeted
    tweet_dict["created_at"] = tweet_object.created_at
    tweet_dict["retweet_count"] = tweet_object.retweet_count
    tweet_dict["truncated"] = tweet_object.truncated
    tweet_dict["user_id_str"] = tweet_object.user.id_str

    # Handle coordinate values
    if tweet_object.coordinates:
        tweet_dict["tweet_lat"] = tweet_object.coordinates.coordinates[1]
        tweet_dict["tweet_long"] = tweet_object.coordinates.coordinates[0]
    else:
        tweet_dict["tweet_lat"] = None
        tweet_dict["tweet_long"] = None

    # Check to see whether retweeted_status exists, set is_retweet accordingly
    if hasattr(tweet_object, "retweeted_status"):
        tweet_dict["is_retweet"] = True
    else:
        tweet_dict["is_retweet"] = False

    tweet_dict["user_created_at"] = tweet_object.user.created_at
    tweet_dict["user_description"] = tweet_object.user.description
    tweet_dict["user_followers_count"] = tweet_object.user.followers_count
    tweet_dict["user_friends_count"] = tweet_object.user.friends_count
    tweet_dict["user_location"] = tweet_object.user.location
    tweet_dict["user_screen_name"] = tweet_object.user.screen_name
    tweet_dict["user_statuses_count"] = tweet_object.user.statuses_count
    tweet_dict["user_time_zone"] = tweet_object.user.time_zone
    tweet_dict["user_utc_offset"] = tweet_object.user.utc_offset
    tweet_dict["user_verified"] = tweet_object.user.verified

    # Add a cleaned tweet field
    tweet_dict["cleaned_text"] = " ".join(parser.process_tweet(tweet_object.text))

    return tweet_dict

if __name__ == '__main__':
    # Set up argparse
    parser = argparse.ArgumentParser("""Takes a file of line-oriented
        Tweet JSON objects as input and outputs a selection of values
        to an SQLite database.""")

    parser.add_argument("input", help="Relative path to JSON input file")
    parser.add_argument("output", help="Relative path to desired SQLite DB output location")

    args = parser.parse_args()

    # Instantiate tweet parser
    p = TweetProcessor()

    with open(args.input, "r") as json_file:
        with dataset.connect("sqlite:///" + args.output) as db:
            tweet_dicts = [get_tweet_data(json_string, p)
                           for json_string in json_file]
            db["tweets"].insert_many(tweet_dicts)
