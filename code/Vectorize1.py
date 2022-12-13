"""Script demonstrating speed of using vectorisation when manipulating matrices"""

__appname__ = 'Vectorize1.py'
__author__ = 'Dashing Dogins'
__version__ = '0.0.1'
__license__ = "CMEE"

#preparation
import sys
import numpy as np
import time

#make a 1000*1000 random matrix
M = np.random.rand(1000, 1000)

#from Vec~1.R
def SumAllElements(M): 
    Dimensions = M.shape
    Tot = 0
    for i in range(0,Dimensions[1]):
        for j in range(0,Dimensions[2]):
            Tot = Tot + M[i,j]
    return (Tot)

#do time measurement
# 1:time the looping function
start = time.time()       
SumAllElements(M)
end = time.time()
Time_period = end - start
print("Python SumAllElements function: {}".format(Time_period))

#2:time the vectorized sum function.
start = time.time()
M.sum()
end = time.time()
Time_period2 = end - start
print("Python sum vectorised function: {}".format(Time_period2))
