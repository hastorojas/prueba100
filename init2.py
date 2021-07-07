intvalor1 = 100
intvalor2 = 100
resta = intvalor1 - intvalor2

print('Suma: '+ str(intvalor1 + intvalor2))
print('Resta: {r}'.format(r=resta))
print('Multiplicacion: {}'.format(intvalor1 * intvalor2))
print('Division igual a {2} de {1} y {0}'.format(intvalor1,intvalor2,intvalor2 / intvalor1))
print(f'Division exacta es: {intvalor2 // intvalor1}')
print('Residuo: %d'%(intvalor2 % intvalor1)) #desactualizado

#comparacion de numeros
if intvalor1 > intvalor2:
    print('El numero {0} es mayor que {1}'.format(intvalor1,intvalor2))
elif intvalor2 > intvalor1:
    print('El numero {0} es menor que {1}'.format(intvalor1,intvalor2))
else:
    print('El numero {0} es igual que {1}'.format(intvalor1,intvalor2))

#comprobacion de numeros pares
if intvalor1%2==0:
    print('El numero {} es par'.format(intvalor1))
else:
    print('El numero {} es impar'.format(intvalor1))


if intvalor2%2==0:
    print('El numero {} es par'.format(intvalor2))
else:
    print('El numero {} es impar'.format(intvalor2))


#subcojuntos

cadena1 = 'Python'
cadena2 = 'Programacion'

print (cadena1[0:3])
print (cadena2[3:7])

print(cadena2+' '+cadena1)

#listas 
print('************* EJEMPLOS CON LISTAS **************')
lista1 = ['roja','verde','amarilla']
print(lista1)
print (lista1[0])
print (lista1[1])
print (lista1[2])

lista1.append('morado')
print('Tamano de la lista: {}'.format(len(lista1)))
print(lista1.index('verde'))

#borrado mediante el indice de una lista
lista1.pop(1)
print(lista1)

#borrado mediante el valor de una lista
lista1.remove('morado')
print(lista1)