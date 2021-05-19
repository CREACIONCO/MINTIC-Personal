from math import pi, tan

# Sets
my_set = {True, "String", 2, "String 2"}
print (type(my_set), "-->",my_set)

# Lists
my_list = [True, -1,-3, 4, "String"]
print (type(my_list), "-->",my_list)
print("Posición N° 3: ",my_list[3])
my_list[4]=5.5
output = my_list[4]
print(output)

# Tuples
# Read more at https://docs.python.org/3/tutorial/datastructures.html 
my_tuple = (True, -1, -3.4, "string")
print (type(my_tuple), "-->",my_tuple)
print("Posición N° 1: ", my_tuple[1])

# Dictionary
my_dict = {"key-1":1, "key-2":True, "key-3":"Your name", "set":[1,2,3,4,5],"dict":{"One":1,"Two":2}}
print(type(my_dict), "-->",my_dict["key-3"])
print("Imrpimir arreglo dentro de dict: ", my_dict["set"][1])
print("Imrpimir dict dentro de dict: ", my_dict["dict"]["Two"])

# Functions
# Calculate the sume between two numbers
def sume_two_numbers(number_a, number_b):
    result = number_a + number_b
    print(f"The result is {result}")

a =4
b = 10
sume_two_numbers(a, b)

# Calc. the tangent of an angle
def tangent(angle):
    result=tan(angle)
    print(f"The result of the tangent is {result}")

tangent(float(input("Write an angle: ")))

# Logical operators AND, OR, NOT
# AND
input1 = True
input2 = True
input3 = True
print(input1 and input2 and input3)

# OR
input1 = False
input2 = False
input3 = False
print(input1 or input2 or input3)

# NOR
print(not(input1 or input2 or input3))

