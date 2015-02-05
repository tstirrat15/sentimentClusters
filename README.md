# sentimentClusters

A tool for parsing tweets and finding semantic threads, using a combination of natural language processing and network-theoretic clustering algorithms.

## Authors:
Michael Christiansen, Thao Nguyen, Aldrin Barraquio, Tanner Stirrat

# Package Contents:

## R

### Package dependencies:

* [treemap](http://cran.r-project.org/web/packages/treemap/treemap.pdf)
* [stringR](http://cran.r-project.org/web/packages/stringr/stringr.pdf)
* [tm](http://cran.r-project.org/web/packages/tm/tm.pdf)
* [SnowballC](http://cran.r-project.org/web/packages/SnowballC/SnowballC.pdf)
* [devtools](http://cran.r-project.org/web/packages/devtools/devtools.pdf)

### Scripts:

#### combine.R:
    Description:	script to combine 2 data sets - August and November into 1 single data set.
    File inputs: tweets.Rdata, tweetsInd.Rdata
    File outputs: tweetsAll.rda
#### textMining.R
    Description:	script for natural language processing, creating tweets-vector data frame and frequency analysis
    File inputs: tweetsAll.rda
    File outputs: tweetsDF.rda
    Source code: func.R
#### distance.R
    Description:	script to calculate distance and cluster tweets
    File inputs: tweetsDF.rda
    File outputs: tweetsClus.rda
    Source code: func.R
#### func.R
    Description:	includes functions for textMining.R, distance.R and stackPlot.R
#### analysis.R
    Description: 	creates visualizations for the analysis
    File inputs: tweetsClus.rda
#### treemapanalysis.R
    Description: 	script to sort tweets into time zones and to construct a treemap
    File inputs: tweetsClus.rda
#### Split time.R
    Description:	script to parse created_at and create variables for stackPlot.R
    File inputs: tweetsClus.rda
#### stackPlot.R
	Description:	script to create stackplots
	File inputs: tweetsClus.rda, Split time.R
	Source code: func.R
