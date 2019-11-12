import math

# Enter your code here. Read input from STDIN. Print output to STDOUT
## Primality function
def primality(number):
    '''check if integer n is a prime'''

    # make sure number is a positive integer
    number = abs(int(number))

    

    # 0 and 1 are not primes
    if number < 2:
        return False

    # 2 is the only even prime number
    if number == 2: 
        return True    

    # all other even numbers are not primes
    if number % 2 == 0:
        return False

    # range starts with 3 and only needs to go up 
    # the square root of n for all odd numbers
    sq = math.floor(math.sqrt(number))
    for i in range(3, sq + 1, 2):
        if number % i == 0:
            return False
            break;
            
    return True

## Input
T = int(input())
n_list = []

for i in range(T):
    n=int(input())
    n_list.append(n)

for n in n_list:
    if primality(n):
        print('Prime')
    else:
        print('Not prime')
    

