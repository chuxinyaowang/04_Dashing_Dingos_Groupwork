#Author: Dashing Dingos
#Script: get_TreeHeight.R
#Created: Sep 2022
#Desc: Groupwork practical on tree height

rm(list=ls())

TreeHeight <- function(degrees, distance) {
  radians <- degrees * pi / 180
  height <- distance * tan(radians)
  
  return (height)
}

#if the command line length is 0
if (length( commandArgs(trailing = T) ) == 0 ){
  print("No files are inputted, using the default pathway. \n ../data/trees.csv ")
  fname = "../data/trees.csv"
} else {
  fname = commandArgs(trailing = T)[1]
}
#read the file
data <- read.csv(file = fname, header = TRUE)

#add TreeHeight.m
data$TreeHeight.m <- TreeHeight(data$Angle.degrees, data$Distance.m)

#get the base file name
fbase = tools::file_path_sans_ext(basename(fname))
#paste the base file name
writepath = paste("../results/", fbase, "_treeheights.csv", sep = "")

# save to results
print("Saving at ../results/trees_treeheights.csv...")
write.csv(data, writepath)
