#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the compareTriplets function below.
def compareTriplets(a, b):
    index = 0
    ascore = 0
    bscore = 0
    while index < 3:
        if a[index] > b[index]:
            ascore += 1
        elif b[index] > a[index]:
            bscore += 1
        index += 1
    score = [ascore, bscore]
    return score


# if __name__ == '__main__':
#     fptr = open(os.environ['OUTPUT_PATH'], 'w')
#
#     a = list(map(int, input().rstrip().split()))
#
#     b = list(map(int, input().rstrip().split()))
#
#     result = compareTriplets(a, b)
#
#     fptr.write(' '.join(map(str, result)))
#     fptr.write('\n')
#
#     fptr.close()
