#Escribir un programa que guarde en una variable el diccionario {'Euro':'€',
#'Dollar':'$', 'Yen':'¥'}, pregunte al usuario por una divisa y muestre su 
#símbolo o un mensaje de aviso si la divisa no está en el diccionario.

diccionario = {'Euro':'€','Dollar':'$', 'Yen':'¥'}
divisa_usuario = input("Introduzaca una divisa:")
if divisa_usuario in diccionario:
    print(f"El símbolo de {divisa_usuario} es {diccionario[divisa_usuario]}")
else:
    print("La divisa no está en el diccionario")
    