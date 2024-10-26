def obtener_numero_estudiantes():
    while True:
        try:
            num = int(input("Ingrese el número de estudiantes: "))
            if num > 0:
                return num
            else:
                print("Por favor, ingrese un número mayor a 0.")
        except ValueError:
            print("Valor no válido. Ingrese un número entero.")

def obtener_nombre_estudiante():
    nombre = input("Ingrese el nombre del estudiante: ")
    return nombre

def obtener_numero_asignaturas():
    while True:
        try:
            num = int(input("Ingrese el número de asignaturas: "))
            if num > 0:
                return num
            else:
                print("Por favor, ingrese un número mayor a 0.")
        except ValueError:
            print("Valor no válido. Ingrese un número entero.")

def obtener_calificaciones(num_asignaturas):
    calificaciones = []
    for i in range(num_asignaturas):
        while True:
            try:
                calificacion = float(input(f"Ingrese la calificación para la asignatura {i+1} (0-10): "))
                if 0 <= calificacion <= 10:
                    calificaciones.append(calificacion)
                    break
                else:
                    print("La calificación debe estar entre 0 y 10.")
            except ValueError:
                print("Valor no válido. Ingrese un número.")
    return calificaciones

def calcular_promedio(calificaciones):
    return sum(calificaciones) / len(calificaciones)

def determinar_estado(promedio):
    if promedio >= 6.0:
        return "Aprobado"
    else:
        return "Reprobado"

def imprimir_resumen(estudiantes):
    print("\n--- Resumen de Calificaciones ---")
    for estudiante in estudiantes:
        print(f"Nombre: {estudiante['nombre']}, Promedio: {estudiante['promedio']:.2f}, Estado: {estudiante['estado']}")
    print("\n--------------------------------")

num_estudiantes = obtener_numero_estudiantes()
estudiantes = []

for i in range(num_estudiantes):
    nombre = obtener_nombre_estudiante()
    num_asignaturas = obtener_numero_asignaturas()
    calificaciones = obtener_calificaciones(num_asignaturas)
    promedio = calcular_promedio(calificaciones)
    estado = determinar_estado(promedio)

    estudiantes.append({
        'nombre': nombre,
        'promedio': promedio,
        'estado': estado
    })

imprimir_resumen(estudiantes)
