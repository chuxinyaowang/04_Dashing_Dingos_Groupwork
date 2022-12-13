#!/usr/bin/env python3


###File Input###
#Take ".csv" as an example.
#I pre-saved two sequences in a .csv file called testseq.csv in week2/sanbox
import sys


def main(argv):
    #import module
    
    import csv
    import pickle
#open csv and input
    
    with open('../data/testseq.csv','r') as f:
        csvwrite=csv.reader(f)
#input first two lines of sequences from csv
        rows=[row[0] for row in csvwrite]
    seq1=rows[0]
    seq2=rows[1]

            
    print("Two sequences are: ", seq1)
    print("                   ", seq2)

# Assign the longer sequence s1, and the shorter to s2
# l1 is length of the longest, l2 that of the shortest
    l1 = len(seq1)
    l2 = len(seq2)
    if l1 >= l2:
        s1 = seq1
        s2 = seq2
    else:
        s1 = seq2
        s2 = seq1
        l1, l2 = l2, l1 # swap the two lengths

# A function that computes a score by returning the number of matches starting
# from arbitrary startpoint (chosen by user)
    def calculate_score(s1, s2, l1, l2, startpoint):
        matched = "" # to hold string displaying alignements
        score = 0
        for i in range(l2):
            if (i + startpoint) < l1:
                if s1[i + startpoint] == s2[i]: # if the bases match
                    matched = matched + "*"
                    score = score + 1
                else:
                    matched = matched + "-"

    # some formatted output
    #print("." * startpoint + matched)           
    #print("." * startpoint + s2)
    #print(s1)
    #print(score) 
    #print(" ")

        return score

# Test the function with some example starting points:
# calculate_score(s1, s2, l1, l2, 0)
# calculate_score(s1, s2, l1, l2, 1)
# calculate_score(s1, s2, l1, l2, 5)

# now try to find the best match (highest score) for the two sequences
    my_best_align = None
    my_best_score = -1
#create a list to store alignment scores
    z=[]
    bestalign=[]
    for i in range(l1): # Note that you just take the last alignment with the highest score 
        z.append(calculate_score(s1, s2, l1, l2, i))
        max=z[0] #to find the max score within list z, and it's z[i]
        if z[i] > max:
            max=z[i]

    #z.sort(reverse=True)
        if z[i] == max:
            my_best_align = "." * i + s2  #print any alignments that scores = max
            my_best_score = z[i]
            bestalign.append(my_best_align) #store best alignments in to it
            #print(my_best_align)
            #print(s1)
            #print("Best score:", my_best_score)
            with open(r"../results/best_align.txt", "wb") as f: #use pickle to store it
                pickle.dump(bestalign, f)
    print("Best alignment has been saved! And they are:")
    with open(r"../results/best_align.txt", "rb") as f:
        print(pickle.load(f))
                
if (__name__ == "__main__"):
    status = main(sys.argv)


