nombre = input('Hola, como te llamas? ')
edad = int(input(f'Me alegra conocerte, {nombre}, que edad tienes? '))
if edad > 18:
    print(f'{nombre} ya eres mayor de edad')
else:
    print(f'{nombre} todavia eres un crio')
