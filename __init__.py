n = int(input('Ingrese un numero entero: '))
    
if n>=1 and n<=150:
    for i in range(1,n+1):
        print(i, end="")
else:
    print('Fuera de rango')