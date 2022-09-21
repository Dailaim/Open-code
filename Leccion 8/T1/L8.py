archivo = open('archivo1.txt', 'w')
archivo.write('Escriniebiendo una linea\n')
archivo.close()

archivo = open('archivo1.txt', 'r+')
archivo.readline()
archivo.write('Segunda linea\n')

archivo.seek(0)
print(archivo.read())
archivo.close()
