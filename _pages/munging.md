---
layout: page
title: Munging
permalink: /munging/
description: "Parsing, sifting, and modifying tweet text"
headings:
- top
- hipster1
- hipster2
- hipster3
- hipster4
- hipster5
---

## Cleaning the Tweets

We wanted to pare down the tweets so that the similarities and differences had as much semantic value as possible. To this end, we wanted to both remove things that wouldn't be in common between any pair of tweets and remove things that would have been common to almost every tweet. We started by sending everything to lowercase to make parsing easier and proceeded from there.

We made heavy use of [regular expressions](http://www.regular-expressions.info/) in cleaning the tweets and extracting the words we wanted. The code that did the parsing can be found in our [tweet_cleaning.py](https://github.com/tstirrat15/sentimentClusters/blob/master/tweet_cleaning.py) script.

### Retweet Strings

**Stripped:** `'rt @[\w]{1,15}: '`

One marker of a retweet is a string that looks like this:

`RT @username:`

The pattern makes use of this format, as well as the knowledge that Twitter usernames consists of between 1 and 15 alphanumeric characters

These provide one indication that a tweet is a retweet. We chose to remove them for two reasons:

1. The "rt" portion would show up in every tweet that was a retweet, and we have other ways of analyzing whether a tweet is a retweet.
2. The @username portion would be unique, or at least very uncommon, within our tweet body, and not contribute anything to the semantic content of the tweet.

### Ferguson Hashtag

**Stripped:** `'#ferguson'`

This one is pretty straightforward. Given that looking for this hashtag was one of the ways that the tweets were originally collected, this hashtag was present in the great majority of tweets.

### URL STrings

**Stripped:** `'http[s]?:\S+'`

Information about the URLs in tweets was available elsewhere in the tweet data, and the URLs by themselves don't contribute to the meaning of a tweet. We chose to use a fairly broad regular expression: this one looks for "http:" or "https:" followed by at least one non-whitespace character. While this could potentially capture something that isn't intended to be a URL, there aren't any English words that are close to the pattern, so we were comfortable removing it.

### @ Callouts

**Stripped:** `'@\w+'`

Because the @ symbol has very specific usage in tweets - it's used to reference another user - it's unlikely that by removing an @ symbol followed by at least one alphanumeric character that we will be unintentionally deleting useful information.

### Tokenizing

**Grabbed:** `'\b\S+\b'`

This regular expression matches any substring that starts with a word boundary, ends with a word boundary, and has at least one non-whitespace character within. The idea behind using non-whitespace characters as opposed to specifically looking for alphanumerics is that this retains things like contractions and other instances of punctuation embedded within words.