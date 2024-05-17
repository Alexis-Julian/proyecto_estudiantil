#24) Se tienen los siguientes datos de las N cuentas de un banco:
#- Número de cuenta
#- Tipo de cuenta (A: caja de ahorros; C: cuenta corriente)
#- Saldo
#Se quiere saber:
# • Promedio de saldos las cajas de ahorros y promedio de las cuentas corrientes
# • Saldo total del banco 




def validarNumCuenta(pepe):
  try:
    int(pepe) 
    return pepe
  except:
    num_cuenta = input("Ingrese un numero de cuenta valido: ")
    return validarNumCuenta(num_cuenta)
    

def validarCuenta() -> str :
    """ ESTO DEVUELVE C O A   """
    tipo_cuenta = input("Tipo de cuenta: [A]-Caja de ahorro : [C]-Cuenta corriente: ")
    while tipo_cuenta.upper() != "A" and tipo_cuenta.upper() != "C":
      tipo_cuenta = input("Error letra incorrecta: [A]-Caja de ahorro [C]-Cuenta corriente: ")
    return tipo_cuenta


def yes_no() -> str:
    opcion = input("ingrese una opcion [Y-Si, N-No]: ").upper()
    print("")
    while opcion != "Y" and opcion != "N":
        opcion = input("error, ingrese una opcion valida [Y-Si, N-No]: ").upper()
        print("")
    return opcion

#CUENTAS AHORRO
sumCA = 0  
promCA = 0
contCA = 0
#CUENTAS CORRIENTE
sumCC= 0
promCC= 0
contCC = 0

#SALDO TOTAL
saldoTotal = 0


print("Desea seguir ingresando cuenta? ")
f = yes_no()
while f == "Y":
  #ESTRUCTURAS#
  num_cuenta = input("Ingrese su numero de cuenta: ")
  num_cuenta= validarNumCuenta(num_cuenta) # VALIDAMOS NUMERO DE CUENTA CON TRY EXCEPT RECURSIVIDAD
  tipo_cuenta  = validarCuenta() # VALIDAMOS TIPO DE CUENTA CON UN WHILE 
  saldo = int(input("Ingrese su saldo: "))
  
  #OPERACIONES
  if(tipo_cuenta=="C" ):
    contCC = contCC + 1 
    sumCC = sumCC + saldo
  else:
    contCA = contCA + 1 
    sumCA = sumCA + saldo
  
  print("Desea seguir ingresando otra cuenta? ")
  f = yes_no()


print("ESTO ES EL SALDO TOTAL",sumCA+sumCC)
print("ESTO ES EL PROMEDIO DE CA: " , sumCA/contCA , "CC",sumCC/contCC)

