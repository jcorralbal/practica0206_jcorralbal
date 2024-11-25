#Escribir un programa que pregunte al usuario su nombre, edad, dirección y 
#teléfono y lo guarde en un diccionario. Después debe mostrar por pantalla el
#mensaje “<nombre> tiene <edad> años, vive en <dirección> y su número de 
#teléfono es <teléfono>”

diccionario = {}
diccionario["nombre"] = input("Escribe tu nombre: ")
diccionario["edad"] = input("Escribe tu edad: ")
diccionario["dirección"] = input("Escribe tu dirección: ")
diccionario["teléfono"] = input("Escribe tu teléfono: ")

print(f"{diccionario['nombre']} tiene {diccionario['edad']} años, vive en"
       f"{diccionario['dirección']} y su número de teléfono es "
       f"{diccionario['teléfono']}")

