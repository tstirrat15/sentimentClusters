#install.packages("devtools")
library(devtools)
source(func.R)

############
#Make a stackplot of days of the month of Aug
# Make a table out of Score and Clusters
Scorez = table(tweetsClus$Score[tweetsClus$Score <= 30], tweetsClus$Cluster13[tweetsClus$Score <= 30])
# Make a streamplot of tweets per group per hour
plot.stacked(as.numeric(rownames((Scorez))), Scorez, center=TRUE, order.method="max", spar=0.3, frac.rand=0.2, main="Tweets per day", xlab="August, 2014", ylab="TWeets tweeted", 
             col=c("red","orange","yellow","green","cyan","blue","violet","purple","magenta","pink","brown","gray","black"))
legend("topright", c("General-Protest","Police Reform","Race","Arresting Journalists","Protest Call-to-action","National Guard","General-Incident","Tear Gas","Riot","Civil Progress","Indictment Decision","Darren Wilson","Flag Burning"), lwd=5,
       col=c("red","orange","yellow","green","cyan","blue","violet","purple","magenta","pink","brown","gray","black"))
ticks = 10:31
axis(side=1,at=ticks)
abline(v=14, lwd=2)
text(14,1800, 2, pos=2, labels="Obama addresses the Nation")
#######

#Make a stackplot of days of the month from Nov-Dec
# Make a table out of Score and Clusters
Scorex = table(tweetsClus$Score[tweetsClus$Score >= 92] - 92, tweetsClus$Cluster13[tweetsClus$Score >= 92] - 92)
# Make a streamplot of tweets per group per hour
plot.stacked(as.numeric(rownames((Scorex))), Scorex, center=TRUE, order.method="max", spar=0.3, frac.rand=0.2, main="Tweets per day", xlab="November, December, 2014", ylab="TWeets tweeted",
             col=c("red","orange","yellow","green","cyan","blue","violet","purple","magenta","pink","brown","gray","black"))         
#Add a line at x=24 to show when the grand jury made their indictment decision
abline(v=24, lwd=2)
#Add text line
text(24,1000, 2, pos=2, labels="Grand jury")
text(24,950, 2, pos=2, labels="decision made")
#Line for when Wilson resigned
abline(v=29, lwd=2)
text(29,1500, 2, pos=2, labels="Wilson")
text(29,1450, 2, pos=2, labels="resigns")
#Line for Hands Up Walk Out
abline(v=31, lwd=2)
text(31,1500, 2, pos=4, labels="Hands Up Walk Out")
#Add legend
legend("topleft", c("General-Protest","Police Reform","Race","Arresting Journalists","Protest Call-to-action","National Guard","General-Incident","Tear Gas","Riot","Civil Progress","Indictment Decision","Darren Wilson","Flag Burning"), lwd=5,
       col=c("red","orange","yellow","green","cyan","blue","violet","purple","magenta","pink","brown","gray","black"))
ticks = 10:40
axis(side=1,at=ticks)

########
#Tweets by hour stackplot
# Make a table out of hourx and clusters
hourz = table(tweetsClus$hourx, tweetsClus$Cluster13)
# Make a streamplot of tweets per group per hour
plot.stacked(as.numeric(rownames((hourz))), hourz, center=TRUE, order.method="max", spar=0.3, frac.rand=0.2, main="Tweets by hour", xlab="Hour of the day", ylab="TWeets tweeted",
             col=c("red","orange","yellow","green","cyan","blue","violet","purple","magenta","pink","brown","gray","black"))         
legend(0.5,1200, c("General-Protest","Police Reform","Race","Arresting Journalists","Protest Call-to-action","National Guard","General-Incident","Tear Gas","Riot","Civil Progress","Indictment Decision","Darren Wilson","Flag Burning"), lwd=5,
       col=c("red","orange","yellow","green","cyan","blue","violet","purple","magenta","pink","brown","gray","black"))


#########
#Stackplot showing how large each cluster is on each day of the week
#Make a table out of Dow and clusters
counts = table(tweetsClus$Dow, tweetsClus$Cluster13)
#Order the days of the week
ordered = rbind(counts["Mon",], counts["Tue",], counts["Wed",], counts["Thu",], counts["Fri",], counts["Sat",], counts["Sun",])
rownames(ordered) = c("Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun")

#Make a stackmplot of groups per Dow
plot(0,0, title(main="Tweets by day", xlab="Days Mon-Sun", ylab="Tweets tweeted"),)
plot.stacked(1:7, ordered, center=TRUE, order.method="max", spar=0.3, frac.rand=0.2, border="white", lwd=0.5, title(main="Tweets by day", xlab="Days Mon-Sun", ylab="Tweets tweeted"), 
             col=c("red","orange","yellow","green","cyan","blue","violet","purple","magenta","pink","brown","gray","black"))
