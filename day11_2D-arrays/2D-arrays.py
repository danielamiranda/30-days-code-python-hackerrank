#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    sum_hg = []

    for row in range(0,4):
        for col in range(0,4):
            sum_rc = arr[row][col] + arr[row][col+1] + arr[row][col+2]+ \
            arr[row+1][col+1] + arr[row+2][col] + arr[row+2][col+1]+ \
            arr[row+2][col+2]

            sum_hg.append(sum_rc)
    
    print(max(sum_hg))