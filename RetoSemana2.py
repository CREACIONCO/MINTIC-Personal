#Reto de la semana 2

rubro = (0.5, 0.2, 0.15, 0.15)
notas = {"Examen":0,"Lecciones":0,"Tareas":0,"Prácticas":0}

notas["Examen"] = float(input("Ingrese la nota del examen: "))
notas["Lecciones"] = float(input("Ingrese la nota de las lecciones: "))
notas["Tareas"] = float(input("Ingrese la nota de las tareas: "))
notas["Prácticas"] = float(input("Ingrese la nota de las prácticas: "))

nota_final=notas["Examen"]*rubro[0]+notas["Lecciones"]*rubro[1]+notas["Tareas"]*rubro[2]+notas["Prácticas"]*rubro[3]

if nota_final >= 0 and nota_final <=5:
    if nota_final<=2:
        nota_cualitativa="E"
    elif nota_final <=3:
        nota_cualitativa="D"
    elif nota_final <=3.5:
        nota_cualitativa="C"
    elif nota_final <=4:
        nota_cualitativa="B"
    elif nota_final <=4.5:
        nota_cualitativa="B+"
    elif nota_final >4.5:
        nota_cualitativa="A"
else:
    print("Error")
    
print(nota_cualitativa)