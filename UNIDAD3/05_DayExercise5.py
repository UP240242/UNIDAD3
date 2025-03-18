# ejercicios 1
empty_list = []

items = [1, 2, 3, 4, 5, 6]

print(len(items))

print(items[0], items[len(items)//2], items[-1])

mixed_data_types = ["TuNombre", 25, 1.75, "Soltero", "TuDireccion"]

it_companies = ["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]

print(it_companies)

print(len(it_companies))

print(it_companies[0], it_companies[len(it_companies)//2], it_companies[-1])

it_companies[0] = "Meta"
print(it_companies)

it_companies.append("Tesla")
print(it_companies)

it_companies.insert(len(it_companies)//2, "Samsung")
print(it_companies)

it_companies[1] = it_companies[1].upper()
print(it_companies)

print("#; ".join(it_companies))

print("Google" in it_companies)

it_companies.sort()
print(it_companies)

it_companies.reverse()
print(it_companies)

print(it_companies[:3])

print(it_companies[-3:])

del it_companies[len(it_companies)//2]
print(it_companies)

it_companies.pop(0)
print(it_companies)

del it_companies[len(it_companies)//2]
print(it_companies)

it_companies.pop()
print(it_companies)

it_companies.clear()
print(it_companies)

front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']
full_stack = front_end + back_end
print(full_stack)

full_stack.insert(full_stack.index("Redux") + 1, "Python")
full_stack.insert(full_stack.index("Python") + 1, "SQL")
print(full_stack)

# ejercicios 2

ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]

ages.sort()
print(ages[0], ages[-1])

ages.append(ages[0])
ages.append(ages[-1])
print(ages)

median = ages[len(ages)//2] if len(ages) % 2 != 0 else (ages[len(ages)//2 - 1] + ages[len(ages)//2]) / 2
print(median)

average = sum(ages) / len(ages)
print(average)

print(max(ages) - min(ages))

print(abs(min(ages) - average), abs(max(ages) - average))

countries = ['China', 'Rusia', 'Estados Unidos', 'Finlandia', 'Suecia', 'Noruega', 'Dinamarca']
print(countries[len(countries)//2])

half = len(countries) // 2
first_half = countries[:half + (len(countries) % 2)]
second_half = countries[half + (len(countries) % 2):]
print(first_half, second_half)

first, second, third, *scandinavian = countries
print(first, second, third, scandinavian)