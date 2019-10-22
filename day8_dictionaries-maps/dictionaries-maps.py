# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
phone_book = {}

if n < 1 or n > 10**5:
    print('error, invalid number of entries')
else:
    for i in range(0,n):
        entry = str(input())
        name = entry.split(' ')[0]
        phone = entry.split(' ')[1]
        phone_book[name] = phone

while True:
    try:
        query = str(input())

        if query in phone_book:
            message = str(query)+'='+str(phone_book[query])
            print(message)
        else:
            print('Not found')
    except:
        break