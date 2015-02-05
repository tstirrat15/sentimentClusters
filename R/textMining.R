#--------------------------------------------------------
# Author: Thao Nguyen
# Date Created: 1/30/2015
# Last Edited: 1/31/2015
# Bags-of-word & Natural Language Processing 
#--------------------------------------------------------
source("func.R")
load("tweetsAll.rda")

txt <- tweetsAll$cleaned_text
names(txt) <- tweetsAll$id

#Natural Language Processing
corpus <- cleantxt(txt)
#Create Document Term Matrix
tweetsDF <- docMat(corpus)
save(tweetsDF, file = "tweetsDF.rda")

#Word Frequency analysis
termMat <- as.data.frame(as.matrix(DocumentTermMatrix(corpus)) > 0)
wordCounts <- colSums(termMat) / nrow(tweetsAll) *100
wordFreq <- table(wordCounts)
freq_hist <- hist(wordCounts,xlim=c(0,1),breaks=1000,xlab="Word Frequency in %",main="Histogram of Word Frequency")

#Number of words will be removed
numSparseTerms <- sum(wordCounts < 0.1)
#Percentage of word removed
sparsePerc <- numSparseTerms / ncol(termMat)
