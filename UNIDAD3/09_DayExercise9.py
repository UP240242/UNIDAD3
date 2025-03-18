# Nivel 1

# Solicitar la edad del usuario y evaluar si puede conducir
edad = int(input("Introduzca su edad: "))
if edad >= 18:
    print("Tiene la edad suficiente para conducir.")
else:
    print(f"Necesita esperar {18 - edad} años para poder conducir.")

# Comparar la edad del usuario con la nuestra
mi_edad = 25  # Puedes modificar esta edad
edad_usuario = int(input("Ingrese su edad: "))
diferencia = abs(mi_edad - edad_usuario)
if edad_usuario > mi_edad:
    print(f"Eres {diferencia} años mayor que yo.")
elif edad_usuario < mi_edad:
    print(f"Soy {diferencia} años mayor que tú.")
else:
    print("Tenemos la misma edad.")

# Comparar dos números introducidos por el usuario
a = int(input("Ingrese el primer número: "))
b = int(input("Ingrese el segundo número: "))
if a > b:
    print(f"{a} es mayor que {b}")
elif a < b:
    print(f"{a} es menor que {b}")
else:
    print(f"{a} es igual a {b}")

# Nivel 2

# Calificar estudiantes según su puntaje
puntaje = int(input("Ingrese la puntuación del estudiante: "))
if 80 <= puntaje <= 100:
    print("Calificación: A")
elif 70 <= puntaje < 80:
    print("Calificación: B")
elif 60 <= puntaje < 70:
    print("Calificación: C")
elif 50 <= puntaje < 60:
    print("Calificación: D")
else:
    print("Calificación: F")

# Determinar la estación del año según el mes ingresado
mes = input("Ingrese un mes: ").lower()
if mes in ["septiembre", "octubre", "noviembre"]:
    print("La estación es Otoño.")
elif mes in ["diciembre", "enero", "febrero"]:
    print("La estación es Invierno.")
elif mes in ["marzo", "abril", "mayo"]:
    print("La estación es Primavera.")
elif mes in ["junio", "julio", "agosto"]:
    print("La estación es Verano.")
else:
    print("Mes no válido.")

# Manejo de una lista de frutas
fruits = ['banana', 'orange', 'mango', 'lemon']
fruit = input("Ingrese una fruta: ").lower()
if fruit in fruits:
    print("Esa fruta ya existe en la lista.")
else:
    fruits.append(fruit)
    print("Lista actualizada de frutas:", fruits)

# Nivel 3

# Diccionario de persona
person = {
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_married': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
}

# Verificar si la clave 'skills' existe y mostrar la habilidad central
if 'skills' in person:
    middle_index = len(person['skills']) // 2
    print("Habilidad central:", person['skills'][middle_index])

# Verificar si la persona tiene la habilidad 'Python'
if 'skills' in person and 'Python' in person['skills']:
    print("La persona tiene la habilidad Python.")

# Determinar el tipo de desarrollador según las habilidades
skills_set = set(person['skills'])
if {'JavaScript', 'React'} == skills_set:
    print("Es un desarrollador Frontend.")
elif {'Node', 'Python', 'MongoDB'}.issubset(skills_set):
    print("Es un desarrollador Backend.")
elif {'React', 'Node', 'MongoDB'}.issubset(skills_set):
    print("Es un desarrollador Fullstack.")
else:
    print("Título desconocido.")

# Verificar si la persona está casada y vive en Finlandia
if person['is_married'] and person['country'] == 'Finland':
    print(f"{person['first_name']} {person['last_name']} vive en Finlandia. Está casado.")
