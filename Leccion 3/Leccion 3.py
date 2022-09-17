peso =float(input("(kg) Cual es tu peso: "))
altura = float(input("(m) Cual es tu altura: ")) 

masaCorporal = peso / (altura**2)

masaCorporal = round(masaCorporal, 2)
print("Tu índice de masa corporal es:",masaCorporal)

