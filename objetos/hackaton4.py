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


class Persona():
     def __init__(self,nombre,edad,telefono):
        self.nombre = nombre
        self.edad = edad
        self.telefono = telefono


class Usuario(Persona):    
        def __init__(self, nombre, edad, telefono,codusuario=0):
                super().__init__(nombre, edad, telefono)
                if codusuario == 0:
                        self.codusuario = self.codusuario + 1
                else:
                        self.codusuario = codusuario

        def __str__(self):
                return str(self.codusuario) + " -> " + str(self.nombre)

        def toDic(self):
                d = {
                "nombre": self.nombre,
                "edad": self.edad,
                "telefono": self.telefono,
                "codusuario": self.codusuario
                }       
                return d

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

showUsuario = True

Home_op = {"Agregar Usuario": "1", "Buscar Usuario": "2","Quitar Usuario": "3","Listar Usuarios":"4","Salir": "0"}

listausuarios =[]
listausuarioDic = []

Main_menu = Menu("USUARIOS", Home_op)
respuesta = Main_menu.show()

while showUsuario:
        if(respuesta == "0"):
                break
        elif(respuesta == "1"):
                nombre = input('Ingrese su nombre: ')
                edad = input('Ingrese su edad: ')
                telefono = input('Ingrese su telefono: ')
                usuario = Usuario(nombre,edad,telefono,2,)
                listausuarios.append(usuario)
                print(usuario)
                break

        elif (respuesta == "2"):
                for lista in listausuarios:
                    print(lista)


