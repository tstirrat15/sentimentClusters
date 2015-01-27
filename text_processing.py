import settings
import os.path
import re
import dataset

# NTLK imports
import nltk.corpus
import nltk.stem.snowball
from nltk import word_tokenize

# Distance import
from distance import jaccard


# Access SQL database
# Get set of tweets pulled in

# Someday: set this up for parallel processing, based on number of cores

# Things to do for text processing:
# Remove retweet string
# Remove ferguson hashtag
# Tokenize
# Remove stopwords
# Stem

class JaccardProcessor(object):
    """docstring for JaccardProcessor"""
    def __init__(self):
        self.stopwords = nltk.corpus.stopwords.words("english")
        self.stemmer = nltk.stem.snowball.SnowballStemmer('english')
        self.tokenize = word_tokenize

        # Compile regex expressions for later reuse
        self.retweet_regex = re.compile(r'^rt @[\w]{1,15}: ')
        self.ferguson_ht_regex = re.compile(r'#ferguson')
        self.url_regex = re.compile(r'http[s]?://\S+\b/?')

        # Claim the function. Not sure if this works this way.
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
        # Split on whitespace
        tokens = self.tokenize(tweet)
        # Remove stopwords
        tokens = [word for word in tokens
                  if word not in self.stopwords]
        # Return tokens. Jaccard already does the setting, so no
        # need to return as set.
        return tokens

if __name__ == "__main__":
    p = JaccardProcessor()
    tweets = [
        "RT @KiaHutch: How is this BETTER than what we've been seeing the past few nights? How is this your go to @GovJayNixon? #Ferguson",
        "RT @WRDSMATTER: Racial reactions to Ferguson even stronger than to Trayvon Martin http://t.co/WUvlce1cfA",
        "Tiffany Mitchell, eyewitness said that #MikeBrown was trying to get away from the cop, from the car. Cop pursued while shooting #Ferguson",
        "RT @petewentz: :( #ferguson",
        """RT @_DirtyTruths: #Ferguson: Cops Gone Wild - The most fatal mistake that any American can make is to call the police http://t.co/g7zFAkl0…""",
    ]
    for tweet in tweets:
        print(tweet)
        print(p.process_tweet(tweet))
