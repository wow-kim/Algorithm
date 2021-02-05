#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the plusMinus function below.
def plusMinus(arr):
    pos = len([a for a in arr if a>0])
    neg = len([a for a in arr if a<0])
    tot = len(arr)
    print(f"{pos/tot:.6f}")
    print(f"{neg/tot:.6f}")
    print(f"{(tot-pos-neg)/tot:.6f}")
        
    

if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
