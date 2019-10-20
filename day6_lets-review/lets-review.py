# Enter your code here. Read input from STDIN. Print output to STDOUT

t = int(input())

for i in range (0,t):
    s = str(input())
    if 2 <= len(s) <= 10000:
        even_char = ''
        odd_char = ''
        for ind,j in enumerate(s):
            mod = ind % 2
            if mod == 0:
                even_char += str(j)
            else:
                odd_char += str(j)
        message = even_char+' '+odd_char
        print(message)
    else:
        print('error, length no valid')
