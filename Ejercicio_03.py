"""
Escribir un programa que guarde en un diccionario los precios de los artículos
de la tabla, pregunte al usuario por un artículo, un número de unidades y 
muestre por pantalla el precio de esa cantidad de producto. Si el producto no 
está en el diccionario debe mostrar un mensaje informando de ello.

Producto   Precio
 Pan        1.40
 Huevos     2.30
 Cebolla    0.85
 Aceite     4.35

"""
precios_prdts = {"pan": 1.40, "huevos":2.30, "cebolla": 0.85, "aceite": 4.35}
articulo = input("Escriba un articulo: ")
unidades = float(input("Escriba las unidades de ese articulo: "))
if articulo in precios_prdts:
    precio = precios_prdts[articulo] * unidades
    print(f"el precio de los {unidades} productos elegidos es {precio:.2f}€")
else:
    print("El producto no está en la lista :(")
    