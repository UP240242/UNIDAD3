
it_companies = {"Google", "Apple", "Microsoft"}


longitud = len(it_companies)
print("Longitud del conjunto it_companies:", longitud)

it_companies.add("Twitter")
print("it_companies después de añadir Twitter:", it_companies)

it_companies.update({"Amazon", "Facebook", "Tesla"})
print("it_companies después de añadir varias empresas:", it_companies)

it_companies.remove("Facebook") 
print("it_companies después de eliminar Facebook:", it_companies)

# 5. ¿Cuál es la diferencia entre quitar y desechar?
# - .remove() elimina un elemento y lanza un error si no se encuentra.
# - .discard() elimina un elemento pero no lanza error si el elemento no existe.

it_companies.discard('Twitter')

#ejercicios 2

A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

union = A | B
print("Unión de A y B:", union)

interseccion = A & B
print("Intersección de A y B:", interseccion)

diferencia = A - B
print("Diferencia A - B:", diferencia)

diferencia_simetrica = A ^ B
print("Diferencia simétrica entre A y B:", diferencia_simetrica)

es_subconjunto = A <= B
print("¿Es A un subconjunto de B?", es_subconjunto)
#ejercicios 3

edades = [25, 30, 25, 20, 30, 30]

edades_set = set(edades)
print("Longitud de la lista de edades:", len(edades))
print("Longitud del conjunto de edades:", len(edades_set))


oracion = "Soy profesora y me encanta inspirar y enseñar a la gente"
palabras = oracion.split()  
palabras_unicas = set(palabras) 
print("Palabras únicas en la oración:", palabras_unicas)
print("Número de palabras únicas:", len(palabras_unicas))
print("hola")