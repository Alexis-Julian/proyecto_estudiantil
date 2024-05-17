import sys
import getpass
import os



# DECLARACIÓN DE CONSTANTES

# String: usuario1, us1_email, us1_pswrd
#        usuario2, us2_email, us2_pswrd
#        usuario3, us3_email, us3_pswrd

# DECLARACIÓN DE VARIABLES

# string:usuario, contrasena, op

# Integer: cont

usuario1 = "nombre 1"
us1_email = "estudiante1@ayed.com"
us1_pswrd = "111222"

usuario2 = "nombre 2"
us2_email = "estudiante2@ayed.com"
us2_pswrd = "333444"


usuario3 = "nombre 3"
us3_email = "estudiante3@ayed.com"
us3_pswrd = "555666"


def validarDatos(inicio:str,limite:str):
    op=str(input("Elija una opcion: "))
    while op < inicio or op > limite:
        op = str(input("Error, elija una opción nuevamente: "))
    return op

def saltoDeLinea():
    """ print("\n") """
    print("\n")

saltoDeLinea()

def en_construccion():
    print("En construcción...")


def volver():
    saltoDeLinea()
    str(input("volver: "))
    limpiar()


def limpiar():
    os.system("cls")


def pausar():
    os.system("pause")

def menu_principal():

    saltoDeLinea()
    print("----------Menu principal----------")
    saltoDeLinea()

    print("1_Gestionar mi perfil ")
    print("2_Gestionar candidatos")
    print("3_Matcheos")
    print("4_Reportes estadísticos")
    print("0_Salir")
    saltoDeLinea()


def opciones_menu1():
    print("----------Menu principal----------")
    saltoDeLinea()
    
    print("1_Gestionar mi perfil\n2_Gestionar candidatos\n3_Matcheos")
    op = validarDatos("0","4")
    match op:
        case '1':
            limpiar()
            menu_modificar() # LOGICA
            volver()  # cuando funcione se borraas

        case '2':
            limpiar()
            en_construccion()
            volver()

        case '3':
            limpiar()
            en_construccion()
            volver()

        case '4':
            limpiar()
            en_construccion()
            volver()

        case '0':
            limpiar()
            print("Saliendo")
            saltoDeLinea()
             
#editar datos personales
def modificarpersonales():
    saltoDeLinea()
    print("----------Inormacion Personal----------")
    print("1_ Fecha de nacimiento ")
    print("2_Biografia")
    print("3_Hobbies")
    print("0_Salir")
    saltoDeLinea()

def menu_modificar():
    modificarpersonales()
    ir = validarDatos("0","3")
    while ir != "0": 
        match ir:
            case '1':
                nacimiento = str(input("Ingrese su fecha de nacimiento: "))  
                print (nacimiento) 
            case '2':
                biografia = str(input("Escriba su biografía: "))
                print(biografia)
            case '3':
                hobbie = str(input("¿cuales son sus hobbies?: "))
                print(hobbie)
        pausar()
        limpiar()
        modificarpersonales()
        ir = validarDatos("0","3")


        








# INCIO PROGRAMA
usuario = str(input("Ingrese nombre de usuario: "))
contrasena = str(input("Ingrese su contraseña: "))
cont = 0


while ((usuario != us1_email) and (usuario != us2_email) and (usuario != us3_email)) or ((contrasena != us1_pswrd) and (contrasena != us2_pswrd) and (contrasena != us3_pswrd)):
    limpiar()
    if cont < 2:
        cont = cont + 1
        usuario = str(
            input("Datos incorrectos, ingrese su email nuvemante: "))
        contrasena = str(
            input("Contraseña incorrecta, ingrese su clave nuevamente: "))
        limpiar()
    else:
        print("acceso denegado")
        saltoDeLinea()
        str(input("Ingrese cualquier valor para salir: "))
        #sys.exit()


limpiar()

""" op = '1'

while op != '0':
    menu_principal() # VISTA 
    op = str(input("Elija una opción: "))
    # # ca
    while op < '0' or op > '4':
        limpiar()
        menu_principal() # VISTA
        op = str(input("Error, elija una opción nuevamente: "))

    opciones_menu1()
    ir='1' """





    