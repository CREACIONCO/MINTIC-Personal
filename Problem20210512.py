# Exercise HackerRank https://www.hackerrank.com/challenges/py-if-else/problem
user_input = input("Please write an integer: ")
def check_input(user_input):
    if not user_input.lstrip("-").isnumeric():
        global numeric
        numeric=False
    else:
        numeric = True
check_input(user_input)
if numeric == True:
    number = int(user_input)
    if number < 1 or number > 100:
        print("The number isn't between 1 and 100.")
    elif number%2 == 1:
        print(f"The number {number} is odd. Weird.")
    elif number in range(2,6):
        print(f"The number {number} is even and between 2 and 5. Not Weird.")
    elif number in range(6, 21):
        print(f"The number {number} is even and between 6 and 20. Weird.")
    elif number > 20:
        print(f"The number {number} is even and greater than 20. Not Weird.")
    else:
        print(f"The number {number} is even but not in the list.")
else:
    print("You didn't type a number.")