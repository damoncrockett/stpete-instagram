df = read.csv("hists.csv")
library(ggplot2)
library(reshape2)

DIR = "/Users/damoncrockett/Desktop/stpete/viz/hists/"
EXT = ".jpg"

for (t in df$tag) {
  filestring = paste(DIR,t,EXT,sep="")
  ggplot(melt(subset(df,df$tag==t)),aes(variable,value,group=tag)) + geom_line(color="grey50") + 
    theme(panel.background = element_rect(fill="white"),
          panel.grid.major = element_line(color="white"),
          panel.grid.minor = element_line(color="white"),
          plot.background = element_rect(fill="white"),
          legend.position="none",
          axis.ticks = element_blank(),
          axis.text = element_blank(),
          text = element_blank())
  ggsave(filename=filestring,width=0.5,height=0.5,units="in",dpi=300)
}