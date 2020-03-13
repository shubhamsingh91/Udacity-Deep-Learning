# Testing simple arrays in Python

import numpy as nm
#from array import *
import array as arr
import sys

# Declaring functions here- in the beginning of the code
def fun1(str1):
    print str1
    return

# step function
def step_fun(y):
    if (y>=0):
        out = 1
    else:
        out = 0
    return(out)

# declaring static array
arr1 = arr.array('f',[1,2,3,4,5,34.35])

for ii in range(0,6):
    arr1[ii] = arr1[ii]+1.23
    print(arr1[ii])

# declaring dynamic arrays
arr2 = []

for ii in range(0,10):
    var1 = ii*87.2
    arr2.append(var1) # append is used to add elements to the array

#print(arr2)
#print(sys.version)
# Calling function here
fun1("hola")

# dot product here using numpy function
a1 = [76 ,2.2]
b1 = [3.232 ,4.2]

c1 = nm.dot(a1,b1)
print(c1)

#------ Testing step function here-----------#

print(step_fun(-10.0))
