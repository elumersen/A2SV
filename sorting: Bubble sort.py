#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countSwaps' function below.
#
# The function accepts INTEGER_ARRAY a as parameter.
#

def countSwaps(a):
    indexing_length= len(a)
    swap= 0
    for i in range(0, indexing_length-1):
        for j in range(0, indexing_length-1):
            if a[j]>a[j+1]:
                swap+=1
                a[j], a[j+1] = a[j+1], a[j]
    print("Array is sorted in "+ str(swap)+ " swaps.")
    print("First Element: "+ str(a[0]))
    print("Last Element: "+ str(a[-1]))
    # return a

if __name__ == '__main__':
    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    countSwaps(a)
