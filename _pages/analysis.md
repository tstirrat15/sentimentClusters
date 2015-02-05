---
layout: page
title: Analysis
permalink: /analysis/
description: What we found upon peering in.
headings:
- link: august
  title: "The Conversation: August"
- link: novdec
  title: "The Conversation: Nov. - Dec."
- link: echo
  title: Echo Chambers
- link: geography
  title: The Geography of Tweets
---

<a id="august" class="anchor"></a>

## The Conversation Over Time

### August

In addition to seeing how the conversations on twitter were different based on where the tweeters were from, we also wanted to see how the conversations changed over time, and whether you could see the impacts of real world actions and events on twitter.

By creating a stacked graph of how many tweets were made per day by each cluster, we can examine how the conversation changed over time; our samples took tweets from the month of August when the Ferguson protests began, and from November to early December centered around when the Grand Jury released their indictment decision, so we created a stacked graph of each sample to avoid needing to truncate a complete timeline that would have no tweets during September or October.

![img]({{ site.baseurl }}/assets/august_tweets_stream_graph.png){: .img-responsive}

The August sample starts gathering tweets from the 10th, one day after the death of Michael Brown, and within two days it had become a fairly popular subject of discussion, and that in this initial period only a few clusters were being discussed, mainly the two general clusters but there is a noticeable amount of tweets from the “race” and “tear gas” clusters as well. November 14th was the day that discussion of Ferguson ballooned into a national subject as President Obama gave a national address on Brown’s death, the Ferguson police and the protests that had taken place in response to the situation; while every cluster experienced growth in this spike, the “police reform” cluster takes a much larger percentage of tweets that day and never has a percentage so high again.

Protests in Ferguson remained on twitter’s mind for the next few days and we see the discussion ramp up from the last week. Over those days we also saw the intensity of conflict between protesters and police ramp up, which lead to controversial actions being taken such as the calling in of the National Guard and the arrest of prominent journalists reporting on the protests.  Interestingly, the “arresting journalists” cluster gains more activity than the “National Guard” cluster, which could be potentially explained in a few ways: it could be that people were more aware of the arrested journalists as other writers and reporters would be more likely to care about that issue and thus spent more time on it, it could also be that not as many people were tweeting about the National Guard because they didn’t believe they could make a difference about that decision, while they could potentially get reporters released by pressuring the police for long enough. The increasing violence between the protesters and police forces at this time can also explain the increase in the “riot” cluster seen between days 18 and 19, as some believed that people were using the death of Brown as an excuse to riot and loot and pass it off as peaceful protest.

Tensions between the Ferguson police department and protestors began to thaw around August 21st with the systematic withdrawal of the National Guard from the city, and with that relative peace came a drop in the amount of tweets being made every day and clusters such as tear gas and National Guard becoming practically invisible within all the combined clusters.  Without any major events going on within the protests, it was still tweeted about but not at nearly as high numbers as earlier in the month, which is why we chose to make the second half of our sample take place during November and into December, which captured the Grand Jury’s decision and other events.

<a id="novdec" class="anchor"></a>

### November and December

![img]({{ site.baseurl }}/assets/november_december_tweets_stream.png){: .img-responsive}

Starting with tweets from November 11th, we see that the twitter discussion on Ferguson remains slower, but is still active as Americans wait for the Grand Jury to come to their decision on whether or not to indict officer Wilson for killing Brown, and in the days leading up to the announcement all clusters see an increase, with the “civil progress” cluster becoming the largest of the non-general clusters.  Then, November 24th, early on a Monday morning, the Grand Jury announced their decision of non-indictment towards Officer Wilson, sending shockwaves all across America and giving us our tallest, longest spike of tweets.

Throughout this spike we see that the “race” cluster is more active than it had been at any other point in time, as is the “riot” cluster, showing that the Grand Jury’s decision turned a corner in how twitter discussed the Ferguson protests. For many, the non-indictment was a racially-motivated failure of the justice system and many ideas and hashtags created during the Trayvon Martin protests, such as #blacklivesmatter, were reclaimed and used again to discuss racial divides in America. However, to many others the continued, and increasingly violent, protests after the decision seemed to be rioting against the justice system and a demand for a mob-rule decision on the issue. After three hectic days of mass protesting and tweeting, tweets began to drop off rapidly as the Ferguson government held strong to the decision of the Grand Jury. The decrease in tweets ends on November 29th, when Officer Wilson announced his resignation from the Ferguson police department, and the “indictment decision” cluster grows larger which we believe is directed again at the non-indictment decision and that willingly leaving his job was not enough of a punishment.

The last major event of the Ferguson protests happened on December 1st, the “Hands Up, Walk Out” solidarity movement was a nationwide scheduled walk-out against the non-indictment decision. This event also saw a return of the “police reform” cluster which had largely been inactive except during times when all clusters saw increases, this could be showing a return to the earlier idea of focusing the protests on demanding a demilitarization of police forces and adding additional checks on officers such as cameras on uniforms to remove ambiguity of events like Brown’s death.

