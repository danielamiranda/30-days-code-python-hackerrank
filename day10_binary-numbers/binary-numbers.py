#!/bin/python3

import math
import os
import random
import re
import sys


if __name__ == '__main__':
    n = int(input())
    n_bin = ''

    while n > 1:
        mod = n%2
        n_bin += str(mod)
        n = int(n/2)
    
    if n == 1:
        n_bin += str(1)

one_chunks = n_bin.split('0')
print(max(map(len,one_chunks)))