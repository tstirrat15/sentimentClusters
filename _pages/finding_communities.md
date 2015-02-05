---
layout: page
title: Finding Communities
permalink: /finding_communities/
description: How we went about grouping tweets together
headings:
- link: clusters
  title: Our Clusters
- link: "finding-distance"
  title: Finding Distance
- link: "distance-comparison"
  title: Distance Comparison
- link: "freq-analysis"
  title: Word Frequency Analysis
- link: algorithm
  title: The Algorithm
---
<a id="clusters" class="anchor"></a>

## Our Clusters

The categories seen below were generated manually by referencing the original tweets used to generate the clusters. Listed under each cluster is the top ten words appearing in that particular cluster.

<!-- Big fat nasty tables -->

<table class="table table-condensed table-bordered">
  <tr>
    <th>General - Protest</th>
    <th>Police Reform</th>
    <th>Race</th>
    <th>Arresting Journalists</th>
    <th>Protest - Call to Action</th>
    <th>National Guard</th>
  </tr>
  <tr>
    <td>police</td>
    <td>police</td>
    <td>black</td>
    <td>arrest</td>
    <td>protest</td>
    <td>nation</td>
  </tr>
  <tr>
    <td>protest</td>
    <td>chief</td>
    <td>people</td>
    <td>report</td>
    <td>mikebrown</td>
    <td>guard</td>
  </tr>
  <tr>
    <td>cop</td>
    <td>camera</td>
    <td>white</td>
    <td>police</td>
    <td>police</td>
    <td>police</td>
  </tr>
  <tr>
    <td>amp</td>
    <td>force</td>
    <td>cop</td>
    <td>protest</td>
    <td>live</td>
    <td>missouri</td>
  </tr>
  <tr>
    <td>dont</td>
    <td>depart</td>
    <td>protest</td>
    <td>journalist</td>
    <td>happen</td>
    <td>deploy</td>
  </tr>
  <tr>
    <td>officer</td>
    <td>protest</td>
    <td>police</td>
    <td>holocaust</td>
    <td>people</td>
    <td>governor</td>
  </tr>
  <tr>
    <td>shoot</td>
    <td>obama</td>
    <td>kill</td>
    <td>survivor</td>
    <td>amp</td>
    <td>protest</td>
  </tr>
  <tr>
    <td>media</td>
    <td>amp</td>
    <td>riot</td>
    <td>photograph</td>
    <td>decision</td>
    <td>call</td>
  </tr>
  <tr>
    <td>people</td>
    <td>america</td>
    <td>man</td>
    <td>getting</td>
    <td>america</td>
    <td>protect</td>
  </tr>
  <tr>
    <td>obama</td>
    <td>mikebrown</td>
    <td>obama</td>
    <td>epistein</td>
    <td>time</td>
    <td>send</td>
  </tr>
</table>

<table class="table table-condensed table-bordered">
  <tr>
    <th>General - Incident</th>
    <th>Tear Gas</th>
    <th>Riot</th>
    <th>Civil Progress</th>
    <th>Indictment Decision</th>
    <th>Darren Wilson</th>
    <th>Flag Burning</th>
  </tr>
  <tr>
    <td>brown</td>
    <td>tear</td>
    <td>protest</td>
    <td>act</td>
    <td>jury</td>
    <td>wilson</td>
    <td>act</td>
  </tr>
  <tr>
    <td>michael</td>
    <td>gas</td>
    <td>police</td>
    <td>behold</td>
    <td>grand</td>
    <td>darren</td>
    <td>american</td>
  </tr>
  <tr>
    <td>mike</td>
    <td>police</td>
    <td>block</td>
    <td>civil</td>
    <td>decision</td>
    <td>police</td>
    <td>care</td>
  </tr>
  <tr>
    <td>police</td>
    <td>protest</td>
    <td>office</td>
    <td>picture</td>
    <td>protest</td>
    <td>officer</td>
    <td>dont</td>
  </tr>
  <tr>
    <td>shot</td>
    <td>fire</td>
    <td>riot</td>
    <td>progress</td>
    <td>indictment</td>
    <td>resign</td>
    <td>side</td>
  </tr>
  <tr>
    <td>officer</td>
    <td>people</td>
    <td>break</td>
    <td>right</td>
    <td>announce</td>
    <td>arrest</td>
    <td>trial</td>
  </tr>
  <tr>
    <td>darren</td>
    <td>gassed</td>
    <td>deandre</td>
    <td>year</td>
    <td>wilson</td>
    <td>cop</td>
    <td>agree</td>
  </tr>
  <tr>
    <td>wilson</td>
    <td>report</td>
    <td>joshua</td>
    <td></td>
    <td>brown</td>
    <td>kill</td>
    <td></td>
  </tr>
  <tr>
    <td>shoot</td>
    <td>crew</td>
    <td>call</td>
    <td></td>
    <td>case</td>
    <td>mikebrown</td>
    <td></td>
  </tr>
  <tr>
    <td>kill</td>
    <td>hit</td>
    <td>missouri</td>
    <td></td>
    <td>prosecutor</td>
    <td>news</td>
    <td></td>
  </tr>
