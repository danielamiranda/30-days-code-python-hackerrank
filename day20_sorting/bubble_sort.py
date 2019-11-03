#!/bin/python3

import sys

n = int(input().strip())
a = list(map(int, input().strip().split(' ')))
# Write Your Code Here

num_swaps = 0
is_sorted = False

while is_sorted==False:
    is_sorted = True

    for j in range(0,n-1):
        if a[j] > a[j+1]:
            a[j],a[j+1] = a[j+1],a[j]
            num_swaps += 1
            is_sorted = False


print('Array is sorted in '+ str(num_swaps) +' swaps.')
print('First Element: '+ str(a[0]))
print('Last Element: '+ str(a[-1]))