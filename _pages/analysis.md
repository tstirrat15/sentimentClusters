---
layout: page
title: Analysis
permalink: /analysis/
description: What we found upon peering in.
headings:
- top
- hipster1
- hipster2
- hipster3
- hipster4
- hipster5
---

## The Geography of Tweets

We wanted to start our analysis by identifying the location from which the tweets originated. The majority of the tweets lacked information detailing the latitude and longitude of the user. Our next option was to use the user’s time zone to identify from which region of the United States the tweets came. Using the time zones gave us general answers to our questions about how important the Ferguson conversation was to certain regions of the US and how much of the nation was engaged in the conversation.

Given that we lacked information on latitude and longitude, we needed to construct a map that best represented the data that we collected without the use of the US map. We decided that a tree map would provide a good visual of the frequency of tweets within each region. In addition to grouping tweets by region, we added a second level to analyze the frequency of tweets, in their cluster groups, within each region.

![img](/assets/tweet_time_zone_tree_map.png){: .img-responsive}


The tree map shows us that the Eastern Time Zone has the most number of tweets among all of the time zones. The Central Time Zone was the second largest group. It is interesting that there are more tweets about Ferguson in Eastern Time than there are in Central Time given that Ferguson, MO is in the middle of the Central Time Zone. We suspected that the possible reason for these results were that there were also incidents of police shootings in New York and Ohio with Eric Garner and Tamir Rice, respectively. The shootings may have motivated individuals in those areas to tweet more about issues related to Ferguson and the protests, causing a rise in tweets in that region.

It seemed that the conversations in all of the time zones were related to “General-Protest” and “Protest Call-to-Action.” We concluded the conversations about Ferguson were related to people’s opinions and sentiments regarding the protests than specific accounts of the events. The tweets also showed support and solidarity with the protesters. A large number of the tweets criticized government action, or lack thereof.

Although we saw that the largest clusters in all of the time zones are “General-Protest” and “Protest Call-to-Action”, we also noticed that there are much fewer tweets in Pacific and Mountain Times. Mountain Time was noticeably the smallest group. There may have been less conflict in that region or less exposure to the events resulting in a smaller number of tweets. With more information about the tweets, such as the user’s location via latitude and longitude, we would get a clearer understanding of which areas are most dense.

Using latitude and longitude allows us to map out tweets to provide a clear visual of tweet density on a US map. We would then be able to see which states were most engaged in the Ferguson conversation and which participated the least. Constructing maps for each cluster would give us a better view of the salience of each subtopic across the US. More data about location will be useful for future analysis and visualization.

## The Conversation Over Time

### August

In addition to seeing how the conversations on twitter were different based on where the tweeters were from, we also wanted to see how the conversations changed over time, and whether you could see the impacts of real world actions and events on twitter.

By creating a stacked graph of how many tweets were made per day by each cluster, we can examine how the conversation changed over time; our samples took tweets from the month of August when the Ferguson protests began, and from November to early December centered around when the Grand Jury released their indictment decision, so we created a stacked graph of each sample to avoid needing to truncate a complete timeline that would have no tweets during September or October.

![img](/assets/august_tweets_stream_graph.png){: .img-responsive}

The August sample starts gathering tweets from the 10th, one day after the death of Michael Brown, and within two days it had become a fairly popular subject of discussion, and that in this initial period only a few clusters were being discussed, mainly the two general clusters but there is a noticeable amount of tweets from the “race” and “tear gas” clusters as well. November 14th was the day that discussion of Ferguson ballooned into a national subject as President Obama gave a national address on Brown’s death, the Ferguson police and the protests that had taken place in response to the situation; while every cluster experienced growth in this spike, the “police reform” cluster takes a much larger percentage of tweets that day and never has a percentage so high again.

Protests in Ferguson remained on twitter’s mind for the next few days and we see the discussion ramp up from the last week. Over those days we also saw the intensity of conflict between protesters and police ramp up, which lead to controversial actions being taken such as the calling in of the National Guard and the arrest of prominent journalists reporting on the protests.  Interestingly, the “arresting journalists” cluster gains more activity than the “National Guard” cluster, which could be potentially explained in a few ways: it could be that people were more aware of the arrested journalists as other writers and reporters would be more likely to care about that issue and thus spent more time on it, it could also be that not as many people were tweeting about the National Guard because they didn’t believe they could make a difference about that decision, while they could potentially get reporters released by pressuring the police for long enough. The increasing violence between the protesters and police forces at this time can also explain the increase in the “riot” cluster seen between days 18 and 19, as some believed that people were using the death of Brown as an excuse to riot and loot and pass it off as peaceful protest.

Tensions between the Ferguson police department and protestors began to thaw around August 21st with the systematic withdrawal of the National Guard from the city, and with that relative peace came a drop in the amount of tweets being made every day and clusters such as tear gas and National Guard becoming practically invisible within all the combined clusters.  Without any major events going on within the protests, it was still tweeted about but not at nearly as high numbers as earlier in the month, which is why we chose to make the second half of our sample take place during November and into December, which captured the Grand Jury’s decision and other events.

### November and December

![img]()