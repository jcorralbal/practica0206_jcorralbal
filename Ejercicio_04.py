"""
Escribir un programa que cree un diccionario vacío y lo vaya llenado con 
información sobre una persona (por ejemplo nombre, edad, sexo, teléfono, 
electrónico, etc.) que se le pida al usuario. Cada vez que se añada un nuevo 
dato debe imprimirse el contenido del diccionario.
"""
diccionario = {}
terminar = ""

while terminar != "fin":

    clave = input("Escribe un dato para agregar: ")
    valor = input("Escribe el valor del dato: ")
    diccionario[clave] = valor

    print(diccionario)

    terminar = input("Escriba fin si ha termindo sino pulse enter: ")
