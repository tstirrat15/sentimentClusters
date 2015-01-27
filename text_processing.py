import settings
import os.path
import re
import dataset
import itertools
import datetime

# NTLK imports
import nltk.corpus

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

    start = datetime.datetime.now()

    db_name = "tiny_sample.db"
    db_path = os.path.join(settings.SQL_DIR, db_name)

    network_name = "tiny_sample.ipairs"
    network_path = os.path.join(settings.NETWORK_DIR, "tiny_sample.ipairs")

    db = dataset.connect("sqlite:///" + db_path)

    p = JaccardProcessor()

    tweets = [Tweet(row["id_str"], row["text"]) for row in db["tweets"].all()]

    for tweet in tweets:
        tweet.cleaned = p.process_tweet(tweet.content)

    with open(network_path, "w") as output:
        for first, second in itertools.combinations(tweets, 2):
            distance = 1 - p.jaccard(first.cleaned, second.cleaned)
            if distance:
                output.write("{0} {1} {2}\n{1} {0} {2}\n".format(first.tweet_id,
                                                             second.tweet_id,
                                                             distance))

    print(datetime.datetime.now() - start)
