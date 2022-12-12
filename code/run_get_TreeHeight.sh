#!/bin/bash
# Author: Dashing Dingos
# Script: run_get_TreeHeight.sh
# Description: script to run get_treeheight script

if [ -z "$1" ]

then

  # use the default trees.csv file
  echo 'Input not found using default file: trees.csv'
  Rscript get_TreeHeight.R ../data/trees.csv
  #echo  "Running python script"
  #python3 get_TreeHeight.py ../data/trees.csv
  
else
  # if an argument is provided run 
  echo 'Input found, Running get_TreeHeight R script'
  Rscript get_TreeHeight.R $1
  #echo 'Running get_Treeheight.py'
  #python3 get_TreeHeight.py $1
fi