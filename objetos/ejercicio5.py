class Agenda:
    def __init__(self):
        self.lista = []

    def menu(self):
        while True:
            opcion = int(input('*********** MENU DE OPCIONES **************\n\n1. Agregar Contacto\n2. Lista de Contactos\n3. Buscar Contacto\n4. Editar Contacto\n5. Cerrar Agenda\n\nElija una opcion: '))

            if opcion == 1:
                self.agregar_contacto()
                break
            elif opcion == 2:
                self.imprimir_contactos()
                break
            elif opcion == 3:
                break
            elif opcion == 4:
                break
            elif opcion == 5:
                break
            else:
                print('Elija solo las opciones que se muestran')

    def agregar_contacto(self):
        self.nombre = str(input('Ingrese nombre: '))
        self.telefono = int(input('Ingrese telefono: '))
        self.email = str(input('Ingrese email: '))

        self.lista.append({'nombre':self.nombre,'telefono':self.telefono,'email':self.email})
        print(self.lista[0]['nombre'])

    def imprimir_contactos(self):
        print(self.lista[0]['nombre'])
    

obj1 = Agenda()
obj1.menu()




