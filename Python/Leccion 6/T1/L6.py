class vehiculo():
    def __init__(self):
        self.color = "rojo"

        self.ruedas = 4

        self.puertas = 2
        
        
class coche(vehiculo):
    def __init__(self):
        super().__init__()
        self.velocidad = 80
        self.cilindrada = 4
        
tesla = coche()

print("El color del carro es:",tesla.color)
print("El carro tiene",tesla.ruedas, "ruedas")
print("El carro tiene:",tesla.puertas, "puertas")
print("La velocidad del carro es:",tesla.velocidad, "km/h")
print("La cilindrada del carro es:",tesla.cilindrada)
