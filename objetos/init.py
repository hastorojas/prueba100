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
     def __init__(self,nombre,apellidos,dni,telefono):
        self.nombre = nombre
        self.apellidos = apellidos
        self.dni = dni
        self.telefono = telefono


class Usuario(Persona):    
        def __init__(self, nombre, apellidos ,dni, telefono,codusuario=0):
                super().__init__(nombre, apellidos, dni, telefono)
                if codusuario == 0:
                        self.codusuario = self.codusuario + 1
                else:
                        self.codusuario = codusuario

        def __str__(self):
                return str(self.codusuario) + " -> " + str(self.nombre)

        def toDic(self):
                d = {
                "nombre": self.nombre,
                "apellidos": self.apellidos,
                "dni": self.dni,
                "telefono": self.telefono,
                "codusuario": self.codusuario
                }       
                return d

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
        path = directorioActual+"//"+self.nombreArchivo
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
            path = directorioActual+"//"+self.nombreArchivo
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


listausuarios = []
listausuarioDic = []

fileCliente = Archivo("contactos.txt")

def cargainicial():
    res = fileCliente.leerArchivo()
    print(res)
    listTempCliente = json.loads(res)
    for dic in listTempCliente:
        newCliente = Usuario(dic["nombre"],dic["apellidos"],dic["dni"],dic["telefono"],dic["codusuario"])
        listausuarios.append(newCliente)
        listausuarioDic.append(newCliente.toDic())

cargainicial()
showUsuario = True
Home_op = {"Agregar Usuario": "1", "Buscar Usuario": "2","Quitar Usuario": "3","Listar Usuarios":"4","Salir": "0"}
respuesta = ""
Main_menu = Menu("USUARIOS", Home_op)

while showUsuario:
        respuesta = Main_menu.show()
        if(respuesta == "0"):
            print("Hasta luego...")
            break

        elif(respuesta == "1"):
            nombre = str(input('Ingrese su nombre: '))
            apellidos = str(input('Ingrese su apellido: '))
            dni = str(input('Ingrese su DNI: '))
            telefono = int(input('Ingrese su telefono: '))
            usuario = Usuario(nombre,apellidos,dni,telefono,2)
            listausuarios.append(usuario)
            listausuarioDic.append(usuario.toDic())
            jsonString = json.dumps(listausuarioDic)
            fileCliente.borrarArchivo()
            fileCliente.escribirArchivo(jsonString)
            print(usuario)
            print("Usuario Agregado !!")

        elif (respuesta == "2"):
            valor = 0
            dniusuario = str(input("Ingresa el DNI a buscar: "))
            for item in listausuarios:
                if(item.dni == dniusuario):
                    valor = 1
                    usuMod = item
                    
            if (valor == 1):
                print("")
                print("::::::: Datos del Usuario :::::::")
                print("")
                print(f"{usuMod.dni} | {usuMod.nombre} | {usuMod.apellidos} | {usuMod.telefono}")             
                print("")
                break
            else: 
                print(f"El usuario con DNI: {dniusuario} no fue encontrado")       
                break

        elif (respuesta == "3"):
            valor3 = 0
            dniusuarioborrar = str(input("Ingrese el DNI del usuario a borrar: "))
            for item in listausuarios:
                if(item.dni == dniusuarioborrar):
                    valor3 = 1
                    usuMod3 = item

            if (valor3 == 1):
                print("")
                print("::::::: Datos del Usuario :::::::")
                print("")
                print(f"{usuMod3.dni} | {usuMod3.nombre} | {usuMod3.apellidos} | {usuMod3.telefono}")             
                print("")
                confirmacion = str(input("Estas seguro que quieres borrarlo [s/n]? "))
                
                if(confirmacion == 's'):
                    listausuarios.remove(usuMod3)
                    listausuarioDic.remove(usuMod3.toDic())
                    jsonString = json.dumps(listausuarioDic)
                    fileCliente.borrarArchivo()
                    fileCliente.escribirArchivo(jsonString)
                    print("Usuario borrado !")
                    break
                elif(confirmacion == 'n'):
                    print("Hasta pronto ...")
                    break
            else: 
                print(f"El usuario con DNI: {dniusuarioborrar} no fue encontrado")
                break

        elif (respuesta == "4"):
            print("::::::: Listado de Usuarios :::::::")
            print("")
            for item in listausuarios:          
                print(f"{item.dni} | {item.nombre} | {item.apellidos} | {item.telefono}")             
                print("")
            break
