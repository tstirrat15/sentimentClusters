---
layout: page
title: Munging
permalink: /munging/
description: "Parsing, sifting, modifying"
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

### Retweet Strings

**Stripped:** `"^rt @[\w]{1,15}: "`

One marker of a retweet is a string that looks like this:

`RT @username:`

These provide one indication that a tweet is a retweet. We chose to remove them for two reasons:

1. The "rt" portion would show up in every tweet that was a retweet, and we have other ways of analyzing whether a tweet is a retweet.
2. The @username portion would be unique, or at least very uncommon, within our tweet body, and not contribute anything to the semantic content of the tweet.
