class Calculadora():
    def __init__(self):
        self.valor1 = int(input('Ingrese el primer numero: '))
        self.valor2 = int(input('Ingrese el segundo numero: '))
        if self.valor1>self.valor2:
            self.suma()
            self.resta()
            self.multiplicacion()
            self.division()
        else:
            print('El primer numero debe ser mayor que el segundo.')


    def __str__(self):
        return f'El primero numero es: {self.valor1}\nEl segundo numero es: {self.valor2}'

    def suma(self):
        res1 = self.valor1 + self.valor2
        print(f'La suma es: {res1}')

    def resta(self):
        res1 = self.valor1 - self.valor2
        print(f'La suma es: {res1}')

    def multiplicacion(self):
        res1 = self.valor1 * self.valor2
        print(f'La suma es: {res1}')

    def division(self):
        res1 = self.valor1 / self.valor2
        print(f'La suma es: {res1}')


obj1 = Calculadora()
print(obj1)
