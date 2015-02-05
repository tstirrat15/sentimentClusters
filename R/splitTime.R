###The time a tweet was made is currently grouped into a single category, created_at, which holds the day of the week,
#day of the month, and time in hours that the tweet was made in. Let's take that category and from there make more.
#install.packages("stringr")
library(stringr)

# create a vector for each variable
n <- nrow(tweetsClus)
Dow <- character(n)
Month <- character(n)
Dom <- numeric(n)
Hour <- character(n)

#Create a score for days since Aug, must add 30 or 31 to anything past a month
Score <- numeric(n)
for (i in 1:n) {
 tweetx <- unlist(str_split(tweetsClus$created_at[i], " "))
 tweetx <- gsub("\\s", "", tweetx)
 Month[i] <- tweetx[2]
 Dom[i] <- as.numeric(tweetx[3])
 Score[i] <- Dom[i]

 if(Month[i] == "Sep") {
   Score[i] = Score[i] + 31
 } else if(Month[i] == "Oct") {
   Score[i] = Score[i] + 61
 } else if(Month[i] == "Nov") {
   Score[i] = Score[i] + 92
 } else if(Month[i] == "Dec") {
   Score[i] = Score[i] + 122
 }
}
tweetsClus$Score = Score


# extract the variables from each tweet
for (i in 1:n) {
  tweetx <- unlist(str_split(tweetsClus$created_at[i], " "))
  tweetx <- gsub("\\s", "", tweetx)

  #splits the string into the aspects we want
  Dow[i] <- tweetx[1]
  Month[i] <- tweetx[2]
  Dom[i] <- as.numeric(tweetx[3])
  Hour[i] <- tweetx[4]
}
#Add new categories to the dataframe
tweetsClus$Dow = Dow
tweetsClus$Month = Month
tweetsClus$Dom = Dom
tweetsClus$Hour = Hour

##Take HH:MM:SS and get just HH so we can stackplot it
hourxx <- numeric(n)
for (i in 1:n) {
  hourx <- unlist(str_split(tweetsClus$Hour[i], ":"))
  hourx <- gsub(":", "", hourx)
  hourxx[i] <- as.numeric(hourx[1])
}
###Change hourx from utc to ET
for (i in 1:n) {
if(hourxx[i] < 6) {
  hourxx[i] = hourxx[i] + 24
}
hourxx[i] = hourxx[i] - 6
}
tweetsClus$hourx = hourxx



