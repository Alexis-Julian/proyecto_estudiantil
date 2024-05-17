import getpass
from datetime import datetime
import os


#USAR GET_PASS
#VARIABLE GLOBAL PARA SABER QUE USUARIO ESTA LOGUEADO 
email_aut = ""

#DECLARACIONES
est1_email= "estudiante1@ayed.com"
est1_contraseña="111222"
est1_nombre=""
est1_fecha_de_nacimiento=""
est1_biografía=""
est1_hobbies=""


est2_email= "estudiante2@ayed.com"
est2_contraseña="333444"
est2_nombre=""
est2_fecha_de_nacimiento=""
est2_biografía=""
est2_hobbies=""

est3_email= "estudiante3@ayed.com"
est3_contraseña="555666"
est3_nombre=""
est3_fecha_de_nacimiento=""
est3_biografía=""
est3_hobbies=""

def VerEstudiante(email:str):
    #print(email)
    if (email == est1_email ):
        print("\nNombre: ",est1_nombre,"\nFecha: ",est1_fecha_de_nacimiento)
        print("\nBiografia: ",est1_biografía,"\nHobbies: ",est1_hobbies)

    if (email == est2_email):
        print("\nNombre: ",est2_nombre,"\nFecha: ",est2_fecha_de_nacimiento)
        print("Biografia: ",est2_biografía,"\nHobbies: ",est2_hobbies)

    if (email == est3_email):
        print("Nombre: ",est3_nombre,"\nFecha: ",est3_fecha_de_nacimiento)
        print("Biografia: ",est3_biografía,"\nHobbies: ",est3_hobbies)
        

def LimpiarConsola():
    os.system("cls")
    
def Contruccion():
    print("En contruccion...")


def CrearTitulo(titulo:str):
    columnas=""
    
    cantidadLetra:int = len(titulo) # ES LA CANTIDAD DE LETRAS QUE TIENE EL TITULO
    columnaTamaño:int = os.get_terminal_size().columns

    for i in range(0,columnaTamaño):
        columnas= columnas + "_"
    
    copiarColumnas = (columnaTamaño - cantidadLetra )//2

    print(columnas)
    print("\n" + " " * copiarColumnas + titulo )
    print(columnas)
    
#------------- VALIDACIONES #
def ValidarSi_No():
    respuesta=input("Ingrese si o no: ") 
    while (respuesta !="si") and  (respuesta !="no"):
        print("No es un opción valida, ingrese si o no")
        respuesta=input("Ingrese si o no: ")
    return respuesta

def Mostrar(string):
    print("\n"+string+"\n")


def ValidarRangoDeNumero(inicio:int,limite:int):
    try:
        numero =int(input("Ingrese una opción: "))
        while (numero < inicio) or (numero > limite):
            print("Error, ingrese nuevamente el número")
            numero =int(input("Ingrese una opción: "))
        return numero
    except:
        Mostrar("Error: Solamente se permiten numeros")
        return ValidarRangoDeNumero(inicio,limite)
    
    

#--------------------------------    

def ValidarLetras():
    letra=str(input("Ingrese una opción: "))
    while (letra!="a") and (letra!="b") and (letra!="c"):
        print("Error, debe elegir una letra del menú")
        letra=str(input("Ingrese una opción: "))
    return letra  



    
def CambiarCampos(email:str,campo:str,valor:str):
    #ESTO ES PARAMETIZABLE CON UN CALLBACK  <- PARA DESPUES    
    match (campo):
        case ("nombre"):
            if(est1_email ==email_aut): 
                est1_nombre = valor
            if(est2_email ==email_aut): 
                est1_nombre = valor
            if(est3_email ==email_aut): 
                est1_nombre = valor
        case ("fecha"):
            if(est1_email ==email_aut): 
                est1_fecha_de_nacimiento = valor
            if(est2_email ==email_aut): 
                est2_fecha_de_nacimiento = valor
            if(est3_email ==email_aut): 
                est3_fecha_de_nacimiento = valor
        case ("biografia"):
            if(est1_email ==email_aut): 
                est1_biografía = valor
            if(est2_email ==email_aut): 
                est2_biografía = valor
            if(est3_email ==email_aut): 
                est3_biografía = valor
        case ("hobbie"):
            if(est1_email ==email_aut): 
                est1_hobbies = valor
            if(est2_email ==email_aut): 
                est1_hobbies = valor
            if(est3_email ==email_aut): 
                est1_hobbies = valor
            
