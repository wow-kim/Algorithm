#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'pickingNumbers' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#
def pickingNumbers(a):
    # Write your code here
    if min(a) == max(a):
        return len(a)
    
    num_dic = {}
    for num in range(min(a), max(a)+1):
        num_dic[num] = a.count(num)
    
    maximum = 0
    values = list(num_dic.values())
    for i in range(len(values)-1):
        maximum = max(maximum, values[i]+values[i+1])
    
    return maximum
        
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = pickingNumbers(a)

    fptr.write(str(result) + '\n')

    fptr.close()
