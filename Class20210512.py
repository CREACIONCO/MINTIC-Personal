# Write a program that asks for the user for the month number
# Your script should print the corresponding month's name
#months = {1:"Januar", 2:"Februar", 3:"March", 4:"April", 5:"May", 6:"Juny", 7:"July", 8: "August", 9:"September", 10:"October", 11:"November", 12:"December"}
#month_number = int(input("Please insert a month number: "))
#if month_number in range(1,13):
#    print(months[month_number])
#else:
#    print("Please type a correct month number")


# HackerRank Challenge: https://www.hackerrank.com/challenges/write-a-function/problem?h_r=internal-search
print("Welcome to the leap year calculator!\n\n")
    
def is_leap(year):
    leap = False
    if not year%4:
        if not year%100:
            if not year%400:
                leap=True
            else:
                leap=False
        else:
            leap=True
    else:
        leap=False
    return leap

year = int(input("Please insert a valid year: "))
if is_leap(year):
    print(f"The year {year} is leap")
else:
    print(f"The year {year} isn't leap")
