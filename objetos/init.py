import os
import time
import json
from datetime import datetime

now = datetime.now()

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
                return str(self.dni) + " -> " + str(self.nombre)

        def toDic(self):
                d = {
                "nombre": self.nombre,
                "apellidos": self.apellidos,
                "dni": self.dni,
                "telefono": self.telefono,
                "codusuario": self.codusuario
                }       
                return d

class Asistencia(Usuario):
    def __init__(self,nombre,apellidos,dni,telefono,codusuario,entrada,salida):
        super().__init__(nombre,apellidos,dni,telefono,codusuario)
        self.entrada = entrada
        self.salida = salida

    def __str__(self):
                return str(self.dni) + " entrada: " + str(self.entrada)+ " salida: " + str(self.salida)

    def toDicAsist(self):
                a = {
                "nombre": self.nombre,
                "apellidos": self.apellidos,
                "dni": self.dni,
                "telefono": self.telefono,
                "codusuario": self.codusuario,
                "entrada": self.entrada,
                "salida": self.salida
                }       
                return a

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
        #print(path)
        if(os.path.isfile(path)):
            try:
                os.remove(path)
                #print("removiendo archivo")

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
                #print("Hasta, pronto")
                break
            b = 0
            for (key, value) in self.op_list.items():
                if (value == ans):
                    b = b + 1
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


showMenu = True
showUsuario = True
showAsistencia = True
showReportes = True

#Home_op = {"Agregar Usuario": "1", "Buscar Usuario": "2","Quitar Usuario": "3","Listar Usuarios":"4","Marcar Entrada":"5","Marcar Salida":"6","Salir": "0"}
Home_op = {"Usuarios":"1","Asistencia":"2","Reportes":"3","Salir":"0"}
SubMenu1 = {"Agregar Usuario": "1", "Buscar Usuario": "2","Quitar Usuario": "3","Listar Usuarios":"4","Atras":"0"}
SubMenu2 = {"Marcar Entrada":"1","Marcar Salida":"2","Atras":"0"}
SubMenu3 = {"Reporte por Usuario":"1","Reporte por Fecha":"2","Atras":"0"}

#lista de usuarios
listausuarios = []
listausuarioDic = []
#lista de asistencia
listasistencia = []
listasistenciDic = []
fileCliente = Archivo("contactos.txt")
fileAsistencia = Archivo("asistencia.txt")


def cargainicial():
    res = fileCliente.leerArchivo()
    print(res)
    listTempCliente = json.loads(res)
    for dic in listTempCliente:
        newCliente = Usuario(dic["nombre"],dic["apellidos"],dic["dni"],dic["telefono"],dic["codusuario"])
        listausuarios.append(newCliente)
        listausuarioDic.append(newCliente.toDic())

def cargainicial_asistencia():
    res = fileAsistencia.leerArchivo()
    print(res)
    listTempAsistencia = json.loads(res)
    for dic in listTempAsistencia:
        newAsist = Asistencia(dic["nombre"],dic["apellidos"],dic["dni"],dic["telefono"],dic["codusuario"],dic["entrada"],dic["salida"])
        listasistencia.append(newAsist)
        listasistenciDic.append(newAsist.toDicAsist())


cargainicial()
cargainicial_asistencia()
respuesta = ""
ansUsuario = ""
ansasistencia = ""
ansreportes = ""

Main_menu = Menu("PRINCIPAL", Home_op)

