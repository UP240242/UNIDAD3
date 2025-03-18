
cadena1 = 'Thirty' + ' ' + 'Days' + ' ' + 'Of' + ' ' + 'Python'
print(cadena1)  

cadena2 = 'Coding' + ' ' + 'For' + ' ' + 'All'
print(cadena2)  

company = "Coding For All"
print(company)

print(len(company))

print(company.upper())

print(company.lower())

print(company.capitalize()) 
print(company.title()) 
print(company.swapcase()) 

print(company.split()[1:])

print(company.find('Coding')) 

print(company.replace('Coding', 'Python'))

company = company.replace('Coding', 'Python')
print(company)

print(company.split())

cadena = 'Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon'
print(cadena.split(', '))

print(company[0])

print(len(company) - 1)

print(company[10])


acronimo1 = ''.join([word[0] for word in 'Python For Everyone'.split()])
print(acronimo1) 

acronimo2 = ''.join([word[0] for word in 'Coding For All'.split()])
print(acronimo2) 

posicion_C = company.find('C')
if posicion_C != -1:
    print(f"La posición de 'C' es: {posicion_C}")
else:
    print("No se encontró la letra 'C' en la cadena.")
print('8======D')
posicion_F = company.find('F')
if posicion_F != -1:
    print(f"La posición de 'F' es: {posicion_F}")
else:
    print("No se encontró la letra 'F' en la cadena.")

print(company.rfind('l'))

oracion = 'No se puede terminar una oración con porque porque porque porque es una conjunción'
print(oracion.find('porque'))

print(oracion.rindex('porque'))

inicio = oracion.find('porque')
fin = oracion.rfind('porque') + len('porque')
print(oracion[inicio:fin])

print(company.startswith('Coding'))

print(company.endswith('All'))

print(' Coding For All '.strip())

print('30DaysOfPython'.isidentifier()) 
print('thirty_days_of_python'.isidentifier())  

bibliotecas = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
print('#'.join(bibliotecas))

print("I am enjoying this challenge.\nI just wonder what is next.")

print("\nguadalupe\t18\tmexico\taguascalientes")

radius = 10
area = 3.14 * radius ** 2
print(f"The area of a circle with radius {radius} is {area} meters square.")

print(f"8 + 6 = {8 + 6}")
print(f"8 - 6 = {8 - 6}")
print(f"8 * 6 = {8 * 6}")
print(f"8 / 6 = {8 / 6:.2f}")
print(f"8 % 6 = {8 % 6}")
print(f"8 // 6 = {8 // 6}")
print(f"8 ** 6 = {8 ** 6}")
