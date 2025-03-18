from datetime import datetime, timedelta

# 1. Obtener el día, mes, año, hora, minuto y marca de tiempo actual
now = datetime.now()
day = now.day
month = now.month
year = now.year
hour = now.hour
minute = now.minute
timestamp = now.timestamp()

print(f"1. Día: {day}, Mes: {month}, Año: {year}, Hora: {hour}, Minuto: {minute}")
print(f"   Marca de tiempo: {timestamp}\n")

# 2. Formatear la fecha actual con el formato "%m/%d/%Y, %H:%M:%S"
formatted_date = now.strftime("%m/%d/%Y, %H:%M:%S")
print(f"2. Fecha formateada: {formatted_date}\n")

# 3. Convertir la cadena "Hoy es 5 diciembre, 2019" a un objeto de tiempo
date_string = "5 December, 2019"
date_object = datetime.strptime(date_string, "%d %B, %Y")
print(f"3. Fecha convertida: {date_object}\n")

# 4. Calcular la diferencia horaria entre ahora y el año nuevo
new_year = datetime(now.year + 1, 1, 1)
time_difference_new_year = new_year - now
print(f"4. Diferencia hasta el año nuevo: {time_difference_new_year}\n")

# 5. Calcular la diferencia horaria entre el 1 de enero de 1970 y ahora
epoch = datetime(1970, 1, 1)
time_difference_epoch = now - epoch
print(f"5. Diferencia desde el 1 de enero de 1970: {time_difference_epoch}\n")

# 6. Ejemplo de uso del módulo datetime en un blog
blog_entry = {
    "title": "Mi primera entrada",
    "content": "Este es el contenido de mi primera entrada en el blog.",
    "timestamp": now
}
print(f"6. Ejemplo de uso en un blog:")
print(f"   Entrada creada el: {blog_entry['timestamp'].strftime('%Y-%m-%d %H:%M:%S')}")