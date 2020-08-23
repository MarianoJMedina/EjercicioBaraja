import os
os.system ("cls")

def Menu():
    print ("""--------------
Calculadora
--------------
Menu
1) Suma
2) Resta
3) Multiplicacion
4) Division
5) Salir""")

def Calculadora():
    Menu()
    opc = int(input("\nSelecione una opción: "))
    while (opc >0 and opc <5):
        os.system ("cls")
        m = int(input("\nIngrese un numero: "))
        n = int(input("Ingrese otro Numero: "))
        if (opc==1):
            os.system ("cls")
            print ("El resultado de la suma es:", m+n)
            Menu()
            opc = int(input("\nSelecione una opción: "))
        elif(opc==2):
            os.system ("cls")
            print ("El resultado de la resta es:",m-n)
            Menu()
            opc = int(input("\nSelecione una opción: "))
        elif(opc==3):
            os.system ("cls")
            print ("El resultado de la multiplicacion es:",m*n)
            Menu()
            opc = int(input("\nSelecione una opción: "))
        elif(opc==4):
            if (n != 0):
                os.system ("cls")
                print ("El resultado de la división es:", m/n)
                Menu()
                opc = int(input("Selecione una opción\n"))
            else:
                os.system ("cls")
                print ("No se permite la división entre 0")
                Menu()
                opc = int(input("\nSelecione una opción: "))
Calculadora()