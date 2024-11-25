"""
Escribir un programa que permita gestionar la base de datos de alumnado de un 
classroom. Los alumnos y alumnas se guardarán en una lista que almacena un 
diccionario para cada alumno/a en el que la clave de cada alumno/a será su NIF,
y el valor será otro diccionario con los datos del alumno/a (nombre, apellidos,
teléfono, correo, aprobado), donde aprobado tendrá el valor True si ha aprobado
el módulo. El programa debe preguntar al usuario por una opción del siguiente 
menú: (1) Añadir alumno/a, (2) Eliminar alumno/a, (3) Mostrar alumno/a, (4) 
Listar todo el alumnado, (5) Listar alumnado aprobado, (6) Terminar. En función
de la opción elegida el programa tendrá que hacer lo siguiente:
Preguntar los datos del alumno/a, crear un diccionario con los datos y añadirlo
a la base de datos.

Preguntar por el NIF del alumno/a y eliminar sus datos de la base de datos.
Preguntar por el NIF del alumno/a y mostrar sus datos.
Mostrar lista de todo el alumnado de la base de datos con su NIF y nombre.
Mostrar la lista del alumnado aprobado de la base de datos con su NIF y nombre.
Terminar el programa.

"""
menu = ""
alumnos = [{}]
aprobados = []

while True:
    menu = input("(1) Añadir alumno/a, (2) Eliminar alumno/a," 
                 "(3) Mostrar alumno/a, (4) Listar todo el alumnado,"
                 "(5) Listar alumnado aprobado, (6) Terminar: ")
    if menu == "1":
        print("***Añadir alumno/a***")
        dato_alumno = {}
        informacion = ("nombre", "apellidos", "telefono", "correo", "aprobado")
        nif = input("Dime tu NIF: ")
        
        if nif in alumnos[0]:
            print("El NIF ya existe en la base de datos.")
            continue
        for i in informacion:
            if i != "aprobado":
                dato_alumno[i] = input("Dime tu " + i + ": ")
            else:
                estado_aprobado = input("Dime si ha"
                                         "aprobado o no (si/no): ").lower()
                if estado_aprobado == "si":
                    dato_alumno[i] = True
                    aprobados.append(nif)
                else:
                    dato_alumno[i] = False
        alumnos[0][nif] = dato_alumno
        print("***AÑADIDO***")
    elif menu == "2":
        print("***Eliminar alumno/a***")
        nif = input("Dime el NIF que quieres borrar: ")
        if nif in alumnos[0]:
            alumnos[0].pop(nif)
            if nif in aprobados:
                aprobados.remove(nif)
            print("***Eliminado***")
        else:
            print("El NIF no se encuentra en la base de datos.")
    elif menu == "3":
        print("***Mostrar alumno/a***")
        nif = input("Dime el NIF que quieres mostrar: ")
        if nif in alumnos[0]:
            alumno = alumnos[0][nif]
            print(f"NIF: {nif}")
            for clave, valor in alumno.items():
                print(f"{clave.capitalize()}: {valor}")
        else:
            print("El NIF no se encuentra en la base de datos.")
    elif menu == "4":
        print("***Listar todo el alumnado***")
        if alumnos[0]:
            for nif, datos in alumnos[0].items():
                print(f"NIF: {nif}, Nombre: {datos['nombre']} {datos['apellidos']}")
        else:
            print("No hay alumnos/as en la base de datos.")
    elif menu == "5":
        print("***Listar alumnado aprobado***")
        if aprobados:
            for nif in aprobados:
                datos = alumnos[0][nif]
                print(f"NIF: {nif}, Nombre: {datos['nombre']} {datos['apellidos']}")
        else:
            print("No hay alumnos/as aprobados/as.")
    elif menu == "6":
        print("***Terminado***")
        break
    else:
        print("Opción no válida. Por favor, elige una opción del menú.")
        