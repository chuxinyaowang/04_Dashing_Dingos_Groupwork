""" Imports genus and species data, and outputs those that are Oaks to JustOaksData.csv"""

__appname__ = "oaks_debugme.py"
__author__ = "Dashing Dingos"
__version__ = "0.0.1"
__license__="CMEE"

#preparation
import csv
import sys
import doctest

#Define function
def is_an_oak(name):
    """ Returns True if name is starts with 'quercus' """
# only accepts quercus, filters out typos    
    return name.lower().split()[0] == "quercus"


def main(argv): 
    f = open('../Data/TestOaksData.csv','r')
    g = open('../Data/JustOaksData.csv','w')
    taxa = csv.reader(f)
    csvwrite = csv.writer(g)
    csvwrite.writerow(["Genus", "species"]) 

    next(taxa, None) # skips the header row

    oaks = set()
    for row in taxa:
        print(row)
        print ("The genus is: ") 
        print(row[0] + '\n')
        if is_an_oak(row[0]):
            print('FOUND AN OAK!\n')
            csvwrite.writerow([row[0], row[1]])  
        f.close()
        g.close()
    return 0
    
if (__name__ == "__main__"):
    status = main(sys.argv)

doctest.testmod()