# Nivel 1

import random

# Generar un ID de usuario aleatorio de 6 caracteres
def random_user_id():
    return ''.join(random.choices('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789', k=6))

# Generar múltiples IDs de usuario según la entrada del usuario
def user_id_gen_by_user():
    num_chars = int(input("Ingrese el número de caracteres: "))
    num_ids = int(input("Ingrese el número de IDs a generar: "))
    return [''.join(random.choices('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789', k=num_chars)) for _ in range(num_ids)]

# Generar un color RGB aleatorio
def rgb_color_gen():
    return f"rgb({random.randint(0,255)},{random.randint(0,255)},{random.randint(0,255)})"

# Nivel 2

# Generar una lista de colores hexadecimales
def list_of_hexa_colors(n):
    return [f"#{''.join(random.choices('0123456789abcdef', k=6))}" for _ in range(n)]

# Generar una lista de colores RGB
def list_of_rgb_colors(n):
    return [rgb_color_gen() for _ in range(n)]

# Generar colores en formato hexadecimal o RGB
def generate_colors(color_type, n):
    if color_type == 'hexa':
        return list_of_hexa_colors(n)
    elif color_type == 'rgb':
        return list_of_rgb_colors(n)
    else:
        return "Tipo de color no válido"

# Nivel 3

# Mezclar aleatoriamente los elementos de una lista
def shuffle_list(lst):
    random.shuffle(lst)
    return lst

# Generar una lista de 7 números aleatorios únicos en el rango de 0 a 9
def unique_random_numbers():
    return random.sample(range(10), 7)

# Filtrar solo los negativos y el cero en la lista
def filter_negative_and_zero(numbers):
    return [num for num in numbers if num <= 0]

# Aplanar una lista de listas de listas
def flatten_list(nested_list):
    return [item for sublist in nested_list for inner_list in sublist for item in inner_list]

# Crear una lista de tuplas siguiendo un patrón específico
def create_tuples():
    return [(i, 1, i**1, i**2, i**3, i**4, i**5) for i in range(11)]

# Transformar una lista de países a una estructura específica
def transform_countries(countries):
    return [[country.upper(), country[:3].upper(), city.upper()] for sublist in countries for country, city in sublist]

# Convertir una lista de países en una lista de diccionarios
def countries_to_dict(countries):
    return [{'country': country.upper(), 'city': city.upper()} for sublist in countries for country, city in sublist]

# Convertir una lista de nombres en una lista de cadenas concatenadas
def names_to_strings(names):
    return [f"{first} {last}" for sublist in names for first, last in sublist]

# Función lambda para calcular la pendiente de una ecuación lineal
calculate_slope = lambda x1, y1, x2, y2: (y2 - y1) / (x2 - x1) if x2 != x1 else None
