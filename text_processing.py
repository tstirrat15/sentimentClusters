import settings
import os.path
import re
import dataset
import itertools

# NTLK imports
import nltk.corpus
import nltk.stem.snowball
from nltk import word_tokenize

# Distance import
from distance import jaccard


# Access SQL database
# Get set of tweets pulled in as tuples:

# Someday: set this up for parallel processing, based on number of cores

class Tweet(object):
    """Holds attributes of tweets"""
    def __init__(self, tweet_id, tweet_text):
        self.tweet_id = tweet_id
        self.content = tweet_text


class JaccardProcessor(object):
    """docstring for JaccardProcessor"""
    def __init__(self):
        self.stopwords = nltk.corpus.stopwords.words("english")
        self.stemmer = nltk.stem.snowball.SnowballStemmer('english')

        # Trying different options for tokenizing
        # self.tokenize = word_tokenize

        # Compile regex expressions for later reuse
        self.retweet_regex = re.compile(r'^rt @[\w]{1,15}: ')
        self.ferguson_ht_regex = re.compile(r'#ferguson')
        self.url_regex = re.compile(r'http[s]?://\S+\b/?')
        self.callout_regex = re.compile(r'@\w+')
        self.token_regex = re.compile(r'\b\S+\b')

        # Claim the function. Not sure if this works this way.
        # It does! but it also probably makes sense to pull this
        # outside of the function. Everything else about this class
        # is just text processing.
        self.jaccard = jaccard

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
        # Remove leading and trailing whitespace
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
    db_path = os.path.join(settings.SQL_DIR)
    p = JaccardProcessor()

    # This is how we get the pairwise stuff
    for first, second in itertools.combinations(tweets, 2):
        first_processed = p.process_tweet(first)
        second_processed = p.process_tweet(second)
        print("===========")
        print(first)
        print(first_processed)
        print(second)
        print(second_processed)
        print(p.jaccard(first_processed, second_processed))