</table>


![img]({{ site.baseurl }}/assets/labeled_cluster_relative_frequency.png)

As you can see, there are two massive clusters, which together consists of 73% of the tweets in our data set. This leaves room for further improvement in terms of cleaning data and choosing the optimal clustering algorithm for this type of problem.

<a id="finding-distance" class="anchor"></a>

## How We Found Them

###Finding Distance:

Using a technique in Text Mining called [bag-of-words](http://en.wikipedia.org/wiki/Bag-of-words_model), we turned each tweet to a bag of words. Therefore, we only care about the word occurrence and not the word order nor grammar. This method certainly has disadvantages in detecting the semantic meaning of the tweets, for example, it fails detect sarcasm or negation. However, in this project we want to identify subtopics within Ferguson event, so this approach fits our goal. Using this approach, we turn each of our tweets into a binary vector with each dimension representing a unique word.

In order to measure the pairwise difference among tweets, we consider two different distance methods: Jaccard and Euclidean indices.

#### Jaccard Index

The [Jaccard index](http://en.wikipedia.org/wiki/Jaccard_index) is simply the size of the intersection of two sets divided by the size of the union of the sets:
\\[ \mathrm{Jaccard}(A, B) = \frac{|A \cap B|}{|A \cup B|} \\]

This index measures the similarity between two text documents by the number of words that appear in both documents divided by the number of words that appear in either documents. Jaccard similarity index ranges from 0 to 1, so we get the Jaccard distance by taking 1 minus this number.

#### Euclidean Distance

The [Euclidean distance](http://en.wikipedia.org/wiki/Euclidean_distance) is the ordinary distance between two points in the Euclidean space. In our project, each tweet, which is converted to a binary vector, can be considered a point in space; therefore, we can compute the Euclidean distance between any two tweets.

<a id="distance-comparison" class="anchor"></a>

### Comparing the Distances

![img]({{ site.baseurl }}/assets/jaccard_distance_distribution.png){: .img-responsive}

After running a few trials with different clustering methods, we realize that Jaccard distance does not work as well as the the Euclidean distance. As shown below, most of our Jaccard distance indices are from 0.9 to 1 even when we remove all the terms that occurs less than 0.1% in our sample. This short spread causes difficulties for most algorithms in identifying clusters.

Therefore, we choose Euclidean metric to calculate the distance matrix required for the clustering algorithm.

<a id="freq-analysis" class="anchor"></a>

## Word Frequency Analysis

![img]({{ site.baseurl }}/assets/word_frequency_distribution.png){: .img-responsive}

There are approximately 17000 unique words in the whole tweets text. As shown in the histogram, the distribution of word frequency is significantly skewed to the right, which means there are a lot of words that do not appear much. These less frequent words increase the dimensions of our problem; as a result, tweets are further from each other. We see these words as “noise” in our data, since they are probably not keywords which help categorize a tweet in any subtopic.Therefore, we decided to remove the words that appear less than 0.1%, which means on average they appear less than once in 1000 tweets.

<a id="algorithm" class="anchor"></a>

## The Algorithm

<!-- What were the other methods that we tried? -->

We try four different clustering algorithms on our data set and choose [agglomerative hierarchical clustering](http://en.wikipedia.org/wiki/Hierarchical_clustering) method due to two reasons:

1. We do not need to decide how many clusters we want before running the algorithm, which is advantageous since we don't know how many thematic threads there are in this sample.
2. The concept of hierarchical clustering is simple enough that we can understand and explain it to people, which wasn't true of many of the approaches we looked at, given our limited knowledge of network theory.

### Agglomerative Hierarchichal Clustering

In hierarchical clustering, each tweet starts out as its own cluster. At each step, the two closest clusters, based on the distance we calculated, are merged together to create a new cluster. Each new distance is calculated between the newly created cluster and every other cluster. We repeat this process until there is only one single cluster left, which includes every tweet in our data set. Therefore, if we have n tweets, then our algorithm has n-1 iterations of this process.

### The Output

![img]({{ site.baseurl }}/assets/hierarchical_dendrogram.png){: .img-responsive}

This dendrogram is a clustering map showing which clusters are combined at each step. Having this dendrogram, we can decide how many clusters we want to create by cutting the dendrogram horizontally. We decided to divide our tweets into 13 groups, which you can see in the red boxes in the graph; each is a group of tweets. We chose 13 in order to make the size of each cluster reasonable.
