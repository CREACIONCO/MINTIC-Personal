# Class 2021-05-13

# Determine if a student can access a government subsidy to access to school education. There are 3 requirements:
# 1. Must be more than 40km to the round of school
# 2. Have more than 2 brothers
# 3. Family income is lower than 1000 dollars.
#print("¡Bienvenido al sistema de subsidio educativo!\n")
#def subsidy(distance, brothers, income):
#    if distance > 40 and brothers > 2 and income >= 0 and income < 1000:
#        return True
#    else:
#        return False
#distance = int(input("¿A cuántos kilómetros vives de la escuela?: "))
#brothers = int(input("¿Cuántos hermanos tienes?: "))
#income = int(input("¿Cuánto gana tu familia anualmente?: "))
#if subsidy(distance, brothers, income):
#    print("\nEres beneficiario del subsidio.")
#else:
#    print("\nLo sentimos, no aplicas para el subsidio")

# Pooja would like to withdraw X $US from an ATM. The cash machine will only accept the transaction if X is a multiple of 5, and Pooja's account balance has enough cash to perform the withdrawal transaction (including bank charges). For each successful withdrawal the bank charges 0.50 $US. Calculate Pooja's account balance after an attempted transaction. 
#print("Welcome to Crypto Bank X!\n")
#withdraw=float(input("How much would you like to withdraw?: "))
#balance=float(input("What is your actual balance?: "))
#if not withdraw%5 and balance>=withdraw+0.5:
#    print(f"\nTRANSACTION SUMMARY:\n{balance}\n -{withdraw}\n -0.5\n")
#    balance=balance-withdraw-0.5
#    print(f"NEW BALANCE: {balance}")
#else:
#    print("You don't have enough balance")

# You enter a dark room and should choose one of two doors, identified by 1 and 2
# Door 1 contains a giant bear eating a cheese cake, Show this to the user and two options:
# 1. Take the cake --> The bear eats your face off, Good Job!
# 2. Scream at the bear --> The bear eats your legs off, Good Job!
# <hidden> If the user chooses another number --> Well doing, {option} is probably better. Bear runs away!
#
# Door 2 --> You stare into the endless abyss at Cthulhu's retina. Show three options with the message "What is your insanity"
# 1. Blueberries
# 2. Yellow Jacket clothespins
# 3. Understanding revolvers yelling melodies
#
# if choose option 1 or 2 --> Your body survives powered by a mind of jello
# if choose option 3 --> Good Job!
# if choose another option --> print "The insanity rots of your eyes into a pool of muck, Good Job!"
#
# If another door number is chosen is not 1 or 2 --> print "You stumble around and fall on a knife and die. Good Job!" 
print("Welcome to the Cthulhu's game. Pray to survive!\n")
print("You enter a dark room and should choose one of two doors:")
dark_room=input(" 1. Door One\n 2. Door Two\n Your option: ")

# ROOM ONE
if dark_room == "1":
    print("\nDoor 1 contains a giant bear eating a cheese cake. What will you do?")
    door1 = input(" 1. Take the cake\n 2. Scream at the bear\n Your option: ")
    if door1 == "1":
        print("The bear eats your face off, Good Job!")
    elif door1 == "2":
        print("The bear eats your legs off, Good Job!")
    else:
        print(f"Well doing, {door1} is probably better. Bear runs away!")

# ROOM TWO
elif dark_room == "2":
    print("\nYou stare into the endless abyss at Cthulhu's retina. What is your insanity?")
    door2 = input(" 1. Blueberries\n 2. Yellow Jacket clothespins\n 3. Understanding revolvers yelling melodies\n Your option: ")
    if door2=="1" or door2=="2":
        print("Your body survives powered by a mind of jello")
    elif door2=="3":
        print("Good Job!")
    else:
        print("The insanity rots of your eyes into a pool of muck, Good Job!")
else:
    print("You stumble around and fall on a knife and die. Good Job!")
