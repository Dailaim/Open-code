
paises = input("Escribe una lista de paises separados por coma: ")
paises = paises.split(", ")
paises = set(paises)
paises = sorted(paises)
salida = ""

for pais in paises:
    if pais == paises[0]:
        salida += pais+ ","
        continue
    elif pais == paises[-1]:
        salida += " " + pais
        continue
    salida += " " + pais+ ","
    
print(salida)