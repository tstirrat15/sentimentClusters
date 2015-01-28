# Python imports
import os.path
import re
import dataset
import itertools
import argparse

# NTLK imports
import nltk.corpus

# Distance import
from distance import jaccard


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
        self.url_regex = re.compile(r'http[s]?://\S+\b/?')
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
    parser = argparse.ArgumentParser()
    parser.add_argument("input", help="Input SQLite file")
    parser.add_argument("output", help="Output file - .ipairs is the preferable extension")

    # Grab arguments from command line
    args = parser.parse_args()

    # Make paths out of paths from command line
    # May actually be extraneous...
    db_path = os.path.join(os.getcwd(), args.input)
    network_path = os.path.join(os.getcwd(), args.output)

    # Make sure that we can actually write to the
    # file before we start iteration
    if not os.path.isdir(os.path.dirname(network_path)):
        raise FileNotFoundError("Can't write to path:\n{0}\nCheck that directories exist.".format(network_path))

    # Set up dataset connection to database
    db = dataset.connect("sqlite:///" + db_path)

    # Make list of Tweet objects out of db rows
    tweets = [Tweet(row["id_str"], row["text"]) for row in db["tweets"].all()]

    # Initialize the tweet processor
    p = TweetProcessor()

    # Clean all tweets on one pass.
    for tweet in tweets:
        tweet.cleaned = p.process_tweet(tweet.content)

    with open(network_path, "w") as output:
        # Iterates over all pairs without repetition
        for first, second in itertools.combinations(tweets, 2):

            # Only try and calculate distance if both sets are nonempty
            # Otherwise jaccard index has a divide by zero error
            if first.cleaned and second.cleaned:
                distance = 1 - jaccard(first.cleaned, second.cleaned)
            else:
                distance = 0

            # Only write to output if distance is nonzero - makes the
            # network file smaller and easier to handle. Can easily
            # be parsed in later.

            # Output format is based on GANXiS's input specification.
            # GANXiS looks for edges in both directions, so print tweet
            # IDs in both orders.
            if distance:
                output.write("{0} {1} {2}\n{1} {0} {2}\n".format(first.tweet_id,
                                                                 second.tweet_id,
                                                                 distance))