#------------- VALIDACIONES #
def EditarDatosPersonales():
    menu_reutilizable = "\n1-Nombre\n","\n2-Fecha de nacimiento\n","\n3-Biografia\n","\n4-Hobbies\n", "\n0-Volver"

    print(menu_reutilizable)
    print("¿Que desea modificar? ")

    opcion = ValidarRangoDeNumero(0,4)
    while opcion != 0:
        match (opcion):
            case (1):
                nombre=input("Ingrese su nombre deseado: ")  
                CambiarCampos(email_aut,"nombre",nombre)
            case (2):
                fecha=input("Ingrese su Fecha de nacimiento: ")
                CambiarCampos(email_aut,"fecha",fecha)
            case (3):
                biografia=input("Ingrese su nueva Biografia: ")
                CambiarCampos(email_aut,"biografia",biografia) 
            case (4):
                hobbie=input("Ingrese sus hobbies: ")
                CambiarCampos(email_aut,"hobbie",hobbie)

        print("Desea modificar algun campo mas?")
        print(menu_reutilizable)
        opcion = ValidarRangoDeNumero(0,4)

            

def EliminarPefil():
    print("En construcción")

def GestionarMiPerfil():
    menu_reutilizable=print("\na-Ver Candidato\n\nb-Reportar un candidato\n\nc-Volver\n")
    LimpiarConsola()
    CrearTitulo("GESTIONAR MI PERFIL")
    print(menu_reutilizable)
    opcion=ValidarLetras()
    while opcion != "c":
        match (opcion):
            case ("a"):
                EditarDatosPersonales()
            case ("b"):
                EliminarPefil()

        LimpiarConsola()
        CrearTitulo("GESTIONAR MI PERFIL")
        print("\na-Editar mis datos personales\n","\nb-Eliminar mi perfil\n","\nc-volver\n")
        opcion=ValidarLetras()

   
def GestionarCandidatos():
    CrearTitulo("GESTIONAR MI PERFIL")
    opcion=ValidarLetras()

    while opcion != "c":
        match (opcion):
            case ("a"):
                VerCandidatos()
            case ("b"):
                Contruccion()
    
    print("\na-Ver Candidato\n\nb-Reportar un candidato\n\nc-Volver\n")
 
def VerCandidatos():
    if(est1_email !=  email_aut):      
        VerEstudiante(est1_email)    
            
    elif(est2_email != email_aut):
        VerEstudiante(est2_email)   
    
    elif(est3_email != email_aut):
        VerEstudiante(est3_email)
    






def MenuPrincipal():
    menu_reutilizable= "\n1-Gestionar mi perfil\n\n2-Gestionar Candidatos\n\n3-Matcheos\n\n4-Reportes Estadsticos\n\n0-Salir\n"
    LimpiarConsola()
    CrearTitulo("MENU PRINCIPAL")
    print(menu_reutilizable)
    # VALIDA EL RANGO DE NUMERO [0-4]
    opcion = ValidarRangoDeNumero(0,4)
    while opcion != 0 :
        match (opcion):
            case (1):
                GestionarMiPerfil()
            case (2):
                GestionarCandidatos()
            case (3):
                Contruccion()
            case (4):
                Contruccion()

        LimpiarConsola()
        CrearTitulo("MENU PRINCIPAL")
        print(menu_reutilizable)
        opcion = ValidarRangoDeNumero(0,4)
        
    # end match


def IniciarSesion():
    global email_aut
    LimpiarConsola()
    CrearTitulo("Bienvenido, ¿buscando al compañero ideal?  ")

    #GENERAMOS LA VARIABLE INTENTO <= 3 PARA QUE NO HAYA ERROR
    intento = 0
    #LA VARIABLE AUTENTICADO SIRVE COMO BOOLEANO PARA SABER CUANDO EL USUARIO ESTA LOGEADO
    autenticado = False
    
      
    while intento < 3 and not(autenticado): 
        print("")
        
        email = input("Ingrese el email: ")
        contraseña = input("Ingrese la contraseña: ")
        
        #PRIMER CASO | ESTUDIANTE 1
        if (email == est1_email ) and (contraseña == est1_contraseña):
            autenticado= True
         
        #SEGUNDO CASO | ESTUDIANTE 2
        if (email == est2_email) and (contraseña == est2_contraseña):
            autenticado= True
            
        #TERCER CASO | ESTUDIANTE 3
        if (email == est3_email) and (contraseña == est3_contraseña):
            autenticado= True
        
        if(not(autenticado)):
            print("\nEl email o la contraseña son incorrectas")
            
        intento = intento + 1

    #SI EL AUTENTICADO ES TRUE ENTONCES SE TE DIRIGE AL MENU PRINCIPAL Y SI NO SALE DEL PROGRAMA 
    if(autenticado):
        email_aut = email
        MenuPrincipal()
    else:
        Mostrar("Reintente nuevamente mas tarde...")

 
def Inicializacion():
    IniciarSesion()
    

Inicializacion() 

    
    

