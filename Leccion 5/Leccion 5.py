def bisiesto(agno):
    if agno%4 == 0:
        print(f"{agno} es bisiesto")
    else:
        print(f"{agno} no es bisiesto")
        
agno = int(input("Escrbe el año que quieres saber si es bisiesto: "))
bisiesto(agno)