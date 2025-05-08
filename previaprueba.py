print("SISTEMA GESTION ESTUDIANTIL")
print("___________________________________________________\n")

estudiantes = []

def agregar_estudiante():
    nombre = input("Ingrese el nombre del estudiante: ")
    edad = int(input("Ingrese la edad: "))
    notas = []
    for i in range(3):  
        nota = float(input(f"Ingrese la nota {i+1}: "))
        notas.append(nota)
    estudiante = {
        "nombre": nombre,
        "edad": edad,
        "notas": notas
    }
    estudiantes.append(estudiante)
    print("Estudiante agregado correctamente.\n")


def menu():
    while True:
        print("----- Sistema de Gestión de Estudiantes -----")
        print("1. Agregar estudiante")
        print("2. Mostrar estudiantes")
        print("3. Actualizar estudiante")
        print("4. Eliminar estudiante")
        print("5. Calcular promedio de notas")
        print("6. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            agregar_estudiante()
        elif opcion == "2":
            mostrar_estudiantes()
        elif opcion == "3":
            actualizar_estudiante()
        elif opcion == "4":
            eliminar_estudiante()
        elif opcion == "5":
            calcular_promedio()
        elif opcion == "6":
            print("Saliendo del sistema.")
            break
        else:
            print("Opción no válida. Intente de nuevo.\n")

menu()
    
