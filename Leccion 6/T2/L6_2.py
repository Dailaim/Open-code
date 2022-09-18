class alumnos():
    def __init__(self,nombre,nota):
        self.nombre = nombre
        self.nota = nota
        self.__data = 3
        
    def aprobacion(self):
        print("Nombre del estudiante:", self.nombre)
        print("Nota del estudiante:", self.nota)
        print(self.__data)
        
        match self.nota:
            case self.nota if self.nota>= 9: print("Aprobo con honores")
            case self.nota if self.nota>= 6: print("Su nota es aprobatoria")
            case _: print("Su nota no es aprobatoria")
            
        
andres = alumnos("Andres",9)

andres.__data = 7
andres.aprobacion()