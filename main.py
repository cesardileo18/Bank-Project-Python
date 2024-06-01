from clases.cuenta import *
import sys

miCuenta = Cuenta("Benito Perez", 2000.10, "1234", "0000", True)

def login(cuenta):
    numero = input("Numero de Cuenta: ")
    clave = input("Clave de la cuenta: ")
    
    if cuenta.numero == numero and cuenta.clave == clave:
        if cuenta.estado:
            print("Acceso autorizado")
            return True
        else:
            print("La cuenta esta Cerrada")
            return False
    else:
        print("El numero o contraseña que ha introducido con incorrectos")
        return False

def operaciones(cuenta):
    inicio = True
    acceso = login(cuenta)
    if acceso:
        while inicio:
            opcion = input('''Bienbenido ''' + cuenta.nombre + ''', escribe el numero de la accion que deseas realizar:
                    1.Sacar dinero
                    2.Depositar dinero
                    3.Ver Cuenta
                    4.Salir:
                    Tu opción: ''')
            if opcion == "1":
                cantidad = input("Que cantidad desea Sacar?: ")
                cuenta.sacarDinero(float(cantidad))
            elif opcion == "2":
                cantidad = input("Que cantidad desea ingresar?: ")
                cuenta.ingresarDinero(float(cantidad))
            elif opcion == "3":
                cuenta.getDatos()
            elif opcion == "4":
                inicio == False
                sys.exit()
                
########   Menu De Nuestra Aplicacio         ########
inicio = True

while inicio:
    opcion = input("Bienvenido, escribe el numero de la accion que quieras realizar: \n1.Inicia sesion\n2.Salir\nOpcion: ")
    if opcion == "1":
        operaciones(miCuenta)
    elif opcion == "2":
        inicio = False