# Nivel 1

# Iterar de 0 a 10 usando for y while
print("Iteración con for:")
for i in range(11):
    print(i)

i = 0
print("Iteración con while:")
while i <= 10:
    print(i)
    i += 1

# Iterar de 10 a 0 usando for y while
print("Iteración inversa con for:")
for i in range(10, -1, -1):
    print(i)

i = 10
print("Iteración inversa con while:")
while i >= 0:
    print(i)
    i -= 1

# Imprimir un triángulo de 7 niveles
for i in range(1, 8):
    print("#" * i)

# Imprimir un patrón de 8x8
for _ in range(8):
    print("# # # # # # # #")

# Imprimir una tabla de multiplicación
for i in range(11):
    print(f"{i} x {i} = {i * i}")

# Iterar sobre una lista e imprimir sus elementos
fruits = ['Python', 'Numpy', 'Pandas', 'Django', 'Flask']
for fruit in fruits:
    print(fruit)

# Imprimir números pares del 0 al 100
print("Números pares:")
for i in range(0, 101, 2):
    print(i)

# Imprimir números impares del 0 al 100
print("Números impares:")
for i in range(1, 101, 2):
    print(i)

# Nivel 2

# Sumar todos los números del 0 al 100
suma_total = sum(range(101))
print(f"La suma de todos los números es {suma_total}.")

# Sumar los números pares e impares del 0 al 100
suma_pares = sum(i for i in range(101) if i % 2 == 0)
suma_impares = sum(i for i in range(101) if i % 2 != 0)
print(f"La suma de todos los pares es {suma_pares}. Y la suma de todos los impares es {suma_impares}.")

# Nivel 3

# Extraer países que contengan la palabra "tierra"
countries = ['Argentina', 'Australia', 'Bolivia', 'Colombia', 'Tierra del Fuego', 'Finlandia', 'Groenlandia']
countries_with_land = [country for country in countries if 'tierra' in country.lower()]
print("Países con 'tierra':", countries_with_land)

# Invertir una lista de frutas
fruits = ['plátano', 'naranja', 'mango', 'limón']
fruits.reverse()
print("Lista de frutas invertida:", fruits)

# Contar el número total de idiomas en una lista de datos ficticia
languages = ['Inglés', 'Español', 'Francés', 'Inglés', 'Alemán', 'Chino', 'Español', 'Portugués']
total_languages = len(set(languages))
print("Número total de idiomas:", total_languages)

# Encontrar los 10 idiomas más hablados (datos ficticios)
language_counts = {'Inglés': 1500, 'Español': 500, 'Francés': 280, 'Chino': 1200, 'Árabe': 600, 'Hindi': 800, 'Portugués': 220, 'Bengalí': 270, 'Ruso': 260, 'Japonés': 125}
most_spoken_languages = sorted(language_counts.items(), key=lambda x: x[1], reverse=True)[:10]
print("Los 10 idiomas más hablados:", most_spoken_languages)

# Encontrar los 10 países más poblados (datos ficticios)
country_population = {'China': 1400, 'India': 1380, 'EEUU': 330, 'Indonesia': 270, 'Pakistán': 220, 'Brasil': 212, 'Nigeria': 206, 'Bangladesh': 165, 'Rusia': 144, 'México': 126}
most_populated_countries = sorted(country_population.items(), key=lambda x: x[1], reverse=True)[:10]
print("Los 10 países más poblados:", most_populated_countries)