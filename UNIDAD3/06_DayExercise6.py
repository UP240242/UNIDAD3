# ejercicio 1

tupla_vacia = ()

hermanas = ("Ana", "María", "Lucía")
hermanos = ("Carlos", "Javier", "Miguel")

todos_los_hermanos = hermanos + hermanas
print(todos_los_hermanos)

print(len(todos_los_hermanos))

familia_completa = todos_los_hermanos + ("Papá", "Mamá")
print(familia_completa)

# ejercicio 2

*solo_hermanos, padre, madre = familia_completa
print(solo_hermanos, padre, madre)

frutas = ("Manzana", "Banana", "Uva")
verduras = ("Zanahoria", "Lechuga", "Tomate")
productos_animales = ("Leche", "Queso", "Huevos")

alimentos = frutas + verduras + productos_animales
print(alimentos)

lista_alimentos = list(alimentos)
print(lista_alimentos)

elemento_medio = alimentos[len(alimentos)//2] if len(alimentos) % 2 != 0 else alimentos[len(alimentos)//2 - 1: len(alimentos)//2 + 1]
print(elemento_medio)

print(lista_alimentos[3:-3])

del alimentos

paises_nordicos = ('Dinamarca', 'Finlandia', 'Islandia', 'Noruega', 'Suecia')
print("Estonia" in paises_nordicos)
print("Islandia" in paises_nordicos)
