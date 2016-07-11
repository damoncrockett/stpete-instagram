df = read.csv("scores_all.csv")

library(ggplot2)

h = hist(df$value)
h$density = h$counts/sum(h$counts)*100
plot(h,freq=FALSE)

ggplot(df,aes(value)) + geom_histogram(color="grey75",fill="white",bins=50) + 
  theme(panel.background = element_rect(fill="grey25"),
        panel.grid.major = element_line(color="grey25"),
        panel.grid.minor = element_line(color="grey25"),
        plot.background = element_rect(fill="grey25"),
        legend.position="none",
        axis.text = element_text(size=rel(0.75),color="white"),
        text = element_text(color="white",size=25))

min(df$value)
max(df$value)
