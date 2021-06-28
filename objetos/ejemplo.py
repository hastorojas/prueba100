import os
import time
import json

class color:
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    DARKCYAN = '\033[36m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'

class Persona:
    def __init__(self, nombre, sexo, dni):
        self.nombre = nombre
        self.sexo = sexo
        self.dni = dni

class Cliente(Persona):
    def __init__(self, nombre, sexo, dni, codCliente=0):
        super().__init__(nombre, sexo, dni)
        if codCliente == 0:
            self.codCliente = self.codCliente + 1
        else:
            self.codCliente = codCliente

    def __str__(self) -> str:
        return self.nombre + " ---- " + str(self.codCliente)

    def comprar(self):
        print("Comprando")

        print("Termino de Comprar")

    def toDic(self):
        d = {
            "nombre": self.nombre,
            "sexo": self.sexo,
            "dni": self.dni,
            "codCliente": self.codCliente
        }
        return d


class Vendedor(Persona):
    def __init__(self, nombre, sexo, dni, codVendedor):
        super().__init__(nombre, sexo, dni)
        self.codVendedor = codVendedor

    def vender(self):
        print("Vendiendo")

        print("Termino de vender")


class Producto:

    def __init__(self, nombre, presentacion, precio):
        self.nombre = nombre
        self.presentacion = presentacion
        self.precio = precio

    def comprar(self, cantidad):
        print("comprando")
        self.__Cantidad = self.__Cantidad + cantidad
        print("termino de comprar")

    def vender(self, cantidad):
        print("comprando")
        self.__Cantidad = self.__Cantidad - cantidad
        print("termino de comprar")


class Helado(Producto):
    def __init__(self, nombre, presentacion, precio, sabor, tamaño, tipo):
        super().__init__(nombre, presentacion, precio) 
        self.sabor = sabor
        self.tamaño = tamaño
        self.tipo = tipo

    def preparar(self, cantidad):
        print("Se esta preparando el Helado")

class Archivo:
    def __init__(self, nombreArchivo):
        self.nombreArchivo = nombreArchivo

    def leerArchivo(self):
        try:
            file = open(self.nombreArchivo,'r')
            return file.read()
        except Exception as e:
            return e
        

    def borrarArchivo(self):
        directorioActual = os.getcwd()
        path = directorioActual+"\\"+self.nombreArchivo
        print(path)
        if(os.path.isfile(path)):
            try:
                os.remove(path)
                print("removiendo archivo")

            except Exception as error:
                print(error)

    def escribirArchivo(self, linea):
        try:
            directorioActual = os.getcwd()
            path = directorioActual+"\\"+self.nombreArchivo
            if(os.path.isfile(path)):
                try:
                    #escribir el archiv
                    file = open(self.nombreArchivo, 'a')
                    file.write(linea + "\n")
                except Exception as e:
                    print(e)
                finally:
                    file.close()
            else:
                file = open(self.nombreArchivo, 'w')
                file.close()
                file = open(self.nombreArchivo, 'a')
                file.write(linea + "\n")
        except Exception as error:
            print(error)      

    # def agregarPersona(self, persona):
    #     try:
    #         file = open(self.nombreArchivo, 'a')
    #         textoAgregar = "{},{},{} \n".format(persona.nombre, persona.sexo, persona.dni)
    #         file.write(textoAgregar)
    #     except Exception as ex:
    #         print(ex)
    #     finally:
    #         file.close()
    #         print(file)

class Menu:
    def __init__(self, name, op_list, pre_menu=0):
        self.name = name
        self.op_list = op_list
        self.pre_menu = pre_menu

    def show(self):
        a = True
        while a:
            self.limpiarPantalla()
            print("")
            print(color.BLUE+"::::::::::::::::::::"+"ESTE ES EL MENU DE " +
                  self.name.upper()+"::::::::::::::::::::"+color.END)
            print("")
            for (key, value) in self.op_list.items():
                print(key + color.GREEN + " → " + color.END + value)
            print("")
            ans = input(
                color.YELLOW + "Por favor, ingrese su opción: " + color.END)
            print("")
            if(ans.upper() == "0"):
                print("Hasta, pronto")
                break
            b = 0
            for (key, value) in self.op_list.items():
                if (value == ans):
                    b = b+1
            if (b > 0):
                a = False

            else:
                print(color.RED + "Opción no valida, escoja una opción valida" + color.END)
                time.sleep(3)
        return ans

    def limpiarPantalla(self):
        def clear():
            # return os.system('cls')
            return os.system('clear')
        clear()

showHome = True
showCliente = True


Home_op = {"Clientes": "1", "Empleados": "2", "Exit": "0"}
clienteOp = {"Nuevo": "1", "Antiguo": "2", "Exit": "0"}

listaCliente = []
listaClienteDic = []
fileCliente = Archivo("cliente.txt")

def cargainicial():
    res = fileCliente.leerArchivo()
    print(res)
    listTempCliente = json.loads(res)
    for dic in listTempCliente:
        newCliente = Cliente(dic["nombre"],dic["sexo"],dic["dni"],dic["codCliente"])
        listaCliente.append(newCliente)

cargainicial()
Main_menu = Menu("home", Home_op)
respuesta = Main_menu.show()

while showHome:
    if(respuesta == "0"):
        break
    elif(respuesta == "1"):
        while showCliente:
            menuCliente = Menu("Cliente", clienteOp)
            ansCliente = menuCliente.show()
            if(ansCliente == "0"):
                break
            elif(ansCliente == "1"):
                nombre = input("Escribe tu nombre: ")
                sexo = input("Escribe tu sexo [ M - F ]: ")
                dni = input("Escribe tu DNI: ")
                cliente = Cliente(nombre, sexo, dni, 3)
                listaCliente.append(cliente)
                listaClienteDic.append(cliente.toDic())
                jsonString = json.dumps(listaClienteDic)
                fileCliente.borrarArchivo()
                fileCliente.escribirArchivo(jsonString)
                print("Cliente Agregado")
            elif(ansCliente == '2'):
                for lista in listaCliente:
                    print(lista)
                codigoCliente = int(input("Escribe tu DNI: "))
                clienteEncontado = None
                for item in listaCliente:
                    if(item.dni == codigoCliente):
                        clienteEncontado = item
                        break
                if clienteEncontado:
                    print(clienteEncontado)
            