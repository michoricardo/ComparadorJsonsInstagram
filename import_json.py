# Función para encontrar valores después de los dos puntos en una línea
def find_values(line):
    values = []
    in_value = False
    for word in line.split():
        if in_value:
            values.append(word.strip('",'))
            in_value = False
        if word.startswith('"value'):
            in_value = True
    return values

# Leer y analizar línea por línea en following.json
following_values = set()
with open('following.json', 'r') as following_file:
    for line in following_file:
        following_values.update(find_values(line))

# Leer y analizar línea por línea en followers.json
followers_values = set()
with open('followers.json', 'r') as followers_file:
    for line in followers_file:
        followers_values.update(find_values(line))

# Encontrar valores en following.json que no están en followers.json
unfollowed_values = following_values - followers_values

# Imprimir los resultados
print("---------------------------------------------------")
print("---------------------------------------------------")
print("---------------------------------------------------")
print("---------------------------------------------------")
print("---------------------------------------------------")
print("---------------------------------------------------")
print("---------------------------------------------------")
print("---------------------------------------------------")
print("---------------------------------------------------")

print("Values en following.json pero no en followers.json:")
for value in unfollowed_values:
    print(value)
