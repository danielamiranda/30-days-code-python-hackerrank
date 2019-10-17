#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    N = int(input())

    # constraint management
    if 1 <= N <= 100:
        message = 'error'

    # conditional tasks
    mod = N % 2
    if mod > 0:
        message = 'Weird'
    elif 2 <= N <= 5 or N > 20:
        message = 'Not Weird'
    elif 6 <= N <= 20:
        message = 'Weird'

    print(message)
         
