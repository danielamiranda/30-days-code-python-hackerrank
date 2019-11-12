# Enter your code here. Read input from STDIN. Print output to STDOUT
# Date inputs
actual_date = str(input())
due_date = str(input())

# Days, months, and years
actual_day, actual_month, actual_year = [ int(i) for i in actual_date.split(' ')] 
due_day, due_month, due_year = [ int(i) for i in due_date.split(' ')]

# Fine
if actual_year > due_year:
    fine = 10000
elif actual_year < due_year:
    fine = 0
else:
    if actual_month > due_month:
        fine = 500*(actual_month-due_month)
    elif actual_month < due_month:
        fine = 0
    else:
        if actual_day > due_day:
            fine = 15*(actual_day-due_day)
        else:
            fine = 0

print(fine)