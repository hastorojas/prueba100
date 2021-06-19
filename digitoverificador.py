def mostrarnombre(nom):
    print(f'Tu nombre es: {nom}')

def mostrardni(num):
    print(f'Tu DNI es: {num}')

def calculaverificador(veri):
    serienum = (6,7,8,9,0,1,1,2,3,4,5)
    seriealf = ('K','A','B','C','D','E','F','G','H','I','J')
    cadena = str(veri)
    listanum = list(cadena)

    dig1 = int(listanum[0])
    dig2 = int(listanum[1])
    dig3 = int(listanum[2])
    dig4 = int(listanum[3]) 
    dig5 = int(listanum[4]) 
    dig6 = int(listanum[5]) 
    dig7 = int(listanum[6]) 
    dig8 = int(listanum[7])

    sum_total = (dig1*3 + dig2*2 + dig3*7 + dig4*6 + dig5*5 + dig6*4 + dig7*3 + dig8*2)
    residuo = sum_total % 11
    posicion = (11 - residuo) + 1
    
    print(f'El digito verificador es: {serienum[posicion-1]}')
    print(f'La letra verificadora es: {seriealf[posicion-1]}')

while True:
    try:
        print('*****************************************************')
        nombre = str(input('Ingresa tu Nombre: '))
        dni = int(input('Ingrese tu DNI: '))
        print(' ')
        if len(str(dni))<8:
            print('el DNI tiene que ser de 8 digitos\nIntenta otra vez ...')
        else:
            opcion = int(input(f'Hola {nombre}, elije la opcion que realizaras:\n 1. Mostrar mi nombre\n 2. Mostrar mi dni\n 3. Calcular mi digito verificado\n 4. Salir\nOpcion: ')) 
            if opcion == 1:
                print('*****************************************************')
                mostrarnombre(nombre)
                break
            if opcion == 2:
                print('*****************************************************')
                mostrardni(dni)
                break
            if opcion == 3:
                print('*****************************************************')
                calculaverificador(dni)
                break
            if opcion == 4:
                print('*****************************************************')
                print('Saliendo ...')
                break 
    except ValueError:
        print('*****************************************************')
        print('Para DNI debes ingresar un numero de 8 digitos\ny el Nombre debe estar en texto\nIntenta otra vez ...')