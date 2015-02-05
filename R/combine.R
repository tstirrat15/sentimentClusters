#--------------------------------------------------------------
# Author: Thao Nguyen
# Date created: 1/30/2015
# Last updated: 1/30/2015
# Combine 2 data sets in 1 big data set
#--------------------------------------------------------------

load("tweets.Rdata")
load("tweetsInd.Rdata")

#Combine 2 data sets
tweets$sample = "aug"
tweetsInd$sample = "indictment"
id <- (nrow(tweets)+1) : (nrow(tweets)+ nrow(tweetsInd))
tweetsInd$id <- id
tweetsAll <- rbind(tweets,tweetsInd)
save(tweetsAll,file="tweetsAll.rda")

