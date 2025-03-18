# Crear un diccionario vacío llamado dog
dog = {}

# Agregar nombre, color, raza, patas y edad al diccionario dog
dog['name'] = 'Buddy'
dog['color'] = 'Brown'
dog['breed'] = 'Labrador'
dog['legs'] = 4
dog['age'] = 5

# Crear un diccionario de estudiante con las claves especificadas
student = {
    'first_name': 'John',  # Primer nombre
    'last_name': 'Doe',  # Apellido
    'gender': 'Male',  # Género
    'age': 21,  # Edad
    'marital_status': 'Single',  # Estado civil
    'skills': ['Python', 'Java'],  # Habilidades
    'country': 'USA',  # País
    'city': 'New York',  # Ciudad
    'address': '123 Main St'  # Dirección
}

# Obtener la longitud del diccionario de estudiante
student_length = len(student)
print("Longitud del diccionario de estudiante:", student_length)

# Obtener el valor de skills y verificar su tipo de dato
skills = student['skills']
print("Habilidades:", skills)
print("Tipo de habilidades:", type(skills))

# Modificar los valores de skills agregando una o dos habilidades
student['skills'].extend(['C++', 'JavaScript'])
print("Habilidades actualizadas:", student['skills'])

# Obtener las claves del diccionario como una lista
keys_list = list(student.keys())
print("Claves del diccionario:", keys_list)

# Obtener los valores del diccionario como una lista
values_list = list(student.values())
print("Valores del diccionario:", values_list)

# Convertir el diccionario en una lista de tuplas usando el método items()
student_tuples = list(student.items())
print("Diccionario como lista de tuplas:", student_tuples)

# Eliminar uno de los elementos del diccionario
del student['marital_status']
print("Diccionario después de eliminar marital_status:", student)

# Eliminar uno de los diccionarios
del dog
# print(dog)  # Esto generaría un error ya que dog ya no existe
