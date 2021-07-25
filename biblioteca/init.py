from conexion import conexion
import os
import time
from tabulate import tabulate

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

class Lector:
    def __init__(self,codigo_lector,nombres,apellido_paterno,apellido_materno,dni,edad,telefono):
        self.codigo_lector = codigo_lector
        self.nombres = nombres 
        self.apellido_paterno = apellido_paterno
        self.apellido_materno = apellido_materno
        self.dni = dni
        self.edad = edad
        self.telefono = telefono 

class Libros: 
    def __init__(self,titulo,autor,categoria,paginas,descripcion):
        self.titulo = titulo 
        self.autor = autor
        self.categoria = categoria 
        self.paginas = paginas 
        self.descripcion = descripcion 

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

#Menu principal 
conn = conexion()
opMenuPrincipal ={"Lector":"1", "Libros":"2","Prestamos":"3","Salir": "0"}
opSubMenu1 = {"Listar Lectores":"1","Registrar Lector":"2","Actualizar Lector":"3","Eliminar Lector":"4","Atras":"0"}
optSubMenu2 = {"Listar Libros":"1","Registrar Libro":"2","Actualizar Libro":"3","Eliminar Libro":"4","Atras":"0"}
optSubMenu3 = {"Registro de Prestamos":"1","Alquilar Libro":"2","Devolver Libro":"3","Atras":"0"}

showHome = True
ansMenuPrincipal = "" 

menuPincipal = Menu("Menu Principal", opMenuPrincipal) 
    