#----------------------------------------------------------------------
# Author: Thao Nguyen
# Date Created: 1/30/2015
# Last Edited: 1/31/2015
# Calculate distance and cluster the data. Return a new data frame
# with the attached cluster result
#----------------------------------------------------------------------
source("func.R")
load("tweetsDF.rda")
tweetsDFBin <- as.matrix(tweetsDF >0)

#Calculate Euclidean distance
euDist <- dist(tweetsDFBin)
save(euDist,file="euDist.rda")

#Hierarchical Clustering
hCluster <- hclust(euDist,method="ward")
save(hCluster,file="hCluster.rda")

group5 <- infoTree(hCluster,tweetsDFBin,numBranches=5)
group11 <- infoTree(hCluster,tweetsDFBin,numBranches=11)
group13 <- infoTree(hCluster,tweetsDFBin,numBranches=13)

watchGroup = group13
watchGroup["numTweets"]
watchGroup["topWords"]

plot(hCluster,labels=FALSE,axes=FALSE,main="Hierarchical Cluster Dendrogram",ylab=NULL)
rect.hclust(hCluster,k=13)


#Append result to database
load("tweetsAll.rda")
tweetsClus <- mergeClus(tweetsAll, groupVec=group13[["subTrees"]], colName="Cluster13")
tweetsClus <- mergeClus(tweetsClus, groupVec=group5[["subTrees"]], colName="Cluster5")
save(tweetsClus,file="tweetsClus.rda")


