#--------------------------------------------------------
# Author: Thao Nguyen
# Date Created: 1/24/2015
# Last Edited: 1/31/2015
# Functions required for Twitter Cluster Project
#--------------------------------------------------------

library(tm)
library(SnowballC)
cleantxt <- function(txt){
  #Function to clean & natural language processing
  #for a text Vector includes of many text documents
  #Create a corpus from tweets
  corpus = Corpus(VectorSource(txt))
  #Transform to lower characters
  corpus = tm_map(corpus, content_transformer(tolower))
  #Remove Punctuation from tweets
  corpus = tm_map(corpus, removePunctuation)
  #Remove Stop words and Ferguson tag
  corpus = tm_map(corpus, removeWords, c("ferguson", "rt", stopwords("SMART")))
  #Get Stem words
  corpus = tm_map(corpus, stemDocument)
  return (corpus)
}
docMat <- function(corpus,sparseFreq=0.999){
  #Create Document Term Matrix from corpus, remove sparse terms
  #Return a data frame
  frequencies = DocumentTermMatrix(corpus)
  #Remove sparse terms that appears less than 0.1% of the tweets
  sparse = removeSparseTerms(frequencies,sparseFreq)
  #Create a data frame
  tweetsSparse = as.data.frame(as.matrix(sparse))
  #Remove rows that have 0 word occurence
  countWords = apply(tweetsSparse,1,sum)
  tweetsSparse = tweetsSparse[countWords>0,]
  return (tweetsSparse)
}

topWords <- function(matrix,groups,num) {
  #Function, takes in group of document term (binary) matrix, and cluster labels
  #returns the top commonly used words in those clusters
  #num: how many words to show
  groupedwordFreq <- by(matrix,groups,FUN=colSums)
  top <- lapply(groupedwordFreq, function(x)(head(sort(x[which (x>0)],decreasing=TRUE),num)))
  return (top)
}
infoTree <- function(tree,distMatrix,numBranches=4,numTopWords=10){
  #Function to present analysis on a Hierarchical clusters
  group = cutree(tree,k = numBranches)
  topWords = topWords(distMatrix,group,numTopWords)
  numTweets = table(group)
  res = list(topWords,numTweets,group)
  names(res) = c("topWords","numTweets","subTrees")
  return (res)
}

fillVec <- function(vec,maxRow){
  #Function would take a named vector with missing id
  #return a vec with full id and fill missing values with NA
  groupFrame <- data.frame(group=vec, id = names(vec))
  groupCol <- merge(data.frame(id = 1:maxRow),groupFrame,all.x=TRUE)
  return (groupCol$group)
}
mergeClus <- function(frame,groupVec,colName) {
  #Return a data frame with group assign to each observations
  group = fillVec(groupVec,nrow(frame))
  newframe = cbind(group,frame)
  colnames(newframe)[1] = colName
  return(newframe)
}

#####

#Create the plot.stacked function
plot.stacked <- function(
  x, y,
  order.method = "as.is",
  ylab="", xlab="",
  border = NULL, lwd=1,
  col=rainbow(length(y[1,])),
  ylim=NULL,
  ...
){
  
  if(sum(y < 0) > 0) error("y cannot contain negative numbers")
  
  if(is.null(border)) border <- par("fg")
  border <- as.vector(matrix(border, nrow=ncol(y), ncol=1))
  col <- as.vector(matrix(col, nrow=ncol(y), ncol=1))
  lwd <- as.vector(matrix(lwd, nrow=ncol(y), ncol=1))
  
  if(order.method == "max") {
    ord <- order(apply(y, 2, which.max))
    y <- y[, ord]
    col <- col[ord]
    border <- border[ord]
  }

  if(order.method == "first") {
    ord <- order(apply(y, 2, function(x) min(which(r>0))))
    y <- y[, ord]
    col <- col[ord]
    border <- border[ord]
  }
  
  top.old <- rep(0,length(x))
  polys <- vector(mode="list", ncol(y))
  for(i in seq(polys)){
    top.new <- top.old + y[,i]
    polys[[i]] <- list(x=c(x, rev(x)), y=c(top.old, rev(top.new)))
    top.old <- top.new
  }
  
  if(is.null(ylim)) ylim <- range(sapply(polys, function(x) range(x$y, na.rm=TRUE)), na.rm=TRUE)
  plot(x,y[,1], ylab=ylab, xlab=xlab, ylim=ylim, t="n", ...)
  for(i in seq(polys)){
    polygon(polys[[i]], border=border[i], col=col[i], lwd=lwd[i])
  }
  
} 
