estudiantes = []

def agregar_estudiante():
    nombre = input("Ingrese el nombre del estudiante: ")
    edad = int(input("Ingrese la edad: "))
    notas = []
    id = int(input("Ingrese Id: "))
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

def mostrar_estudiante():
    if not estudiantes:
        print("No encuentro registro")
    else:
        print(estudiantes)

def pedir_notas():
    cantidad=[]
    return[float(input("Ingrese notas separada de comas: "))]

def actualizar_estudiantes():
    mostrar_estudiante()
    ingresar=input("Ingrese el id de estudiante a actualizar: ")
    ingresar == estudiantes
    print(input("Ingreso valido"))

def menu():
    while True:
        print("----- Sistema de Gestión de Estudiantes -----\n")
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
            mostrar_estudiante()
        elif opcion == "3":
            pedir_notas()
        elif opcion == "4"
            actualizar_estudiantes()
      