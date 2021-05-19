salary = input("Ingresa tu salario: ") #Don't forget to clear prompt
salary = float(salary)
expenses = {"Alimentos":0.2, "Pasajes":0.15, "Cine": 0.1, "Libros":0.15, "Arriendo":0.0}
expenses["Arriendo"] = 1-expenses["Alimentos"]-expenses["Pasajes"]-expenses["Cine"]-expenses["Libros"]
new_salary = salary*expenses["Arriendo"]
new_salary = round(new_salary,2)
print("Tu salario restante es: $ ", new_salary)