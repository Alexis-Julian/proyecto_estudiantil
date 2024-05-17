import getpass
from os import system


nombreu1="juan"
email_usuario1="estudiante1@ayed.com"
contraseña_usuario1="111222"
nombreu2="manuel"
email_usuario2="estudiante2@ayed.com"
contraseña_usuario2="333444"
nombreu3="francisco"
email_usuario3="estudiante3@ayed.com"
contraseña_usuario3="555666"

def clear():
	system("cls")

def login():
	global Mail_ingreso
	contador=2
	print("Hola bienvenido a nuestro programa de matches para compañero de estudio, nombre pendiente a patente")
	print("---------------------------------------------------------------------------------------------------")
	print("Porfavor inicie sesion")
	Mail_ingreso=str(input("mail: "))
	while (Mail_ingreso!=email_usuario1 and Mail_ingreso!=email_usuario2 and Mail_ingreso!=email_usuario3) and contador!=0:
		print("el mail ingresado no es valido")
		contador-=1
		Mail_ingreso=str(input(f"ingrese un mail valido, le quedan {contador+1} intentos: "))
	if contador==0:
		clear()
		print("usted se ha quedado sin intentos")
	elif Mail_ingreso==email_usuario1:
		contraseña_ingreso=getpass.getpass("ingrese su contraseña: ")
		if contraseña_ingreso==contraseña_usuario1:
			menuprin()
			return Mail_ingreso
		if contraseña_ingreso!=contraseña_usuario1:
				while contraseña_ingreso!=contraseña_usuario1 and contador!=0:
					contador=contador-1
					contraseña_ingreso=getpass.getpass(f"contraseña erronea, intente otra vez, le queda {contador+1} intentos: ")
				if contador==0:
					clear()
					print("se acabaron sus intentos, usted no es propietario del usuario, o en todo caso usted es muy olvidadizo")
				if contraseña_ingreso==contraseña_usuario1:
					menuprin()
					return Mail_ingreso
	elif Mail_ingreso==email_usuario2:
		contraseña_ingreso=getpass.getpass("contraseña: ")
		if contraseña_ingreso==contraseña_usuario2:
				menuprin()
				return Mail_ingreso
		if contraseña_ingreso!=contraseña_usuario2:
				while contraseña_ingreso!=contraseña_usuario2 and contador!=0:
					contador=contador-1
					contraseña_ingreso=getpass.getpass(f"contraseña erronea, intente otra vez, le quedan {contador+1} intentos: ")
				if contador==0:
					clear()
					print("se acabaron sus intentos, usted no es propietario del usuario, o en todo caso usted es muy olvidadizo")
				if contraseña_ingreso==contraseña_usuario2:
					menuprin()
					return Mail_ingreso
	elif Mail_ingreso==email_usuario3:
		contraseña_ingreso=getpass.getpass("contraseña: ")
		if contraseña_ingreso==contraseña_usuario3:
			menuprin()
			return Mail_ingreso
		if contraseña_ingreso!=contraseña_usuario3:
				while contraseña_ingreso!=contraseña_usuario3 and contador!=0:
					contador=contador-1
					contraseña_ingreso=getpass.getpass(f"contraseña erronea, intente nuevamente, le quedan {contador+1} intentos: ")
				if contador==0:
					clear()
					print("se acabaron sus intentos, usted no es propietario del usuario, o en todo caso usted es muy olvidadizo")
				if contraseña_ingreso==contraseña_usuario3:
					menuprin()
					return Mail_ingreso

def menuprin():
	clear()
	print("Bienvenido denuevo a la mejor aplicacion para encontrar a tu compañero ideal")
	print(" ")
	print("1-Gestionar perfil")
	print(" ")
	print("2.Gestionar candidatos")
	print(" ")
	print("3-Matcheos")
	print(" ")
	print("4-reportes estadisticos")
	print(" ")
	print("0-Salir")
	print(" ")

	selecion=str(input("a que seccion desea acceder?ingrese el numero correspondiente: "))
	while selecion!="1" and selecion!="2" and selecion!="3" and selecion!="4" and selecion!="0":
		selecion=str(input("introduzca una opcion valida: "))
	if selecion=="0":
		print("en construccion, lo lamento esta atrapado aqui y no te molestes en tratar de volver, tambien esta en construccion")
	elif selecion=="1":
		print("funcion aca")
	elif selecion=="2":
		print("funcion aca")
	elif selecion=="3":
		print("en construccion...")
	elif selecion=="4":
		print("en construccion...")

login()