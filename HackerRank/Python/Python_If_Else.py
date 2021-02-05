#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip())

result = "Weird"
if (n % 2 == 0) & (((n >= 2) & (n <= 5)) | (n > 20)):
    result = "Not Weird"
    
print(result)