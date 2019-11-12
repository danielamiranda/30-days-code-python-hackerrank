#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        nk = input().split()

        n = int(nk[0])

        k = int(nk[1])

        results = []


        # Brute force solution with memory error in cases 2-3-4
        # for i in range(1,n+1):
        #     for j in range(i+1,n+1):
        #         bitwise_and = i&j
        #         if bitwise_and < k:
        #             results.append(bitwise_and)
        
        # print(max(results))

        print((k-1 if (k-1)|k <= n else k-2)\
        if k <= n\
        else (n-1) & -2)
