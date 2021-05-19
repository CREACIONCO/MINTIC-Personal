# Class of 2021-05-18. Offline exercises
from os import system,name

# Ejercicio #1
#n = int(input("Inserte un número entero entre 1 y 20: "))
#for i in range(1,n+1):
#    print(pow(i,3))

# Ejercicio #2
#user_input = str(input("PALABRAS PALÍNDROMAS\nEscriba una frase: "))
#phrase=user_input.replace(" ", "")
#phrase=phrase.upper()
#validator=False
#k=len(phrase)
#for i in range(0,k):
#    if phrase[i]==phrase[k-1]:
#        validator=True
#        k=k-1
#    else:
#        validator=False
#        break
#print(f"La frase '{user_input}' es palíndroma") if validator else print(f"La frase '{user_input}' NO es palíndroma")
#print(i,k,validator, phrase)

# Ejercicio #3
keep_going=True
while keep_going:
    sales=float(input("Amount of sales: "))
    comm_rate=float(input("Commision rate in % (i.e. 20): "))
    commission=sales*comm_rate/100
    print(f"Commission: $ {commission}\nTotal sales: $ {sales}")
    user_input=input("Do you want to continue? Y/N: ")
    if user_input.upper()=='N':
        keep_going=False
    else:
        keep_going=True
        system('cls' if name == 'nt' else 'clear')