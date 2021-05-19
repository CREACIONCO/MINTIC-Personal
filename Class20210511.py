# Class 2021-05-11
user_input1 = input("Please write an email: ")
user_input2 = ""

def check_input(user_input1, user_input2):
    if not user_input1.lstrip("-").isnumeric() and not user_input2.lstrip("-").isnumeric():
        global numeric
        numeric=False
    else:
        numeric = True

check_input(user_input1, user_input2)

# Print if the number is equal or not to 5
#number = 5
#if number == 5:
#    print("The number is the same as 5")
#else:
#    print("The number is different as 5")
    
# Write a program that prints a divisible number by 5
#if numeric==True:
#    number = float(user_input)
#    number2 = 5.0
#    if number%number2 == 0:
#        print(f"The number {number} is divisible by 5")
#    else:
#        print(f"The number {number} isn't divisible by 5")
#else:
#    print(f"The var '{user_input}' is not a number")

# gender.upper() Pasa a mayúsculas / gender.lower() Pasa a minúsculas

# Write a program that checks the "@" of an email
if numeric == False:
    email=str(user_input1)
    gender=str(user_input2)
    if email=="" or gender=="":
        print("You didn't write an email or gender.")
    elif email.find("@")==-1:
        print(f"Your email {email} is invalid")
    elif gender.upper() == "M" or gender.upper() == "F":
        print(f"Your gender {gender} is invalid.")
    else:
        print(f"Your email {email} and gender {gender} is valid")
else:
    print(f"The field {user_input1} or {user_input2} only accepts a string")