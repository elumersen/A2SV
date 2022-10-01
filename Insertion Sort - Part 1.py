#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'insertionSort1' function below.
#
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY arr
#

def insertionSort1(n, arr):
     last_num= arr[-1]
     n = len(arr)
     for i in range(n-2, -1, -1):
        if last_num < arr[i]:
            arr[i+1]= arr[i]
        else:
            arr[i+1]=last_num
            for i in arr :
                print(i,end=" ")
            print()
            break
        
        for i in arr :
            print(i,end=" ")
        print()
            
     if(arr[0]>last_num):
        arr[0]=last_num
        for i in arr :
            print(i,end=" ")
        print()

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort1(n, arr)
