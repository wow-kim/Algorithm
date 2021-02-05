#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def diagonalDifference(arr):
    # Write your code here
    left_pointer = 0
    right_pointer = len(arr[0])-1
    left_sum = 0
    right_sum = 0
    for a in arr:
        left_sum += a[left_pointer]
        right_sum += a[right_pointer]
        left_pointer += 1
        right_pointer -= 1
    
    return abs(left_sum - right_sum)
        
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
