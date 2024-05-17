

email_usuario1="estudiante1@ayed.com"
contraseña_usuario1=111222
email_usuario2="estudiante2@ayed.com"
contraseña_usuario2=333444
email_usuario3="estudiante3@ayed.com"
contraseña_usuario3=555666

def ValidarContraseña():
	contador = 0
	while contraseña_ingreso!=contraseña_usuario1 and contador != 0:
		contador= contador - 1
		contraseña_ingreso=int(input("contraseña erronea, intente otra vez: "))
		if contador==0:
			print("se acabaron sus intentos, usted no es propietario del usuario, o en todo caso usted es muy olvidadizo")
		if contraseña_ingreso==contraseña_usuario1:
			print("funcion aca")


def Menu():
    print("Menu")


def login(): 
	contador=2
	print("Hola bienvenido a nuestro programa de matches para compañero de estudio, nombre pendiente a patente")
	print("---------------------------------------------------------------------------------------------------")
	print("Porfavor inicie sesion")
	Mail_ingreso=str(input("mail: "))
	while Mail_ingreso!=email_usuario1 and Mail_ingreso!=email_usuario2 and Mail_ingreso!=email_usuario3:
		print("el mail ingresado no es valido")
		Mail_ingreso=str(input("ingrese mail: "))
		if Mail_ingreso==email_usuario1:
			contraseña_ingreso=int(input("contraseña: "))
			if contraseña_ingreso==contraseña_usuario1:
				Menu()
			if contraseña_ingreso!=contraseña_usuario1:
				ValidarContraseña()
					
		elif Mail_ingreso==email_usuario2:
				contraseña_ingreso=int(input("contraseña: "))
				if contraseña_ingreso==contraseña_usuario2:
						Menu()
				if contraseña_ingreso!=contraseña_usuario2:
					ValidarContraseña()
				
					
		elif Mail_ingreso==email_usuario3:
			contraseña_ingreso=int(input("contraseña: "))
			if contraseña_ingreso==contraseña_usuario3:
				Menu()
			if contraseña_ingreso!=contraseña_usuario3:
				ValidarContraseña()
				

