df = read.csv("tags_counts_rank.csv")
library(ggplot2)
library(ggrepel)
ggplot(df[c(1:47),],aes(avg_rank,count,label=tag)) + geom_text_repel() + stat_smooth()
