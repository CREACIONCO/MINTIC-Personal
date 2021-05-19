# Reto de la semana 3

#import json
#productos = json.loads(input())

productos = [
    {'sku': 1, 'fecha_expiracion': '', 'precio': 423.646, 'descuento': 0},
    {'sku': 2, 'fecha_expiracion': '', 'precio': 45.117, 'descuento': 24},
    {'sku': 3, 'fecha_expiracion': 'hoy', 'precio': 485.603, 'descuento': 0}
]

def nueva_compra(productos):
    subtotal = 0    # Declaración y reseteo de variable
    
    # Inspección por índice de la lista de productos
    for i in range(0,len(productos)):
        # Si vence hoy, se le aplica 20% de descuento
        if productos[i]["fecha_expiracion"]=="hoy":
            productos[i]["descuento"]=productos[i]["descuento"]+20
        # Sumatoria del subtotal con el precio del producto - descuento
        subtotal = subtotal + productos[i]["precio"]*(1-productos[i]["descuento"]/100)
    return subtotal
# Fin de función

total = nueva_compra(productos)     # Guarda el resultado de la nueva compra en el total
print("Total = ",round(total, 2))   # Redondea el total y lo imprime