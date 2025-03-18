from functools import reduce

# LISTAS PARA USO EN LOS EJEMPLOS
paises = ["Estonia", "Finlandia", "Suecia", "Dinamarca", "Noruega", "Islandia"]
nombres = ["Ana", "Juan", "Luis", "María"]
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# 1. USANDO UN BUCLE FOR PARA IMPRIMIR LISTAS
for pais in paises:
    print(pais)

for nombre in nombres:
    print(nombre)

for numero in numeros:
    print(numero)

# 2. USANDO MAP PARA MODIFICAR LISTAS
paises_mayus = list(map(str.upper, paises))
numeros_cuadrados = list(map(lambda x: x**2, numeros))
nombres_mayus = list(map(str.upper, nombres))

print(paises_mayus)
print(numeros_cuadrados)
print(nombres_mayus)

# 3. USANDO FILTER PARA FILTRAR ELEMENTOS
paises_tierra = list(filter(lambda p: "tierra" in p.lower(), paises))
paises_seis_letras = list(filter(lambda p: len(p) == 6, paises))
paises_largos = list(filter(lambda p: len(p) >= 6, paises))
paises_E = list(filter(lambda p: p.startswith("E"), paises))

print(paises_tierra)
print(paises_seis_letras)
print(paises_largos)
print(paises_E)

# 4. ENCADENANDO MAP, FILTER Y REDUCE
resultado = reduce(lambda x, y: x + y,
                   filter(lambda x: x > 10,
                          map(lambda x: x**2, numeros)))

print(resultado)

# 5. FUNCIÓN PARA EXTRAER SOLO ELEMENTOS DE TIPO STRING
def get_string_lists(lista):
    return list(filter(lambda x: isinstance(x, str), lista))

mi_lista = [1, "Hola", 3.5, "Mundo", True]
print(get_string_lists(mi_lista))

# 6. SUMAR TODOS LOS NÚMEROS USANDO REDUCE
suma_total = reduce(lambda x, y: x + y, numeros)
print(suma_total)

# 7. CONCATENAR TODOS LOS PAÍSES EN UNA ORACIÓN USANDO REDUCE
frase = reduce(lambda x, y: f"{x}, {y}", paises[:-1]) + f" y {paises[-1]} son países del norte de Europa."
print(frase)

# 8. FUNCIÓN PARA CATEGORIZAR PAÍSES SEGÚN UN PATRÓN
def categorize_countries(paises, patron):
    return list(filter(lambda p: patron in p.lower(), paises))

print(categorize_countries(paises, "land"))

# 9. CREAR UN DICCIONARIO CON LA CANTIDAD DE PAÍSES POR LETRA INICIAL
def contar_paises_por_letra(paises):
    resultado = {}
    for pais in paises:
        letra = pais[0]
        resultado[letra] = resultado.get(letra, 0) + 1
    return resultado

print(contar_paises_por_letra(paises))

# 10. OBTENER LOS PRIMEROS Y ÚLTIMOS DIEZ PAÍSES
def get_first_ten_countries(lista):
    return lista[:10]

def get_last_ten_countries(lista):
    return lista[-10:]

countries = ["Afganistán", "Albania", "Argelia", "Andorra", "Angola", "Argentina", "Armenia", "Australia", "Austria", "Azerbaiyán",
             "Bahamas", "Baréin", "Bangladés", "Barbados", "Bielorrusia", "Bélgica", "Belice", "Benín", "Bután", "Bolivia"]

print(get_first_ten_countries(countries))
print(get_last_ten_countries(countries))


#procesar_paises parte 3
from collections import Counter

from countries_dataset import countries
  # Importamos la lista de países desde el archivo countries_dataset.py
for country in countries:
    print(country["name"])  # Esto imprimirá el nombre de cada país



# 🔹 Ordenar países por nombre
def ordenar_paises_por_nombre():
    return sorted(countries, key=lambda x: x['name'])

# 🔹 Ordenar países por capital
def ordenar_paises_por_capital():
    return sorted(countries, key=lambda x: x.get('capital', ''))

# 🔹 Ordenar países por población (de mayor a menor)
def ordenar_paises_por_poblacion():
    return sorted(countries, key=lambda x: x['population'], reverse=True)

# 🔹 Obtener los 10 idiomas más hablados
def obtener_idiomas_mas_hablados():
    idiomas = []
    for pais in countries:
        idiomas.extend(pais['languages'])  
    return Counter(idiomas).most_common(10)

# 🔹 Función para obtener los 10 países más poblados
def obtener_paises_mas_poblados():
    return sorted(countries, key=lambda x: x['population'], reverse=True)[:10]

# 🔹 Ejecutar las funciones y mostrar los resultados
if __name__ == "__main__":
    print(" Países ordenados por nombre:")
    print([p['name'] for p in ordenar_paises_por_nombre()][:10])

    print("\n Países ordenados por capital:")
    print([p['capital'] for p in ordenar_paises_por_capital()][:10])

    print("\nPaíses ordenados por población:")
    print([(p['name'], p['population']) for p in ordenar_paises_por_poblacion()][:10])

    print("\n Los 10 idiomas más hablados:")
    for idioma, cantidad in obtener_idiomas_mas_hablados():
        print(f"{idioma}: {cantidad} países lo hablan")

    print("\n Los 10 países más poblados:")
    for pais in obtener_paises_mas_poblados():
        print(f"{pais['name']}: {pais['population']}")
