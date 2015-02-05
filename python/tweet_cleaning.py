# Python imports
import os.path
import re
import dataset
import argparse

# NTLK imports
import nltk.corpus

# Someday: set this up for parallel processing, based on number of cores


class Tweet(object):
    """Holds attributes of tweets"""
    def __init__(self, tweet_id, tweet_text):
        self.tweet_id = tweet_id
        self.content = tweet_text


class TweetProcessor(object):
    """Class that provides tweet processing specific to
    our Jaccard index analysis. Encapsulates the regular
    expressions and stopwords for reuse upon multiple
    calls to process_tweet."""
    def __init__(self):
        self.stopwords = nltk.corpus.stopwords.words("english")

        # Trying different options for tokenizing
        # self.tokenize = word_tokenize

        # Compile regex expressions for later reuse
        self.retweet_regex = re.compile(r'^rt @[\w]{1,15}: ')
        self.ferguson_ht_regex = re.compile(r'#ferguson')
        self.url_regex = re.compile(r'http[s]?:\S+')
        self.callout_regex = re.compile(r'@\w+')
        self.token_regex = re.compile(r'\b\S+\b')

    def process_tweet(self, tweet):
        # Send to lower
        tweet = tweet.lower()
        # Strip retweets
        tweet = self.retweet_regex.sub('', tweet)
        # Remove ferguson hashtag
        tweet = self.ferguson_ht_regex.sub('', tweet)
        # Remove URLs
        tweet = self.url_regex.sub('', tweet)
        # Remove @ references
        tweet = self.callout_regex.sub('', tweet)
        # Split on whitespace
        tokens = self.tokenize(tweet)
        # Remove stopwords
        tokens = [word for word in tokens
                  if word not in self.stopwords]
        # Return tokens. Jaccard already does the setting, so no
        # need to return as set.
        return tokens

    def tokenize(self, string):
        """Custom tokenizing function. Splits on word boundaries
        with whitespace between them. """
        return self.token_regex.findall(string)


if __name__ == "__main__":

    # Set up argument parsing
    parser = argparse.ArgumentParser(description=""""Takes an SQLite database
        of tweets as an input, and outputs a list of tweet ID pairs along with
        their Jaccard index, based on a processed version of each tweet.""")
    parser.add_argument("input", help="Input SQLite file")

    # Grab arguments from command line
    args = parser.parse_args()

    # Make paths out of paths from command line
    # May actually be extraneous...
    db_path = os.path.join(os.getcwd(), args.input)

    # Initialize the tweet processor
    p = TweetProcessor()

    # Set up dataset connection to database
    with dataset.connect("sqlite:///" + db_path) as db:
        tweets = [Tweet(row["id_str"], row["text"]) for row in db["tweets"].all()]

    with dataset.connect("sqlite:///" + db_path) as db:
        for tweet in tweets:
            tweet.cleaned = p.process_tweet(tweet.content)
            tweet.cleaned = " ".join(tweet.cleaned)
            db["tweets"].update({"id_str": tweet.tweet_id, "cleaned": tweet.cleaned}, ["id_str"])
