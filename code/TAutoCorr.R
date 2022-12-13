# start the script
rm(list=ls())

# input the data
AnnualT = load("../data/KeyWestAnnualMeanTemperature.RData")

#  split the data by time series
t1 = ats[1:99,2]
t2 = ats[2:100,2]

standard = cor(t1, t2)

#randomly sampled the function and measured its correlation
CorAnnualT <- function(x, y){
  sample1 = sample(x, length(x))
  sample2 = sample(y, length(y))
  cor_T = cor(sample1, sample2)
  return(cor_T)
}

#vectorize the function
cor_v = sapply(1:10000,function(i) CorAnnualT(t1, t2))

# plotting
pdf("../results/TAuto.pdf")
plot(density(cor_v), main = "")
abline(v = standard, col = "blue")
dev.off()

# compare with standard
length(cor_v[cor_v>standard])/length(cor_v)
length(cor_v[cor_v>standard])