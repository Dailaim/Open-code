import sqlite3

conecion = sqlite3.connect('./alumnos.db')
cursor =conecion.cursor()

cursor.execute("CREATE TABLE Alumnos(id INTEGER PRIMARY KEY AUTOINCREMENT,nombre TEXT NOT NULL,apellido TEXT NOT NULL);")

cursor.execute("INSERT INTO Alumnos(nombre,apellido) VALUES('pabo', 'guerrero')")
cursor.execute("INSERT INTO Alumnos(nombre,apellido) VALUES('marco', 'Rodriguez')")
cursor.execute("INSERT INTO Alumnos(nombre,apellido) VALUES('polo', 'Martinez')")
cursor.execute("INSERT INTO Alumnos(nombre,apellido) VALUES('R2t2', 'Perez')")
cursor.execute("INSERT INTO Alumnos(nombre,apellido) VALUES('Catrina', 'Mongomerri')")
cursor.execute("INSERT INTO Alumnos(nombre,apellido) VALUES('Otrama', 'Gonzales')")
cursor.execute("INSERT INTO Alumnos(nombre,apellido) VALUES('Marzo', 'Otorres')")
cursor.execute("INSERT INTO Alumnos(nombre,apellido) VALUES('Martacosa', 'Iglesias')")
conecion.commit()

cursor.execute("SELECT * FROM Alumnos WHERE nombre = 'pabo'")

rows = cursor.fetchall()


print(rows)
conecion.close()