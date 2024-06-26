from getpass import getpass
import random
from datetime import datetime
from datetime import timedelta

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


def Ruleta():
    def RenovarConsola():
        LimpiarConsola()
        CrearTitulo("Bienvenido a la ruleta")
        print("")
        print("La suma de las probabiliades debe dar 100")
        print("")
    RenovarConsola()
    a=0
    b=0
    c=0
    while not(a+b+c == 100):
        a=int(input("Probabilidad de la persona A: "))
        print("")
        b=int(input("Probabilidad de la persona B: "))
        print("")
        c=int(input("Probabilidad de la persona C: "))

        if(not(a+b+c== 100)):
            RenovarConsola()
            print("Ingrese nuevamente")   
            print("") 
            
    numero = random.randint(1,100)
    
    if numero <= a:
       print("\nPersona A ha sido elegido")
    elif numero <= a + b:
        print("\nPersona B ha sido elegido")
    else:
        print("\nPersona C ha sido elegido")
    
    input("")
    
def VerEstudiante(email:str):

    if (email == est1_email ):
        print("\nNombre: ",est1_nombre,"\n\nFecha: ",est1_fecha_de_nacimiento)
        print("\nBiografia: ",est1_biografía,"\n\nHobbies: ",est1_hobbies)
        if(est1_fecha_de_nacimiento):
            print("\nAños: ",generarEdad(est1_fecha_de_nacimiento))
    if (email == est2_email):
        print("\nNombre: ",est2_nombre,"\n\nFecha: ",est2_fecha_de_nacimiento)
        print("\nBiografia: ",est2_biografía,"\n\nHobbies: ",est2_hobbies)
        if(est2_fecha_de_nacimiento):
            print("\nAños: ",generarEdad(est2_fecha_de_nacimiento))
    if (email == est3_email):
        print("\nNombre: ",est3_nombre,"\n\nFecha: ",est3_fecha_de_nacimiento)
        print("\nBiografia: ",est3_biografía,"\n\nHobbies: ",est3_hobbies)
        if(est3_fecha_de_nacimiento):
            print("\nAños: ",generarEdad(est3_fecha_de_nacimiento))

        


def LimpiarConsola():
    os.system("cls")
    

def PausarPrograma():
    os.system("pause")

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


def generarEdad(fecha:str):
    hoy = datetime.now()
    
    res = datetime.strptime(fecha, "%Y-%m-%d")
    
    edad = ((hoy - res ).days)/365
    
    return int(edad)
    

#Funcion para crear fechas devuelve una fecha    
def CrearFechas():
    """ Devuelve una fecha ejemplo : (2004-02-03) """
    bandera = False
    fecha_devolver=0
    while bandera != True:
        try:
            ahora = datetime.now()

            fecha = datetime.strptime(input("Ingrese una fecha en el formato AAAA-MM-DD: "),"%Y-%m-%d")
            
            fechaLimite= ahora-timedelta(days=365*18)
            fechaInicial = ahora-timedelta(days=365*100)
            
            if(fecha >= fechaInicial and fecha <= fechaLimite):
                fecha_devolver = fecha
                bandera = True
                
        except:
            print("Error fecha invalida")
            os.system("pause")
            bandera = False

    return fecha_devolver.strftime("%Y-%m-%d")


#--------------------------------    

def ValidarLetras():
    letra=str(input("Ingrese una opción: "))
    while (letra!="a") and (letra!="b") and (letra!="c"):
        print("Error, debe elegir una letra del menú")
        letra=str(input("Ingrese una opción: "))
    return letra  


def CambiarCampos(campo:str,valor:str):
    # NOMBRE
    global est1_nombre,est2_nombre,est3_nombre
    
    #FECHA DE NACIMIENTO
    global est1_fecha_de_nacimiento,est2_fecha_de_nacimiento,est3_fecha_de_nacimiento

    #BIOGRAFIA 
    global est1_biografía,est2_biografía,est3_biografía
    
    #HOBBIES
    global est1_hobbies,est2_hobbies,est3_hobbies
    
    match (campo):
        case ("nombre"):
            if(est1_email ==email_aut): 
                est1_nombre = valor
            if(est2_email ==email_aut): 
                est2_nombre = valor
            if(est3_email ==email_aut): 
                est3_nombre = valor
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
                est2_hobbies = valor
            if(est3_email ==email_aut): 
                est3_hobbies = valor
            
