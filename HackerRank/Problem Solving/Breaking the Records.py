#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the breakingRecords function below.
def breakingRecords(scores):
    
    b, w = 0, 0
    best, worst = scores[0], scores[0]
    for score in scores[1:]:
        if score > best:
            best = score
            b += 1
        
        if score < worst:
            worst = score
            w += 1
    
    return [b, w]

    
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
