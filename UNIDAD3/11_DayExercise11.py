# Nivel 1

# Declarar una función que sume dos números
def add_two_numbers(a, b):
    return a + b

# Calcular el área de un círculo
def area_of_circle(r):
    import math
    return math.pi * r * r

# Sumar todos los números dados como argumentos
def add_all_nums(*args):
    if all(isinstance(i, (int, float)) for i in args):
        return sum(args)
    return "Todos los elementos deben ser números."

# Convertir grados Celsius a Fahrenheit
def convert_celsius_to_fahrenheit(c):
    return (c * 9/5) + 32

# Determinar la estación según el mes
def check_season(month):
    seasons = {
        'Otoño': ['Septiembre', 'Octubre', 'Noviembre'],
        'Invierno': ['Diciembre', 'Enero', 'Febrero'],
        'Primavera': ['Marzo', 'Abril', 'Mayo'],
        'Verano': ['Junio', 'Julio', 'Agosto']
    }
    for season, months in seasons.items():
        if month in months:
            return season
    return "Mes no válido"

# Calcular la pendiente de una ecuación lineal
def calculate_slope(x1, y1, x2, y2):
    return (y2 - y1) / (x2 - x1)

# Resolver una ecuación cuadrática
def solve_quadratic_eqn(a, b, c):
    import math
    discriminant = b**2 - 4*a*c
    if discriminant < 0:
        return "No hay soluciones reales"
    elif discriminant == 0:
        return -b / (2*a)
    else:
        root1 = (-b + math.sqrt(discriminant)) / (2*a)
        root2 = (-b - math.sqrt(discriminant)) / (2*a)
        return root1, root2

# Imprimir una lista
def print_list(lst):
    for item in lst:
        print(item)

# Invertir una lista
def reverse_list(lst):
    return lst[::-1]

# Convertir elementos de una lista a mayúsculas
def capitalize_list_items(lst):
    return [item.upper() for item in lst]

# Agregar un elemento a una lista
def add_item(lst, item):
    lst.append(item)
    return lst

# Eliminar un elemento de una lista
def remove_item(lst, item):
    if item in lst:
        lst.remove(item)
    return lst

# Sumar todos los números de un rango
def sum_of_numbers(n):
    return sum(range(n + 1))

# Sumar los números impares de un rango
def sum_of_odds(n):
    return sum(i for i in range(n + 1) if i % 2 != 0)

# Sumar los números pares de un rango
def sum_of_even(n):
    return sum(i for i in range(n + 1) if i % 2 == 0)

# Nivel 2

# Contar números pares e impares en un rango
def evens_and_odds(n):
    evens = sum(1 for i in range(n + 1) if i % 2 == 0)
    odds = sum(1 for i in range(n + 1) if i % 2 != 0)
    return f"The number of evens are {evens}. The number of odds are {odds}."

# Calcular el factorial de un número
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)

# Verificar si un parámetro está vacío
def is_empty(param):
    return not bool(param)

# Calcular estadísticas de una lista de números
def calculate_mean(lst):
    return sum(lst) / len(lst)

def calculate_median(lst):
    lst.sort()
    n = len(lst)
    mid = n // 2
    return (lst[mid] if n % 2 != 0 else (lst[mid - 1] + lst[mid]) / 2)

def calculate_mode(lst):
    from collections import Counter
    return Counter(lst).most_common(1)[0][0]

def calculate_range(lst):
    return max(lst) - min(lst)

def calculate_variance(lst):
    mean = calculate_mean(lst)
    return sum((x - mean) ** 2 for x in lst) / len(lst)

def calculate_std(lst):
    import math
    return math.sqrt(calculate_variance(lst))

# Nivel 3

# Verificar si un número es primo
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

# Verificar si todos los elementos de una lista son únicos
def all_unique(lst):
    return len(lst) == len(set(lst))

# Verificar si todos los elementos de una lista son del mismo tipo
def same_data_type(lst):
    return all(isinstance(i, type(lst[0])) for i in lst)

# Verificar si una variable es válida en Python
def is_valid_variable(var):
    import keyword
    return var.isidentifier() and not keyword.iskeyword(var)

# Encontrar los idiomas más hablados (ejemplo ficticio)
def most_spoken_languages(n=10):
    language_counts = {'Inglés': 1500, 'Español': 500, 'Francés': 280, 'Chino': 1200, 'Arabe': 600}
    return sorted(language_counts.items(), key=lambda x: x[1], reverse=True)[:n]

# Encontrar los países más poblados (ejemplo ficticio)
def most_populated_countries(n=10):
    country_population = {'China': 1400, 'India': 1380, 'EEUU': 330, 'Indonesia': 270, 'Brasil': 212}
    return sorted(country_population.items(), key=lambda x: x[1], reverse=True)[:n]
