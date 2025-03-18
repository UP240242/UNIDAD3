print(min(30,15,20))
print(max(30,15,20))
nu=(20,60,40,50)
suma=sum(nu,10)
print("el resultado es ",suma)

# Variables in Python
first_name = 'Guadalupe'
last_name = 'Macias Najera'
country = 'Mexico'
city = 'Aguascalientes'
age = 18
is_married = False
skills = ['HTML', 'CSS', 'JS','Python','C++']
person_info = {
   'firstname':'Guadalupe',
   'lastname':'Macias Najera',
   'country':'Mexico',
   'city':'Aguascalientes',
   'age': '18',
  ' is_married' : 'False',
   'skills' : ['HTML', 'CSS', 'JS','Python','C++']
  }
print(type(person_info))

first_name, last_name, country, age, is_married = 'Guadalupe', 'Macias Najera', 'Mexico', 18 , False

print(first_name, last_name, country, age, is_married)
print('First name:', first_name)
print('Last name: ', last_name)
print('Country: ', country)
print('Age: ', age)
print('Married: ', is_married)

first_name = input('What is your name: ')
age = input('How old are you? ')
print(first_name)
print(len(first_name))
print(age)

#ejercicio 1 


nombre = "guadalupe"
apellido = "macias "
nombre_completo = nombre + " " + apellido
pais = "México"
ciudad = "aguascalientes"
edad = 18
año = 2025
is_married = False
is_true = True
is_light_on = True

var1, var2, var3, var4 = 10, 20, "Python", False

#ejercicio 2

# Verificar los tipos de datos
print(type(nombre))
print(type(apellido))
print(type(nombre_completo))
print(type(pais))
print(type(ciudad))
print(type(edad))
print(type(año))
print(type(is_married))
print(type(is_true))
print(type(is_light_on))

print("Longitud del nombre:", len(nombre))

print("Diferencia de longitud:", len(nombre) - len(apellido))

num_one = 5
num_two = 4

total = num_one + num_two
diff = num_one - num_two
producto = num_one * num_two
division = num_one / num_two
resto = num_one % num_two
exp = num_one ** num_two
floor_division = num_one // num_two

print("Suma:", total)
print("Resta:", diff)
print("Multiplicación:", producto)
print("División:", division)
print("Módulo:", resto)
print("Exponenciación:", exp)
print("División de piso:", floor_division)

radio = 30
pi = 3.1416

area_of_circle = pi * radio**2
circum_of_circle = 2 * pi * radio

print("Área del círculo:", area_of_circle)
print("Circunferencia del círculo:", circum_of_circle)


radio_usuario = float(input("Ingresa el radio del círculo: "))
area_usuario = pi * radio_usuario**2
print("El área del círculo con radio", radio_usuario, "es:", area_usuario)


nombre_usuario = input("Ingresa tu nombre: ")
apellido_usuario = input("Ingresa tu apellido: ")
pais_usuario = input("Ingresa tu país: ")
edad_usuario = int(input("Ingresa tu edad: "))

print("Nombre:", nombre_usuario)
print("Apellido:", apellido_usuario)
print("País:", pais_usuario)
print("Edad:", edad_usuario)

help('keywords')
