#----------------------------------------------------------------------
# Author: Thao Nguyen
# Date Created: 2/2/2015
# Last Edited: 2/2/2015
# Code to create visualization for the analysis
#----------------------------------------------------------------------

#Analysis on retweet_count
load("tweetsClus.rda")
tweets <- tweetsClus[!is.na(tweetsClus$Cluster13),]

#Name each clusters
clusterName <- c("General-Protest","Police Reform","Race","Arresting Journalists","Protest Call-to-action",
                 "National Guard","General-Incident","Tear Gas","Riot","Civil Progress","Indictment Decision"
                 ,"Darren Wilson","Flag Burning")

names(retweetCounts) <- clusterName

#Number of Tweets per cluster - Bar graph
barplot(sumClus,horiz=TRUE,cex.names=0.7,cex.axis = 0.5
        main="Number of Tweets per Cluster",xlim=c(0,8000))
ticks = seq(0,8000,500)
axis(side = 1, at = ticks)

#Number of Tweets per cluster - Pie Charts
par(cex.lab=0.05)
perc <- table(tweets$Cluster13)/nrow(tweets)
roundedPerc <- round(perc*100)
lbs <- paste(paste(clusterName,roundedPerc),"%",sep="")
pie(perc,labels=lbs,main="Cluster Percentage of Total Tweets",col=rainbow(length(lbs)))

#Percentage of Retweets in each cluster
rt <- substr(tweets$text,1,2) == "RT"
tweets$rt <- rt
rtTab <- table(tweets$rt,tweets$Cluster13)[2,]
percRT <- rtTab/as.vector(table(tweets$Cluster13))
names(percRT) <- clusterName
par(las=2,mar=c(5,7,4,1))
barplot(percRT,horiz=TRUE,cex.names=0.7,main="Percentage of Retweets per Cluster")



