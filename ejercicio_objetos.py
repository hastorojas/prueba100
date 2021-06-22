class vehiculo():
    def __init__(self,color,precio):
        self.color = color
        self.precio = precio
        
class avion(vehiculo):
    def __init__(self, color, precio,cod_avion):
        super().__init__(color, precio)
        self.cod_avion = cod_avion

class auto(vehiculo):
    def __init__(self, color, precio,cod_auto):
        super().__init__(color, precio)
        self.cod_auto = cod_auto

veh1 = avion('blanco',500000,'AV001')

print(f'color: {veh1.color} - precio: {veh1.precio}')

veh2 = auto('blanco',270000,'AT001')

print(veh2.color)
