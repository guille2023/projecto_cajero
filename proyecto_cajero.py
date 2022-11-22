
from  funcionesCajero import *
import os


def main():
    
        
    presentacion()
        
    clave = int(input("ingresa tu clave: "))
    nombre = str(input("ingresa tu nombre: "))
    
    cls()
    if clave == 1234:

        
        opcion = 0
        while opcion < 10:
            menu(nombre)

            opcion = int(input("ingresa tu opcion: "))
            cls()


            #1consultar saldo
            if opcion == 1:
                
                saldoActual()
        
                esperar()
                cls()

            #2depositar dinero
            elif opcion == 2:
                
                depositar()
                

                esperar()
                cls()
            #3extraer dinero
            elif opcion == 3:

                extraer()

                esperar()
                cls()

            #4transferir dinero
            elif opcion == 4:
                tranferir = int(input("ingrese el cbu de la cuenta a la cual deseas tranferir: "))
                monto = int(input("ingresa el monto a tranferir: "))
                
                transferi(tranferir,monto)
                esperar()
                cls()

            #5comprar dolares
            elif opcion == 5:
                comprarDolares()

                compraDolar = float(input("ingresa el monto de dolares a comprar: "))


                comprarDolares1(compraDolar)      

                esperar()
                cls()


            #6vender dolares
            elif opcion == 6:

                venderDolar = float(input("ingresa el monto de dolares a vender: "))
                venderDolares(venderDolar)

                esperar()
                cls()

            #7 consultar CBU
            elif opcion == 7:
                consultarCbu()

                esperar()
                cls()

            # 8 simulador de plazo fijo en pesos
            elif opcion == 8:
                
                
                plazoFijo = float(input("Ingresa el monto a invertir en plazo fijo: "))
                print("♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦  ♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦  ♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦\n")

                
                print("El tiempo minimo es de 30 dias")

                cantidaDia = int(input("Durante cuanto dias: \n"))
                print("♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦  ♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦  ♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦\n")
                

                simularPlazoFijo(plazoFijo, cantidaDia)

                esperar()
                cls()

            #9ver ultimos movimientos
            elif opcion == 9:
                ultimoMovimientos()
                
                print("")
                esperar()
                cls()

            #10salir de la cuenta
            elif opcion == 10:
                pass
    else:
        print("clave incorrecta")
    print("========================================================\n")
    print("Gracias por utilizar los servicios del cajero automatico \n")
    print("========================================================")


if __name__ == '__main__':
    main()




# 1- utilice dos modulos una para las funciones y otro para el programa principal
# 2- reorganize y cree funciones para que el programa principal sea mas limpio en codigo
# 3- reescribi  la funcion extraer para que no quede un saldo negativo y tenga un monto minimo de retiro
# 4- reescribi la funcion tranferi para que no transfiera mas dinero del que tiene
# 5- reescribi la funcion comprar dolares1 para que no compre de lo que le permite el saldo
# 6- cree la funcion vender dolares, con la condicion de que no venda mas dolares del que tiene en la cuenta
# 7- creo la funcion consultar CBU
# 8- en este caso solo cree un funcion que simula un plazo fijo. defini a tna como variable global .
# 9- creo una funcion lambda para limpiar la pantalla. solo funciona para widonws en caso de otros S.O hay que reescribirla
# 10- elimine la opcion de elegir idioma , ya que me parecio que es reescribir codigo
# 11- agrego un iterador while , para interartuar con el programa
# 12- agrego la funcion salir del programa
# 13- creo una funcion lambda esperar para que la interaccion con el programa no sea tan brusco
# 14- utilizo git 
# 15- Creo variables globales 
# 16- creo la funcion ultimos movimientos
# 17- reeplazo la funcion principal cajero x main