<a id="echo" class="anchor"></a>

## Echo Chambers

One major societal change brought about by the internet that is rarely discussed or even recognized is the change in how Americans get their news. It used to be that there were very few major sources of national news, which meant that those companies had the ability to act as gatekeepers to information, if there was a particular story, opinion or fact that they didn’t want the public to know they could simply not bring it up and few would be any wiser. Another part of having only a few sources of news was that those sources needed to all present themselves as fairly unbiased because they needed to capture as much of the market as they could to remain  competitive against the other news behemoths, because being a news station required massive funding and popularity to survive.

The internet changed this entire dynamic by making it possible for absolutely anyone to share the news or their opinions on it through blogs or internet newspapers, and the far lower costs to operating one of these meant that people could take an ideological stance on an issue instead of playing the moderate and keep a small, but dedicated, reader base. The rise of biased news meant that readers could search out news sources that held the same beliefs and opinions as themselves and only hear thoughts that they already agreed with. This echochamber of opinion presents problems when discussing any controversial issue, and is often blamed for the partisan nature of our current government. Since twitter is used as both a way of getting news information and as a social media website, we wanted to examine whether the ideas of the echochamber and homophily held true when discussing Ferguson on twitter.

Twitter’s “ReTweet” function allows a user to post someone else’s tweet again for their friends and followers to see, but doesn’t add to the discussion of that tweet.  By examining the percentage of each cluster’s tweets that are retweets, we should get an idea of whether people are posting new, original thoughts or simply repeating what they have heard and agree with.

Each time a user retweet from another person they will put “RT” characters in their tweets. Even though this is not an official function from Twitters, this practice is considered the norm for Twitter users. Therefore, we are confident that by identifying all the tweets that have “RT” in their contents, we have a good estimate of how many tweets are retweets. Further more, we only consider the tweets starting with “RT”, since these tweets consists only the only The actual code is simple, using the substr function in R to extract from each tweet the first two characters, which is “RT” if a tweet is a retweet.

![img]({{ site.baseurl }}/assets/retweet_relative_frequency.png){: .img-responsive}

Immediately, we can see that two of our clusters have a ridiculously high percentage of retweets, where every tweet contained in the cluster is a retweet of the same original tweet. With tens of thousands of our tweets being the exact same message, it makes sense that any significant number of retweets would be clustered together and excludes any other tweets, and because we took only a small sample of the total tweets we have, these clusters may not be representative of the entire data set. For our other 11 clusters however, it is surprising that every one of them features a retweet percentage of over 50%, and may be indicative of twitter functioning as an echochamber for its users.

<a id="geography" class="anchor"></a>

## The Geography of Tweets

We wanted to start our analysis by identifying the location from which the tweets originated. The majority of the tweets lacked information detailing the latitude and longitude of the user. Our next option was to use the user’s time zone to identify from which region of the United States the tweets came. Using the time zones gave us general answers to our questions about how important the Ferguson conversation was to certain regions of the US and how much of the nation was engaged in the conversation.

Given that we lacked information on latitude and longitude, we needed to construct a map that best represented the data that we collected without the use of the US map. We decided that a tree map would provide a good visual of the frequency of tweets within each region. In addition to grouping tweets by region, we added a second level to analyze the frequency of tweets, in their cluster groups, within each region.

![img]({{ site.baseurl }}/assets/tweet_time_zone_tree_map.png){: .img-responsive}


The tree map shows us that the Eastern Time Zone has the most number of tweets among all of the time zones. The Central Time Zone was the second largest group. It is interesting that there are more tweets about Ferguson in Eastern Time than there are in Central Time given that Ferguson, MO is in the middle of the Central Time Zone. We suspected that the possible reason for these results were that there were also incidents of police shootings in New York and Ohio with Eric Garner and Tamir Rice, respectively. The shootings may have motivated individuals in those areas to tweet more about issues related to Ferguson and the protests, causing a rise in tweets in that region.

It seemed that the conversations in all of the time zones were related to “General-Protest” and “Protest Call-to-Action.” We concluded the conversations about Ferguson were related to people’s opinions and sentiments regarding the protests than specific accounts of the events. The tweets also showed support and solidarity with the protesters. A large number of the tweets criticized government action, or lack thereof.

Although we saw that the largest clusters in all of the time zones are “General-Protest” and “Protest Call-to-Action”, we also noticed that there are much fewer tweets in Pacific and Mountain Times. Mountain Time was noticeably the smallest group. There may have been less conflict in that region or less exposure to the events resulting in a smaller number of tweets. With more information about the tweets, such as the user’s location via latitude and longitude, we would get a clearer understanding of which areas are most dense.

Using latitude and longitude allows us to map out tweets to provide a clear visual of tweet density on a US map. We would then be able to see which states were most engaged in the Ferguson conversation and which participated the least. Constructing maps for each cluster would give us a better view of the salience of each subtopic across the US. More data about location will be useful for future analysis and visualization.
