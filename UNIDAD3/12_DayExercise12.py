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