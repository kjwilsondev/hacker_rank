#!/bin/python3

import math
import os
import random
import re
import sys

write = sys.stdout.write

# Complete the diagonalDifference function below.
def diagonalDifference(arr):
    # short for number
    n = len(arr) - 1
    # short for count
    c = 0
    addend = 0
    a_sum = 0
    b_sum = 0
    sum = 0

    # First diagonal
    while c < n:
        print("add ")
        addend = arr[c][c]
        print(addend)
        print("then\n")
        a_sum += arr[c][c]
        c += 1

    print("the first sum is ")
    print(a_sum)
    print("\n")

    # short for count
    c = 0

    # Second diagonal
    while c < n:
        print("add ")
        addend = arr[n][c]
        print(addend)
        print("then\n")
        b_sum += arr[n][c]


    print("the second sum is ")
    print(b_sum)
    print("\n")

    # find absolute difference
    print("THE ABSOLUTE DIFFERENCE IS: ")
    sum = a_sum + b_sum
    ab_diff = abs(sum)
    print(ab_diff)

square = [[0, 1], [2, 3]]
cube = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]
tesseract = [[0, 1, 2, 3], [4, 5, 6, 7], [8, 9, 10, 11], [12, 13, 14, 15]]
print(square)
print("diagonals have a value of 3\n The abosolute difference should be zero\n")
print(diagonalDifference(square))
print(cube)
print("diagonals have a value of 12\n The abosolute difference should be zero\n")
print(diagonalDifference(cube))
print(tesseract)
print(" diagonals have a value of 30\n The abosolute difference should be zero\n")
print(diagonalDifference(tesseract))

# if __name__ == '__main__':
#     fptr = open(os.environ['OUTPUT_PATH'], 'w')
#
#     n = int(input())
#
#     arr = []
#
#     for _ in range(n):
#         arr.append(list(map(int, input().rstrip().split())))
#
#     result = diagonalDifference(arr)
#
#     fptr.write(str(result) + '\n')
#
#     fptr.close()
