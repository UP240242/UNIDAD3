from collections import Counter
import re

# Ejercicios: Nivel 1

# 1. Palabra más frecuente en el párrafo
paragraph = 'I love teaching. If you do not love teaching what else can you love. I love Python if you do not love something which can give you all the capabilities to develop an application what else can you love.'

# Limpiar el texto y dividirlo en palabras
words = re.findall(r'\b\w+\b', paragraph.lower())

# Contar la frecuencia de cada palabra
word_counts = Counter(words)

# Ordenar las palabras por frecuencia (de mayor a menor)
sorted_word_counts = sorted(word_counts.items(), key=lambda x: x[1], reverse=True)

print("1. Palabras más frecuentes:")
for word, count in sorted_word_counts:
    print(f"   ({count}, '{word}')")

# 2. Distancia entre las dos partículas más lejanas
text = "La posición de algunas partículas en el eje x horizontal es -12, -4, -3 y -1 en la dirección negativa, 0 en el origen, 4 y 8 en la dirección positiva."

# Extraer los números del texto
points = list(map(int, re.findall(r'-?\d+', text)))

# Ordenar los puntos
sorted_points = sorted(points)

# Calcular la distancia entre los dos puntos más lejanos
distance = sorted_points[-1] - sorted_points[0]

print("\n2. Distancia entre las dos partículas más lejanas:")
print(f"   Puntos: {sorted_points}")
print(f"   Distancia: {distance}")

# Ejercicios: Nivel 2

# 3. Identificar si una cadena es una variable de Python válida
def is_valid_variable(variable):
    # Expresión regular para validar una variable de Python
    pattern = r'^[a-zA-Z_][a-zA-Z0-9_]*$'
    return bool(re.match(pattern, variable))

print("\n3. Validación de variables de Python:")
print(f"   'first_name': {is_valid_variable('first_name')}") 
print(f"   'first-name': {is_valid_variable('first-name')}")  
print(f"   '1first_name': {is_valid_variable('1first_name')}") 
print(f"   'firstname': {is_valid_variable('firstname')}")   

# Ejercicios: Nivel 3

# 4. Limpiar texto y contar las tres palabras más frecuentes
sentence = '''%I $am@% a %tea@cher%, &and& I lo%#ve %tea@ching%;. There $is nothing; &as& mo@re rewarding as educa@ting &and& @emp%o@wering peo@ple. ;I found tea@ching m%o@re interesting tha@n any other %jo@bs. %Do@es thi%s mo@tivate yo@u to be a tea@cher!?'''

def clean_text(text):
    # Eliminar caracteres especiales y espacios adicionales
    cleaned_text = re.sub(r'[^a-zA-Z\s]', '', text)
    cleaned_text = re.sub(r'\s+', ' ', cleaned_text).strip()
    return cleaned_text

def most_frequent_words(text, n=3):
    # Dividir el texto en palabras
    words = text.lower().split()
    # Contar la frecuencia de cada palabra
    word_counts = Counter(words)
    # Obtener las n palabras más frecuentes
    return word_counts.most_common(n)

# Limpiar el texto
cleaned_text = clean_text(sentence)
print("\n4. Texto limpio:")
print(cleaned_text)

# Obtener las tres palabras más frecuentes
frequent_words = most_frequent_words(cleaned_text)
print("\n   Palabras más frecuentes:")
print(f"   {frequent_words}")