#------------- VALIDACIONES #
def EditarDatosPersonales():

    def RenovarConsola():
        menu_reutilizable = "\n1-Nombre\n\n2-Fecha de nacimiento\n\n3-Biografia\n\n4-Hobbies\n\n0-Volver"
        LimpiarConsola()
        CrearTitulo("Configuración de perfil")
        VerEstudiante(email_aut)
        print("")
        print(menu_reutilizable)
        print("\n¿Que desea modificar? \n")
        
    
   
    RenovarConsola()
    opcion = ValidarRangoDeNumero(0,4)
    while opcion != 0:
        match (opcion):
            case (1):
                nombre=input("Ingrese su nombre deseado: ")  
                CambiarCampos("nombre",nombre)
            case (2):
                fecha = CrearFechas()
                CambiarCampos("fecha",fecha)
            case (3):
                biografia=input("Ingrese su nueva Biografia: ")
                CambiarCampos("biografia",biografia) 
            case (4):
                hobbie=input("Ingrese sus hobbies: ")
                CambiarCampos("hobbie",hobbie)

        RenovarConsola()
        opcion = ValidarRangoDeNumero(0,4)

            

def EliminarPefil():
    print("En construcción")

def GestionarMiPerfil():
    menu_reutilizable="\na-Editar mis datos personales\n\nb-Eliminar mi perfil\n\nc-Volver\n"
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
        print(menu_reutilizable)
        opcion=ValidarLetras()

   
def GestionarCandidatos():
    LimpiarConsola()
    CrearTitulo("GESTIONAR CANDIDATOS")
    print("\na-Ver candidatos\n","\nb-Reportar un candidato\n","\nc-volver\n")
    opcion=ValidarLetras()
    while opcion != "c":
        match (opcion):
            case ("a"):
                VerCandidatos()
            case ("b"):
                Contruccion()

        LimpiarConsola()
        CrearTitulo("GESTIONAR CANDIDATOS")
        print("\na-Ver candidatos\n","\nb-Reportar un candidato\n","\nc-volver\n")
        opcion=ValidarLetras()
        
    
    print("\na-Ver Candidato\n\nb-Reportar un candidato\n\nc-Volver\n")
 

#VER DESPUES POR DOBLE MENU DE OPCION
def VerCandidatos():
    participantes = False
    LimpiarConsola()
    
    if(est1_email !=  email_aut and est1_nombre != ""):      
        CrearTitulo("Estudiante 1")
        VerEstudiante(est1_email)
        participantes=True    
            
    if(est2_email != email_aut and est2_nombre != ""):
        CrearTitulo("Estudiante 2")
        VerEstudiante(est2_email)   
        participantes=True    
        
    
    if(est3_email != email_aut and est3_nombre != ""):
        CrearTitulo("Estudiante 3")
        VerEstudiante(est3_email)
        participantes=True    
    
    if(not(participantes)):
        CrearTitulo("Proximamente candidatos disponibles")
        print("")
        PausarPrograma()
    else:
        megusta=""
        nombre = input("\nIngrese el participantes con el que desea hacer match: ")
        while megusta == "" and nombre != "0":
            # ALEJO 
            if (est1_email != email_aut) and (est1_nombre == nombre):
                print("Le diste like a ",est1_nombre)
                megusta= est1_nombre
            #ALEJO 
            if (est2_email != email_aut) and (est2_nombre == nombre):
                print("Le diste like a ",est2_nombre)
                megusta= est2_nombre
                
            if (est3_email != email_aut) and (est3_nombre == nombre):
                print("Le diste like a ",est3_nombre)
                megusta= est3_nombre
                
            nombre = input("\nIngrese el participantes con el que desea hacer match [0-Salir]: ")
            

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
        
        email = input("Ingrese el email: ")
        contraseña = getpass("Ingrese una contraseña: ")
        
        
        #PRIMER CASO | ESTUDIANTE 1
        if (email == est1_email ) and (contraseña == est1_contraseña):
            autenticado= True
         
        #SEGUNDO CASO | ESTUDIANTE 2
        elif (email == est2_email) and (contraseña == est2_contraseña):
            autenticado= True
            
        #TERCER CASO | ESTUDIANTE 3
        elif (email ==   est3_email) and (contraseña == est3_contraseña):
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
    LimpiarConsola()
    CrearTitulo("Login")
    print("\n1-Iniciar sesion\n\n2-Ruleta\n\n0-Salir\n\n")
    opc = input("Ingresar opcion: ")
    while opc != "0":
        if(opc == "1"):
            IniciarSesion()
        elif (opc == "2"):
            Ruleta()
        LimpiarConsola()
        CrearTitulo("Login")
        print("\n1-Iniciar sesion\n\n2-Ruleta\n\n0-Salir\n\n")
    
        opc = input("Ingrese una nueva opcion: ")
    



    


Inicializacion() 

    
    

