#!/bin/python3

import math
import os
import random
import re
import sys

if __name__ == '__main__':
    s = input()

dic = {}
for a in s:
    dic[a] = dic.get(a, 0) + 1

top3 = sorted(dic.items(), key = lambda x : (-x[1], x[0]))[0:3]

for alphabet, num in top3:
    print(alphabet,num,sep=" ")
