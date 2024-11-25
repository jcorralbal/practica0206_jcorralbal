"""
Escribir un programa que cree un diccionario de traducción español-inglés. El
usuario introducirá las palabras en español e inglés separadas por dos puntos,
y cada par <palabra>:<traducción> separados por comas, hasta que el usuario
introduzca la palabra “terminar”. El programa debe crear un diccionario con
las palabras y sus traducciones. Después pedirá una frase en español y 
utilizará el diccionario para traducirla palabra a palabra. Si una palabra no
está en el diccionario debe dejarla sin traducir.
"""


dic_traduccion = {}
terminar = ""

while terminar != "terminar":   

    traduccion = input("Escriba la <palabra>:<traducción>: ")

    separar = traduccion.split(":")

    palabra = separar[0]
    palabra = palabra.replace(" ", "")

    traduccion = separar[1]
    traduccion = traduccion.replace(" ", "")

    dic_traduccion[palabra] = traduccion
    terminar = input("Escriba terminar para finalizar sino pulse enter: ")

print(dic_traduccion)

frase_esp = input("Escribe una palabra en Español para traducirla: ")
for i in frase_esp.split():
    if i in dic_traduccion:
        palabra_traducida = i.replace(i, dic_traduccion[i])
        print(palabra_traducida)
    else:
        print(i)
