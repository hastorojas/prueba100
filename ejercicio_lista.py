try:
    lista=[]
    cant = int(input('De que tamaño quieres tu lista: '))
    i = 0

    while i < cant:
        valor = input('Agregue un nombre a la lista: ')
        lista.append(valor)
        i = i + 1

    print('El listado es el siguiente: ')
    print(lista)

except Exception as ex:
    print('Hubo un problemilla; '+str(ex))
finally:
    print('Se termino de ejecutar')