num_magico=12345679
num_usuario = int(input('Ingresa un numero del 1 al 9: '))

if num_usuario>=1 and num_usuario<=9:       
        num_usuario = num_usuario * 9 
        num_magico = num_magico * num_usuario
        print(f'Resultado {num_magico}') 

else:
        print(f'El numero debe ser del 1 al 9, tu ingresaste el {num_usuario}')