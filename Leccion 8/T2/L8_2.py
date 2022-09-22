import pickle

class vehiculo:
    def __init__(self):
        self.comprador = "carlos"
        self.color = "red"
        
venta = vehiculo()

print(venta.color)

file = open('historial.bin', 'wb')
pickle.dump(venta, file)
file.close

file = open('historial.bin', "rb")
histori = pickle.load(file)
file.close


