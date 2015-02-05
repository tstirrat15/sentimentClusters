setwd("H:/twitter")
load("tweetsClus.rda")
library(stringr)
library(treemap)


#sort into time zone categories
combine <- c("America/Chicago" = "Central Time", "Central Time (US & Canada)" = "Central Time", 
              "America/Denver" = "Mountain Time", "Mountain Time (US & Canada)" = "Mountain Time",
              "America/Los_Angeles" = "Pacific Time", "Pacific Time (US & Canada)" = "Pacific Time",
              "Arizona" = "Pacific Time", "America/Detroit" = "Eastern Time", "America/New_York" = 
               "Eastern Time", "Eastern Time (US & Canada)" = "Eastern Time")
tweetsClus$ustimezones <- factor(combine[as.character(tweetsClus$user_time_zone)],
                                 levels = unique(unname(combine)))

#sort and rename clusters
combine <- c("1" = "General-Protest", "2" = "Police Reform", "3" = "Race", "4" = "Arresting Journalists",
              "5" = "Protest Call-to-Action", "6" = "National Guard", "7" = "General-Incident",
              "8" = "Tear Gas", "9" = "Riot", "10" = "Civil Progress", "11" = "Indictment Decision",
              "12" = "Darren Wilson", "13" = "Flag Burning")
tweetsClus$Cluster13 <- factor(combine[as.character(tweetsClus$Cluster13)], 
                               levels = unique(unname(combine)))

#construct a table with a frequency column
map <- table(tweetsClus$Cluster13, tweetsClus$ustimezones)
df <- as.data.frame(map)
colnames(df) <- c("Cluster13", "ustimezones", "freq")


#create a tree map showing frequency of tweets in a cluster within a time zone
treemap(df, index = c("ustimezones", "Cluster13"), vSize = "freq",
        vColor = "ustimezones", type = "categorical",
        title = "Frequency of Tweets by Time Zones", fontface.labels = 1, 
        fontsize.labels = 12, border.lwds = .08, position.legend = "none")