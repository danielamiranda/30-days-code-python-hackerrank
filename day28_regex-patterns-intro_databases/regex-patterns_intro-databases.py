#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    N = int(input())

    names_gmail = []

    for N_itr in range(N):
        firstNameEmailID = input().split()

        firstName = firstNameEmailID[0]

        emailID = firstNameEmailID[1]
        x = re.search(r'[a-z0-9]+@gmail\.com$', emailID)
        if x:
            names_gmail.append(firstName)
    
    names_gmail = sorted(names_gmail)
    for n in names_gmail:
        print(n)
