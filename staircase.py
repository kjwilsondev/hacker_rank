#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the staircase function below.
def staircase(n):
    c = 0
    while c < n:
        c += 1
        hashtags = "#" * c
        spaces = " " * (n - c)
        print(spaces + hashtags)

test_1 = 3
test_2 = 7
test_3 = 21
print(staircase(test_1))
print(staircase(test_2))
print(staircase(test_3))

# if __name__ == '__main__':
#     n = int(input())
#
#     staircase(n)
