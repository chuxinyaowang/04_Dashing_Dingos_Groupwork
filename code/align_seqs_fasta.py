#!/usr/bin/env python3

#load packages
import sys



#To start the function:
def seq():
    """File Input"""
    print("Input your fasta file 1:")
    input_file1=input("../data/")
    print("Input your fasta file 2:")
    input_file2=input("../data/")
    #read the sequences line by line
    f1=open(input_file1, 'r')
    lines1=f1.readlines()
    f2=open(input_file2,'r')
    lines2=f2.readlines()
    ls1=[]
    ls2=[]
    #This is for deleting the info of sequences at line1 also "\n"
    for line in lines1:
        if not line.startswith('>'):
            ls1.append(line.replace('\n',''))
    f1.close
    #Same for another sequences
    for line in lines2:
        if not line.startswith('>'):
            ls2.append(line.replace('\n',''))
    f2.close

#make seq1&seq2 from lists to strings 
#to make it easier to align with this:
    seq1 = ''.join(ls1)
    seq2 = ''.join(ls1)


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
        l1, l2 = l2, l1 
        # swap the two lengths

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
    #import ipdb; ipdb.set_trace()
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

    for i in range(l1): # Note that you just take the last alignment with the highest score
        z = calculate_score(s1, s2, l1, l2, i)
        if z > my_best_score:
            my_best_align = "." * i + s2 
            # think about what this is doing!
            my_best_score = z 
    print("The highest score alignment is:")
    print("                             ", my_best_align)
    print("                             ", s1)
    print("And the best score is:", my_best_score)

def main(argv):
 seq()
if (__name__ == "__main__"):
    status = main(sys.argv)
    sys.exit(status)

