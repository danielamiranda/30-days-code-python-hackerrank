#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input())

    for i in range(1,11):
        message = '{} x {} = {}'.format(str(n), str(i), str(n*i))
        print(message)