from functools import reduce

def filtro(x):
    return x % 2
def suma(a,b):
    return a + b

def solucion(lista): 
    resultado = list(filter(filtro, lista)) 
    print(resultado)
    resultado = reduce(suma, resultado) 
    print(resultado)

lista = list(range(100))

solucion(lista)
