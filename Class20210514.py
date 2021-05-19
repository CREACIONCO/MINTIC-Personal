#Class 2021-05-14

#my_str = "A,9,1,TT,ASA,123"
#my_str.split(",")
#def check_input(user_input):
#    if not user_input.lstrip("-").isnumeric():
#        return False
#    else:
#        return True
#user_input = input("Type a string in the following format: A, 1, 2:")
#user_input.split(",")
#if check_input(user_input[0])==True:
#    print(f"{user_input[0]} > {user_input[1]}") if check_input(user_input[1])==True and user_input[0]>user_input[1] else continue
#    print(f"{user_input[0]} < {user_input[1]}") if check_input(user_input[1])==True and user_input[0]<user_input[1]
#    elif check_input(user_input[1])==True and user_input[0]<user_input[1]:
#        print(f"{user_input[0]} < {user_input[1]}")
#    else:
#elif check_input(user_input[1])==True:
#    print(f"{user_input[1]} it's numeric")
#elif check_input(user_input[2])==True:
#    print(f"{user_input[2]} it's numeric")

# Using something called as the Internet, you have acquired a dictionary of N words of a forgotten language. Meanwhile, you also know K phrases used in modern languages. For each of the words of the forgotten language, your task is to determine whether the word is still in use in any of these K modern phrases or not.
# Words --> Max two words of a forgotten language
# Phrase --> Max 3 words of a modern language

words = [str(input("Type the first forgotten word: ")), str(input("Type the second forgotten word: "))]
modern_phrase = str(input("Type a modern phrase: "))

modern_phrase=modern_phrase.split(" ")
#print(modern_phrase[0],modern_phrase[1],modern_phrase[2]) #Debug
#print(words[0], words[1]) # Debug

if len(modern_phrase)>1 and len(modern_phrase)<=2:
    print(f"The word {words[0]} was found on the phrase!") if words[0]!="" and words[0] in modern_phrase else print(f"The first word was not found here.")
    print(f"The word {words[1]} was found on the phrase!") if words[1]!="" and words[1] in modern_phrase else print(f"The second word was not found here.")
else:
    print("Error! Please write one or two words.")