from random import randint

# Logic basic
#print(3 <= 3) # Imprime True si 3 <= 3
#print(3 > 3) # Imprime false porque 3 no es mayor que 3
#print(3 != 3) # Imprime false porque 3 no es diferente de 3
#print("Juan" == "Solano") # Imprime false porque ambos strings son distintas
#print("Juan" == "Juan") # True
#print(3*8 == 6*4) # True
#print("jjjjj" == "j"*5) # True
#print(True > False) # True = 1 es mayor que False = 0
#print(True > False + 1) # False
#print(True >= False + 1) # True
#print(True == 1.0) # True
#print(True != "Juan") # True, son diferentes
#print(1 == "1") # False, tratar de comparar datos del mismo tipo
#print(True == "True") # False, tipos de datos distintos

# AND: Símil de multiplicación
#my_bool1 = True
#my_bool2 = True
#my_bool3 = False
#print(my_bool1, " AND ", my_bool2, " = ", my_bool1 and my_bool2)
#print(my_bool1, " AND ", my_bool2, " AND ", my_bool3, " = ", my_bool1 and my_bool2 and my_bool3)

# OR: Símil de multiplicación
#my_bool1 = True
#my_bool2 = True
#my_bool3 = False

#print(my_bool1 or my_bool2)
#print(my_bool1 or my_bool2 or my_bool3)
#print((my_bool3 and my_bool1) and (my_bool3 or my_bool1) or "jj" == "jj")

# XOR: Si A y B son distintas, es verdadero; Si A y B son iguales, es falso.

# NOT: Cambia el estado
#print(not True)

# Programa: Analiza si es positivo o negativo
#user_input = input("¿Qué número? ")
#if not user_input.lstrip("-").isdigit():
#    print(f"La variable '{user_input}' no es un número")
#else:
#    number = float(user_input)
#    
    # Condicional
#    if number == 0:
#        print(f"El número {number} es cero")
#    else:
#        if number > 0:
#            print(f"El número {number} es positivo")
#        else:
#            print(f"El número {number} es negativo")

# Programa: Lotería del 1 al 9
rand_number = randint(1,9)
user_input = input("Inserte un número del 1 al 9: ")

if not user_input.lstrip("-").isnumeric():
    print(f"La variable '{user_input}' no es un número")
else:
    number = float(user_input)
    
    if number == rand_number:
        print("¡Ganaste un iPhone!")
    else:
        print(f"Vuelve a intentarlo. El número ganador fue {rand_number}")
