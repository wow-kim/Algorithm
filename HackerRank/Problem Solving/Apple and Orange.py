#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countApplesAndOranges function below.
def countApplesAndOranges(s, t, a, b, apples, oranges):
    apples = list(map(lambda x: x+a, apples))
    oranges = list(map(lambda x: x+b, oranges))
    
    app = sum([1 for apple in apples if (apple >= s)&(apple <= t)])
    ora = sum([1 for orange in oranges if (orange >= s)&(orange <= t)])
    
    print(app)
    print(ora)

if __name__ == '__main__':
    st = input().split()

    s = int(st[0])

    t = int(st[1])

    ab = input().split()

    a = int(ab[0])

    b = int(ab[1])

    mn = input().split()

    m = int(mn[0])

    n = int(mn[1])

    apples = list(map(int, input().rstrip().split()))

    oranges = list(map(int, input().rstrip().split()))

    countApplesAndOranges(s, t, a, b, apples, oranges)