while showMenu:
    respuesta = Main_menu.show()
    if (respuesta == "0"):
        print("Hasta luego ...")
        print("")
        break
    elif(respuesta == "1"):
        menusuario = Menu("USUARIOS", SubMenu1)
        while showUsuario:
            #menusuario = Menu("USUARIOS", SubMenu1)
            ansUsuario = menusuario.show()
            if(ansUsuario == "0"): #atras 
                break                    
            elif(ansUsuario == "1"):
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
                print("Usuario agregado exitosamente !!")
                showUsuario = False
                showMenu = False
            elif(ansUsuario == "2"):
                valor = 0
                dniusuario = str(input("Ingresa el DNI a buscar: "))
                for item in listausuarios:
                    if(item.dni == dniusuario):
                        valor = 1
                        usuMod = item           
                if(valor == 1):
                    print("")
                    print("::::::: Datos del Usuario :::::::")
                    print("")
                    print(f"{usuMod.dni} | {usuMod.nombre} | {usuMod.apellidos} | {usuMod.telefono}")             
                    print("")
                    showUsuario = False
                    showMenu = False
                else: 
                    print(f"El usuario con DNI: {dniusuario} no fue encontrado")       
                    showUsuario = False
                    showMenu = False
            elif (ansUsuario == "3"):
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
                        print("")
                        print("Usuario borrado !")
                        print("")
                        listausuarios.remove(usuMod3)
                        listausuarioDic.remove(usuMod3.toDic())
                        jsonString = json.dumps(listausuarioDic)
                        fileCliente.borrarArchivo()
                        fileCliente.escribirArchivo(jsonString)
                        showUsuario = False
                        showMenu = False
                    elif(confirmacion == 'n'):
                        print("Hasta pronto ...")
                        showUsuario = False
                        showMenu = False
                else: 
                    print(f"El usuario con DNI: {dniusuarioborrar} no fue encontrado")
                    showUsuario = False
                    showMenu = False
            elif (ansUsuario == "4"):
                print("::::::: Listado de Usuarios :::::::")
                print("")
                for item in listausuarios:          
                    print(f"{item.dni} | {item.nombre} | {item.apellidos} | {item.telefono}")             
                    print("")
                    showUsuario = False
                    showMenu = False

    elif(respuesta == "2"):
        menuasistencia = Menu("ASISTENCIA", SubMenu2)
        while showAsistencia:
            #menuasistencia = Menu("ASISTENCIA", SubMenu2)
            ansasistencia = menuasistencia.show()  
            if (ansasistencia == "0"): #atras
                break
            elif (ansasistencia == "1"):
                valor = 0
                print("::::::: Marcar Entrada :::::::")
                print("")
                dniasistencia = str(input("Ingrese su DNI: "))
                for item in listausuarios:
                    if(item.dni == dniasistencia):
                        valor = 1
                        usuMod = item  
                if valor == 1:
                    print("")
                    print("::::::: Datos del Usuario :::::::")
                    print("")
                    print(f"{usuMod.dni} | {usuMod.nombre} | {usuMod.apellidos} | {usuMod.telefono}")             
                    print("")
                    entrada = str(now.day)+'/'+str(now.month)+'/'+str(now.year)+' '+str(now.hour)+':'+str(now.minute)+':'+str(now.second)
                    salida = ""
                    print(f"Entrada marcada con exito !! -> {entrada}")
                    print("")
                    asistencia = Asistencia(usuMod.nombre,usuMod.apellidos,usuMod.dni,usuMod.telefono,usuMod.codusuario,entrada,salida)
                    listasistencia.append(asistencia)
                    listasistenciDic.append(asistencia.toDicAsist())
                    jsonString = json.dumps(listasistenciDic)
                    fileAsistencia.borrarArchivo()
                    fileAsistencia.escribirArchivo(jsonString)
                    showAsistencia = False
                    showMenu = False
                else: 
                    print(f"El DNI: {dniasistencia} no se encuentra registrado !!")
                    showAsistencia = False
                    showMenu = False
            elif (ansasistencia == "2"):
                valor = 0
                print("::::::: Marcar Salida :::::::")
                print("")
                dniasistencia = str(input("Ingrese su DNI: "))
                for item in listasistencia:
                    if(item.dni == dniasistencia):
                        valor = 1
                        usuMod = item
            
                if valor == 1:
                    print("")
                    print("::::::: Datos del Usuario :::::::")
                    print("")
                    print(f"{usuMod.dni} | {usuMod.nombre} | {usuMod.apellidos} | {usuMod.telefono}")             
                    print("")
                    salida = str(now.day)+'/'+str(now.month)+'/'+str(now.year)+' '+str(now.hour)+':'+str(now.minute)+':'+str(now.second)         
                    newdni = usuMod.dni
                    newnombre = usuMod.nombre
                    newapellidos = usuMod.apellidos
                    newtelefono = usuMod.telefono 
                    newcodigo = usuMod.codusuario
                    newentrada = usuMod.entrada
                    #print(usuMod.salida)
                    print(f"Salida marcada con exito !! -> {salida}")
                    print("")
                    asistencia = Asistencia(newnombre,newapellidos,newdni,newtelefono,newcodigo,newentrada,salida)
                    listasistencia.remove(usuMod)
                    listasistencia.append(asistencia)
                    listasistenciDic.remove(usuMod.toDicAsist())
                    listasistenciDic.append(asistencia.toDicAsist())
                    jsonString = json.dumps(listasistenciDic)
                    fileAsistencia.borrarArchivo()
                    fileAsistencia.escribirArchivo(jsonString)
                    showAsistencia = False
                    showMenu = False
                else: 
                    print(f"El DNI: {dniasistencia} no se encuentra registrado !!")
                    showAsistencia = False
                    showMenu = False

    elif respuesta == "3":
        menureportes = Menu("REPORTES", SubMenu3)
        while showReportes:
            #menureportes = Menu("REPORTES", SubMenu3)
            ansreportes = menureportes.show()  
            if (ansreportes == "0"): #atras
                break
            elif(ansreportes == "1"):
                print("::::::: Reporte por Usuarios :::::::")
                print("")
                for item in listasistencia:          
                    print(f"{item.dni} | {item.nombre} | {item.apellidos}")
                    print(f"entrada: {item.entrada}")
                    print(f"salida: {item.salida}")      
                    print("")           
                    showReportes = False
                    showMenu = False
            elif(ansreportes == "2"):
                print("Reporte en construccion ... vuelva pronto =D")
                print("")
                showReportes = False
                showMenu = False
