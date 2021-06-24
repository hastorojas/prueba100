class Triangulo:
    def __init__(self):
        self.lado1 = int(input('Ingrese el primer lado: '))
        self.lado2 = int(input('Ingrese el segundo lado: '))
        self.lado3 = int(input('Ingrese el tercer lado: '))

    def mayor(self):
        if self.lado1>self.lado2 and self.lado1>self.lado3 :
            print(f'El lado con valor {self.lado1} es el mayor')
        elif self.lado2>self.lado3:
            print(f'El lado con valor {self.lado2} es el mayor')
        else :
            print(f'El lado con valor {self.lado3} es el mayor')
    
    def calcular(self):
        if self.lado1 == self.lado2 and self.lado1 == self.lado3 :
            print('Es un triagunlo equilatero')
        elif self.lado1 != self.lado2 and self.lado1 != self.lado3 :
            print('Es un triangulo escaleno')
        else:
            print('Es un triangulo isosceles')
    

obj1 = Triangulo()
obj1.mayor()
obj1.calcular()