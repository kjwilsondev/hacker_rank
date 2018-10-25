#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the plusMinus function below.
def plusMinus(arr):
    positive = 0.0
    negative = 0.0
    zero = 0.0
    length = len(arr)

    for number in arr:
        if number > 0:
            positive += 1
        elif number < 0:
            negative += 1
        elif number == 0:
            zero += 1

    # positive = float(positive/length)
    # negative = float(negative/length)
    # zero = float(zero/length)
    positive = str.format('{0:.6f}', float(positive/length))
    negative = str.format('{0:.6f}', float(negative/length))
    zero = str.format('{0:.6f}', float(zero/length))

    print(positive)
    print(negative)
    print(zero)
    # return positive, negative, zero

test_1 = [1, 1, -1, -1, 0]
test_2 = [2, -2, 5, -20, 3, 0]
test_3 = [0, 0, 0, 0, 0, 0, 0]
test_4 = [-20, -30, -40, -50, -100]
print("answer should be .4, .4, .2")
plusMinus(test_1)
print("answer should be .5, .333, .166")
plusMinus(test_2)
print("answer should be 0, 0, 1")
plusMinus(test_3)
print("answer should be 0, 1, 0")
plusMinus(test_4)

# if __name__ == '__main__':
#     n = int(input())
#
#     arr = list(map(int, input().rstrip().split()))
#
#     plusMinus(arr)
