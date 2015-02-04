---
layout: page
title: Data Collection
permalink: /data_collection/
description: Where and how we found our tweets
headings:
- top
- hipster1
- hipster2
- hipster3
- hipster4
- hipster5
---

## The Data Set

For this demonstration of our methodology, we chose to focus on a body of tweets concerning the events that occured in Ferguson, Missouri in Fall 2014. These tweets were originally collected and analyzed by [Ed Summers](http://inkdroid.org/journal/2014/11/18/on-forgetting/). The data set is [freely available online](https://archive.org/details/ferguson-tweet-ids), and we began collection there. There were two data sets: one of tweets collected during the time period from 2014-08-10 to 2014-08-27, in the two weeks following the shooting of Michael Brown, and a second one of tweets collected from 2014-11-11 and 2014-12-08, following the indictment decision.

## Hydrating the tweets

The data set, due to Twitter's [Terms of Service](https://dev.twitter.com/overview/terms/policy#6._Be_a_Good_Partner_to_Twitter), consisted only of tweet IDs. In order to access the full content of each tweet, we had to use our own access to the API to "hydrate" the tweets. Fortunately, there's a Python utility called [twarc](https://github.com/edsu/twarc) that takes care of downloading the raw JSON data for each tweet, automatically respecting rate limits. If you're interested in working with tweet data sets that others have made available, we highly recommend it.

## A Simple Random Sample

These data sets were massive: approximately 13 million and 15 million tweets, respectively. Due to constraints on both computing power available and rate limiting by the Twitter API, we chose to take a simple random sample of 10,000 tweet IDs from each of the two data sets, using the [shuf](http://linux.die.net/man/1/shuf) program from the GNU coreutils.

## SQLite

In order to be able to access the data easily in both Python and R, we chose to use an [SQLite](http://www.sqlite.org/) database to store the various attributes of the tweets that we were interested in. It lends itself well to R's tabular style, and has the advantage of being file-based, so the data set doesn't need to be completely loaded into memory before you can manipulate it. We used our [load_tweets.py](https://github.com/tstirrat15/sentimentClusters/blob/master/load_tweets.py) script to select the attributes that we wanted and then move from the raw JSON to an SQLite database.