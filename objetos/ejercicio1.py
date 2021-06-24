class Alumno: 
    def __init__(self,nombre, nota):
        self.nombre = nombre
        self.nota = nota 
    
    def resultado(self):
        if self.nota>10:
            print('APROBADO')
        else:
            print('JALADO')


obj1 = Alumno('Haroun',12)
obj1.resultado()