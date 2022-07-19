import os
from usuario import Usuario

class Menu:
    def __init__(self,tit,opc):
        self.titulo=tit
        self.opciones=opc

    def menu(self):
        print(self.titulo)
        for opcion in self.opciones:
            print(opcion)
        opc = input("Elija opcion[1...{}]: ".format(len(self.opciones)))
        return opc

opc =""
while opc !="4":
    os.system("cls")
    men = Menu("\033[3;36m"+"Elija su rol",["\033[0;33m"+"1) Administrador","2) Empleado","3) Cliente","4) Salir"])
    opc = men.menu()
    os.system("cls")
    if opc == "1":
        opc1 =""
        while opc1 !="4":
            os.system("cls")
            men = Menu("Opciones del Administrador",["1) Iniciar Sesion","2) Informacion Personal","3) Control de Acceso","4) Salir"])
            opc1 = men.menu()
            if opc1 == "1":
                opc1_1 =""
                while opc1_1 !="5":
                    os.system("cls")
                    men1 = Menu("\033[3;36m"+"Operaciones inicio de sesion",["\033[0;33m"+"1) Crear Cuenta","2) Autentificacion de cuenta","3) Actualizar contraseña","4) Analisis de entrada externa","5) Salir"])
                    opc1_1 = men1.menu()
                    os.system("cls")

                    if opc1_1 == "1":
                        input("Ingrese usuario: ")
                        input("Ingrese contraseña: ")
                        print("Cuenta creada con exito")
                        input("Presione una tecla para continuar...")

                    elif opc1_1 == "2":
                        input("Ingrese codigo de autentificación: ")
                        print("Autentificación exitosa")
                        input("Presione una tecla para continuar...")

                    elif opc1_1 == "3":
                        input("Ingrese contraseña actual: ")
                        input("Ingrese nueva contraseña: ")
                        print("Cambio de contraseña exitoso")
                        input("Presione una tecla para continuar...")

                    elif opc1_1 == "4":
                        print("No se ha dectectado entradas externas al sistema")
                        input("Presione una tecla para continuar...")

            elif opc1 == "2":
                opc2 =""
                usua1 = Usuario()
                while opc2 !="4":
                    os.system("cls")
                    men2 = Menu("\033[3;36m"+"Operaciones de Información Personal",["\033[0;33m"+"1) Ingresar datos personales","2) Eliminar datos personales","3) Editar Informacion Personal","4) Salir"])
                    opc2 = men2.menu()
                    os.system("cls")

                    if opc2 == "1":
                        print("Ingreso de datos personales")
                        usua1.mostrarUsuario
                        input("Ingrese Id:")
                        input("Ingrese nombre:")
                        input("Ingrese direccion:")
                        input("Ingrese telefono:")
                        input("Ingrese cedula:")
                        print("Ingreso exitoso")
                        input("Presione una tecla para continuar...")

                    elif opc2 == "2":
                        print("Eliminar datos personales")
                        print("Seleccionar datos a eliminar")
                        input("Presione una tecla para continuar...")

                    elif opc2 == "3":
                        print("Editar datos personales")
                        print("Datos editados correctamente")
                        input("Presione una tecla para continuar...")

            elif opc1 == "3":
                opc3 =""
                while opc3 !="3":
                    os.system("cls")
                    men3 = Menu("\033[3;36m"+"Operaciones de Control de acceso",["\033[0;33m"+"1) Clientes","2) Empleados","3) Salir"])
                    opc3 = men3.menu()
                    os.system("cls")

                    if opc3 == "1":
                        print("Historial de cliente")
                        input("Presione una tecla para continuar...")

                    elif opc3 == "2":
                        print("Historial de empleados")
                        input("Presione una tecla para continuar...")

    elif opc == "2":
        opc1 =""
        while opc !="3":
            os.system("cls")
            men = Menu("Opciones de Empleados",["1) Iniciar Sesion","2) Informacion Personal","3) Salir"])
            opc = men.menu()
            if opc == "1":
                opc1 =""
                while opc1 !="4":
                    os.system("cls")
                    men1 = Menu("\033[3;36m"+"Operaciones inicio de sesion",["\033[0;33m"+"1) Crear Cuenta","2) Autentificacion de cuenta","3) Actualizar contraseña","4) Salir"])
                    opc1 = men1.menu()
                    os.system("cls")

                    if opc1 == "1":
                        input("Ingrese usuario: ")
                        input("Ingrese contraseña: ")
                        print("Cuenta creada con exito")
                        input("Presione una tecla para continuar...")

                    elif opc1 == "2":
                        input("Ingrese codigo de autentificación: ")
                        print("Autentificación exitosa")
                        input("Presione una tecla para continuar...")

                    elif opc1 == "3":
                        input("Ingrese contraseña actual: ")
                        input("Ingrese nueva contraseña: ")
                        print("Cambio de contraseña exitoso")
                        input("Presione una tecla para continuar...")

            elif opc == "2":
                opc2 =""
                usua1 = Usuario()
                while opc2 !="4":
                    os.system("cls")
                    men2 = Menu("\033[3;36m"+"Operaciones de Información Personal",["\033[0;33m"+"1) Ingresar datos personales","2) Eliminar datos personales","3) Editar Informacion Personal","4) Salir"])
                    opc2 = men2.menu()
                    os.system("cls")

                    if opc2 == "1":
                        print("Ingreso de datos personales")
                        usua1.mostrarUsuario
                        input("Ingrese Id:")
                        input("Ingrese nombre:")
                        input("Ingrese direccion:")
                        input("Ingrese telefono:")
                        input("Ingrese cedula:")
                        print("Ingreso exitoso")
                        input("Presione una tecla para continuar...")

                    elif opc2 == "2":
                        print("Eliminar datos personales")
                        print("Seleccionar datos a eliminar")
                        input("Presione una tecla para continuar...")

                    elif opc2 == "3":
                        print("Editar datos personales")
                        print("Datos editados correctamente")
                        input("Presione una tecla para continuar...")

    elif opc == "3":
        opc3 =""
        while opc3 !="3":
            os.system("cls")
            men3 = Menu("Opciones de Clientes",["1) Iniciar Sesion","2) Informacion Personal","3) Salir"])
            opc3 = men3.menu()
            if opc3 == "1":
                opc1 =""
                while opc1 !="4":
                    os.system("cls")
                    men = Menu("\033[3;36m"+"Operaciones inicio de sesion",["\033[0;33m"+"1) Crear Cuenta","2) Autentificacion de cuenta","3) Actualizar contraseña","4) Salir"])
                    opc1 = men.menu()
                    os.system("cls")

                    if opc1 == "1":
                        input("Ingrese usuario: ")
                        input("Ingrese contraseña: ")
                        print("Cuenta creada con exito")
                        input("Presione una tecla para continuar...")

                    elif opc1 == "2":
                        input("Ingrese codigo de autentificación: ")
                        print("Autentificación exitosa")
                        input("Presione una tecla para continuar...")

                    elif opc1 == "3":
                        input("Ingrese contraseña actual: ")
                        input("Ingrese nueva contraseña: ")
                        print("Cambio de contraseña exitoso")
                        input("Presione una tecla para continuar...")

            elif opc3 == "2":
                opc2 =""
                usua1 = Usuario()
                while opc2 !="4":
                    os.system("cls")
                    men2 = Menu("\033[3;36m"+"Operaciones de Información Personal",["\033[0;33m"+"1) Ingresar datos personales","2) Eliminar datos personales","3) Editar Informacion Personal","4) Salir"])
                    opc2 = men2.menu()
                    os.system("cls")

                    if opc2 == "1":
                        print("Ingreso de datos personales")
                        usua1.mostrarUsuario
                        input("Ingrese Id:")
                        input("Ingrese nombre:")
                        input("Ingrese direccion:")
                        input("Ingrese telefono:")
                        input("Ingrese cedula:")
                        print("Ingreso exitoso")
                        input("Presione una tecla para continuar...")

                    elif opc2 == "2":
                        print("Eliminar datos personales")
                        print("Seleccionar datos a eliminar")
                        input("Presione una tecla para continuar...")

                    elif opc2 == "3":
                        print("Editar datos personales")
                        print("Datos editados correctamente")
                        input("Presione una tecla para continuar...")

    else:
        print("Opcion no valida")

print("Lo esperamos en una proxima ocasion")