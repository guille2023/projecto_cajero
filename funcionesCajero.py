import os

saldo = float(83459)
saldoDolar = float(100)
saldoActual = float(0)
tna = float(0.75)
emp = []



def presentacion():
    print("♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦  ♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦  ♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦\n")
    print("\t\t\t\tHola Bienvenido al cajero de codo a codo \n")
    print("ingresa tu clave para acceder a tu cuenta \n la clave es 1234 ")
    return print("♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦  ♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦  ♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦\n")




def menu(nombre):
    print("#########################################")
    print("Bienvenido a tu cuenta", nombre, "!!")
    print("#########################################")
    print("seleciona una opcion y presiona lo Enter: ")
    print("#########################################")
    print("     #1  consultar saldo")
    print("     #2  depositar dinero")
    print("     #3  extraer dinero")
    print("     #4  transferir dinero")
    print("     #5  comprar dolares")
    print("     #6  vender dolares")
    print("     #7  consultar CBU")
    print("     #8  simulador plazo fijo")
    print("     #9  ultimos movimientos")
    print("     #10  salir de la cuenta")
    return print("#########################################")


# 1- consultar saldo y saldo en dolares 
def saldoActual():
    global saldo
    global saldoDolar
    print("♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣\n")
    print("tu saldo actual en pesos es: $" ,saldo, "\n")
    print("tu saldo actual en dolares es: u$S" ,saldoDolar, "\n")
    return print("♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣\n")



# 2- depositar dinero
def depositar():
    print("♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣\n")
    global saldo
    
    ingreso = int(input("digite por teclado el monto de su dinero a ingresar y luego inserte su dinero: "))
    saldo += ingreso
    emp.append(f"deposito $ {ingreso}")  # esta la utilizo para guardar los movimientos
    
    print("--Gracias por ingresar su dinero, su saldo actual es de: $",saldo, "--\n")
    return print("♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣")


# 3- extraer de la cuenta
def extraer():
    print("♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣\n")
    global saldo

    extraccion = int(input("ingresa el monto a extraer: "))
    if (saldo > extraccion) and (extraccion >= 500):
        emp.append(f"retiro $ -{extraccion}")  # esta la utilizo para guardar los movimientos
        saldo -= extraccion

        print("gracias por extraer, tu saldo restante es: $", saldo )
        return print("♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣\n")
    elif(saldo >= extraccion) and (extraccion < 500):
        return print("el retiro minimo es de 500\n")

    else:
        return print("saldo insuficiente ")


# 4- transferir dinero
def transferi(tranferir,monto):
    print("#########################################################\n")

    global saldo
    print("Estas por realizar una transferencia al numero de cuenta ", tranferir , "con el siguiente monto: ", monto )
    print("estas seguro que deseas realizar esta accion ?\n")

    print("#########################################################\n")
    if( saldo >= tranferir ):
        emp.append(f"Transferencia $ -{monto}") # esta la utilizo para guardar los movimientos
        saldo -= monto
        confirmar = str(input("ingresa: \n     # si para confirmar la transferencia. \n     # no para cancelar: \n "))
        if confirmar == "si":
            print("gracias tu tranferencia ha sido realizada!, tu saldo actual es de: $" , saldo )
        elif confirmar == "no":
            print("has cancelado tu transferencia")
        else:
            print("has ingresado un valor invalido")
    else:print("saldo insuficiente")            

# 5- comprar dolares
def comprarDolares():
    global saldo
    print("#####################################")
    print("    el precio del dolar es de $160")
    print("    tu saldo es : $" , saldo)
    return print("#####################################")



def comprarDolares1(compraDolar):
    print("#####################################")

    global saldo
    global saldoDolar
    print("estas seguro de comprar : u$s" , compraDolar, " dolares ?")
    confirma  = str(input("ingresa \n     #si para confirmar. \n     #no para cancelar "))
    print(" ")
    if confirma == "si":
        conversion = compraDolar * 160
        saldo = saldo - conversion
        if(saldo >= 0):
            emp.append(f"Compra dolares $ -{saldo}")  # esta la utilizo para guardar los movimientos
            saldoDolar = saldoDolar + compraDolar
            print("#####################################################")

            print("tu saldo en tu cuenta pesos es de: $" , saldo)
            print("tu saldo en tu cuenta dolares es de: u$s" , saldoDolar )

            return print("#####################################################")
            
            
            
        else: saldo = saldo + conversion 
        print("#####################################################")

        print("tu saldo en tu cuenta dolares es de: u$s" , saldoDolar )
        print("tu saldo en tu cuenta pesos es de: $" , saldo)

        print("#####################################################")

        return print("saldo insuficiente para comprar dolares ")



    elif confirma == "no":
        return print("has cancelado tu compra")       

# 6- vender dolares
def venderDolares(venderDolar):
    global saldo
    global saldoDolar
    print("#####################################")
    print("estas seguro de vender : u$s" , venderDolar, " dolares ?")
    confirma  = str(input("ingresa \n     #si para confirmar. \n     #no para cancelar "))
    print(" ")
    if confirma == "si":
        if( venderDolar <= saldoDolar):
            
            conversion = venderDolar * 155
            saldo += conversion
            emp.append(f"Vender dolares $ {saldo}") # esta la utilizo para guardar los movimientos
            saldoDolar = saldoDolar - venderDolar
            print("#####################################################")

            print("tu saldo en tu cuenta pesos es de: $" , saldo)
            print("tu saldo en tu cuenta dolares es de: u$s" , saldoDolar )

            return print("#####################################################")        

        else: 
            print("#####################################################")

            print("tu saldo en tu cuenta dolares es de: u$s" , saldoDolar )
            print("tu saldo en tu cuenta pesos es de: $" , saldo)

            print("#####################################################")

            return print("saldo insuficiente para vender dolares ")

# 7- consultar cbu
def consultarCbu():
    print("♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦  ♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦  ♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦\n")
    print("Numero de CBU: " ,2850590 ,1907000, 12345678,"\n")
    return print("♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦  ♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦  ♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦\n")
    


# 8- crear plazo fijo en pesos

def simularPlazoFijo(plazoFijo,cantidaDia):
    global tna

    print("♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦  ♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦  ♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦\n")
    print("Este es un simulador de plazo fijo\n")
    print(f"LA TASA NOMINAL ANUAL ES DE: % {tna*100}\n")
    print ("El monto minimo a invertir es de 1000 pesos \n")



    if (plazoFijo >= 1000) and (cantidaDia >= 30):
        porcentajePlazo = tna * (cantidaDia /365)
        gananciaPLazo = plazoFijo * porcentajePlazo + plazoFijo

        print("♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦  ♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦  ♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦\n")
        print(" Monto a invertir en pesos: $",plazoFijo)
        print("Durante ",cantidaDia," dias")
        print("La ganancia Total es de: $",round(gananciaPLazo, 2))  
        return print("♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦  ♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦  ♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦")
    
    elif(plazoFijo < 1000) and (cantidaDia >= 30):
        return print("Error, Ingrese un monto mayor a 1000")

    else: print("Error, La cantidad de dias es inferior a 30 dias")



# 10- ultimos movimientos
def ultimoMovimientos():
    global emp
    print("♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦  ♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦  ♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦\n")
    print("ULTIMOS MOVIMIENTOS\n")
    for i in reversed(emp):

        print(i)

# limpiar pantalla
cls = lambda: os.system ("cls")

# funcion lambda esperar
esperar = lambda:type(input("presione enter para continuar......"))