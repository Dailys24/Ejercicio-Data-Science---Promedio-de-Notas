#Ejercicio Data Science - Promedio de Notas

estudiantes = [
    {"nombre": "Ana", "notas": [6.5, 7.0, 5.8]},
    {"nombre": "Luis", "notas": [4.2, 5.1, 6.0]},
    {"nombre": "Sofia", "notas": [3.9, 4.0, 4.5]},
    {"nombre": "Francisca", "notas": [6.9, 6.8, 7.0]},
    {"nombre": "Maria", "notas": [5.5, 6.0, 5.9]},
    {"nombre": "Carlos", "notas": [4.0, 4.5, 3.8]},
    {"nombre": "Laura", "notas": [6.2, 6.5, 6.8]},
    {"nombre": "Javier", "notas": [5.0, 5.2, 5.4]},
    {"nombre": "Elena", "notas": [3.5, 4.0, 4.1]},
    {"nombre": "Diego", "notas": [2.0, 2.5, 3.2]},
    {"nombre": "Angelo", "notas": [7.0, 6.1, 6.3]},
    {"nombre": "Andres", "notas": [4.5, 4.2, 3.9]},
    {"nombre": "Valeria", "notas": [1.8, 4.7, 2.0]},
    {"nombre": "Juan", "notas": [5.1, 5.3, 5.0]},
    {"nombre": "Gabriela", "notas": [4.0, 4.3, 3.7]},
    {"nombre": "Nicolas Rosale", "notas": [5.0, 3.0, 4.0]},
    {"nombre": "Paula", "notas": [6.0, 6.5, 6.2]},
    {"nombre": "Ricardo", "notas": [4.8, 4.9, 5.1]},
    {"nombre": "Fernanda", "notas": [5.8, 2.3, 4.2]},
    {"nombre": "Jorge", "notas": [5.6, 5.5, 5.8]},
    {"nombre": "Natalia", "notas": [3.6, 4.0, 3.5]},
    {"nombre": "Hugo", "notas": [6.1, 3.2, 6.0]},
    {"nombre": "Camila", "notas": [6.4, 6.0, 6.5]},
    {"nombre": "Roberto", "notas": [5.2, 5.0, 5.3]},
    {"nombre": "Matia Lope", "notas": [4.1, 4.2, 4.0]},
    {"nombre": "Manuel", "notas": [5.8, 2.3, 4.2]}, 
    {"nombre": "Silvia", "notas": [6.7, 6.9, 7.0]},
    {"nombre": "Felipe", "notas": [5.3, 5.5, 5.2]},
    {"nombre": "Adriana", "notas": [3.8, 4.1, 3.9]},
    {"nombre": "Benjamin", "notas": [6.1, 3.2, 6.0]},
    {"nombre": "Lucia", "notas": [6.1, 6.3, 6.0]},
    {"nombre": "Victor", "notas": [4.9, 5.0, 4.8]},
    {"nombre": "Carolina", "notas": [4.9, 5.0, 4.8]}, 
]

# 1. Calcular promedio de notas
promedios = []

print("# Nombre y promedio de notas de cada estudiante:")
for i, estudiante in enumerate(estudiantes):
    nombre = estudiante["nombre"]
    notas = estudiante["notas"]
    promedio = sum(notas) / len(notas)
    promedios.append({"nombre": nombre, "promedio": promedio})
    print(f"{i+1}. {nombre}: {promedio:.1f}")

# 1. Calcular promedio más bajo y más alto
if promedios:
    promedio_mas_bajo = min(promedios, key=lambda x: x["promedio"])
    promedio_mas_alto = max(promedios, key=lambda x: x["promedio"])

# 2. Filtrar estudiantes que aprobaron (promedio >= 4.0)
estudiantes_aprobados = [promedio for promedio in promedios if promedio["promedio"] >= 4.0]

print(f"--------------------------------------------------------------")
print(f"#1 Promedio más bajo: {promedio_mas_bajo['nombre']} con {promedio_mas_bajo['promedio']:.1f}")
print(f"#1 Promedio más alto: {promedio_mas_alto['nombre']} con {promedio_mas_alto['promedio']:.1f}")
print(f"--------------------------------------------------------------")
print(f"#2 Estudiantes que aprobaron sus asignaturas: {len(estudiantes_aprobados)}")

# 3. Nota mas frecuente (moda) considerando todas las notas de todos los estudiantes.
todas = [nota for estudiante in estudiantes for nota in estudiante["notas"]]

moda = max(todas, key=lambda x: sum(1 for nota in todas if nota == x))
frecuencia = sum(1 for nota in todas if nota == moda)

# 4. Porcentaje de estudiantes con al menos una nota bajo 4.0.
total = len(estudiantes)
con_rojos = sum(1 for estudiante in estudiantes if any(nota < 4.0 for nota in estudiante["notas"]))
porcentaje = (con_rojos / total) * 100

print(f"--------------------------------------------------------------")
print(f"#3 La nota más frecuente es {moda} con {frecuencia} apariciones.")
print(f"--------------------------------------------------------------")
print(f"#4 Porcentaje de estudiantes con al menos una nota bajo 4.0: {porcentaje:.1f}%")
print(f"--------------------------------------------------------------")

# 5. listado ordenado (de mayor a menor) de los estudiantes según su promedio.

ranking_estudiantes = sorted(promedios, key=lambda x: x["promedio"], reverse=True)

print(f"#5 Listado ordenado de los estudiantes según su promedio (mayor a menor).")

for i, estudiante in enumerate(ranking_estudiantes):
    print(f"{i+1}. {estudiante['nombre']}: {estudiante['promedio']:.1f}")
