def ingresa_numero(num):
    while True:
        try:
            print(f'El numero ingresado es: {num}')
            break
        except ValueError:
            print('Debes ingresar un numero, Intenta otra vez ... ')