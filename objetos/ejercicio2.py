class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad 

    def calcular(self):
        if self.edad>18:
            print(f'{self.nombre} eres mayor de edad')
        else:
            print(f'{self.nombre} eres un crio aun') 

obj1 = Persona('Haroun',12)
obj1.calcular()     