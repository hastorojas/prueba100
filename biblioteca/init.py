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

    def __str__(self):
        rpta = self.codigo_lector+" - "+self.nombres+" "+self.apellido_paterno+" "+self.apellido_materno
        return rpta
        

class Libros: 
    def __init__(self,codigo_libro,titulo,autor,categoria,paginas,descripcion):
        self.codigo_libro = codigo_libro
        self.titulo = titulo 
        self.autor = autor
        self.categoria = categoria 
        self.paginas = paginas 
        self.descripcion = descripcion 

    def __str__(self):
        rpta = self.codigo_libro+" - "+self.titulo+", "+self.autor
        return rpta

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
                print("Hasta, pronto ...")
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
optSubMenu1 = {"Listar Lectores":"1","Registrar Lector":"2","Actualizar Lector":"3","Eliminar Lector":"4","Atras":"0"}
optSubMenu2 = {"Listar Libros":"1","Registrar Libro":"2","Actualizar Libro":"3","Eliminar Libro":"4","Atras":"0"}
optSubMenu3 = {"Listar Prestamos":"1","Alquilar Libro":"2","Devolver Libro":"3","Atras":"0"}

showMenu = True
showLector = True
showLibro = True 
showPrestamo = True

respuesta = ""
rptlector = ""
rptlibros = ""
rptprestamos = ""

menuPrincipal = Menu("Menu Principal", opMenuPrincipal) 

while showMenu:
    respuesta = menuPrincipal.show()
    if (respuesta == "0"):
        print("")
        break
    elif(respuesta == "1"):
        menuLector = Menu("LECTOR", optSubMenu1) 
        while showLector:
            rptlector = menuLector.show()
            if (rptlector == "0"): #atras
                break
            if (rptlector == "1"):
                query = "select * from lector"
                result = conn.consultarBDD(query)
                headerlector = ['ID', 'Codigo', 'Nombre', 'Ape.Paterno', 'Ape.Materno',
                      'Dni','Edad', 'Telefono']
                print(tabulate(result, headers=headerlector, tablefmt='fancy_grid'))
                input("presiona cualquier tecla para continuar")
    elif(respuesta == "2"):
        menuLibros = Menu("LIBROS", optSubMenu2) 
        while showLibro:
            rptlibros = menuLibros.show()
            if (rptlibros == "0"): #atras
                break
            if (rptlibros == "1"):
                query = "select * from libros order by condicion asc"
                resultlibros = conn.consultarBDD(query)
                headerlibros = ['ID', 'Codigo', 'Titulo', 'Autor', 'Categoria',
                      'Paginas','Condicion','Descripcion']
                print(tabulate(resultlibros, headers=headerlibros, tablefmt='fancy_grid'))
                input("presiona cualquier tecla para continuar")
    elif(respuesta=="3"):
        menuPrestamos = Menu("PRESTAMOS", optSubMenu3) 
        while showPrestamo:
            rptprestamos = menuPrestamos.show()
            if (rptprestamos == "0"): #atras
                break
