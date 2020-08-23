''' 
    -----------------------------------------------------------------
    Ejercicio para practicar asignación de datos e 
    impresión de cálculos por pantalla por lo que no
    deben utilizar estructuras de control solo deben solicitar datos
    hacer el calculo e imprimirlo.
    -----------------------------------------------------------------
    EJERCICIO 1: 
    Escribir un programa que pida al usuario dos números enteros y muestre 
    por pantalla la <n> entre <m> da un cociente <c> y un resto <r> donde <n> 
    y <m> son los números introducidos por el usuario, y <c> y <r> son el 
    cociente y el resto de la división entera respectivamente.
'''
# Coloque la resolución del Ejercicio 1 debajo de esta línea
import os
print ("Bienvendo")
n = int(input ("\nIngrese un numero a dividir (Dividendo): "))
os.system ("cls")
m = int(input ("\nAhora, ingrese otro numero (Divisor): "))
os.system ("cls")
print ("\nEstos son tus numeros ingresados: ", n,"como Dividendo y", m, "como Divisor")
print ("\nA continuacion, haremos la division entera de estos numeros: ")
c = n/m
r = n%m
os.system ("cls")
print ("\nEl resultado o cociente de la division es: ", c, "con un resto de: ", r)


'''
    -----------------------------------------------------------------
    Ejercicio simple para practicar Estructuras de control.
    Para resolver este ejercicio deberá utilizar estructuras 
    condicionales.
    -----------------------------------------------------------------
    EJERCICIO 2: 
    Una barra de chocolate de forma rectangular puede ser dividida 
    en n × m porciones. La barra de chocolate se puede dividir en 
    dos partes rectangulares partiéndola a lo largo de una línea 
    recta seleccionada en su patrón. 
    Determine si es posible dividirlo para que una de las partes 
    tenga exactamente 'k' cuadrados.
    El programa lee tres enteros: 'n', 'm' y 'k'. 
    Debe imprimir SÍ se puede dividir o NO se puede dividir.
'''
# Coloque la resolución del Ejercicio 2 debajo de esta línea
import os
print ("\nBienvenido")
print ("\nNotaras que tu barra de chocolate tiene n x m (filas x columnas) cuadraditos o pedacitos de chocolate")
os.system ("cls")
n = int(input("\nIngrese el numero de filas de tu chocolate: \n(Es la cantidad de pedacitos que podes contar en la parte lateral de tu chocolate)\n"))
m = int(input("\nAhora ingrese el numero de columnas: \n(Es la cantidad de pedacitos que podes contar en la parte superior de chocolate)\n"))

if ((n*m)%2 == 0):
    k = (n*m)/2
    os.system ("cls")
    print ("\nSe puede dividir en dos partes iguales con",k,"pedacitos para cada uno")
else:
    os.system ("cls")
    print ("\nNo se puede dividir en pedacitos iguales para cada uno")
'''   -----------------------------------------------------------------
    Ejercicio simple para practicar Estructuras de control.
    Para resolver este ejercicio deberá utilizar estructuras 
    repetitivas.
    -----------------------------------------------------------------
    EJERCICIO 3:
    Crear un programa que solicite el ingreso de números enteros 
    positivos, hasta que el usuario ingrese el 0. Por cada número, 
    informar cuántos dígitos pares y cuántos impares tiene.
    Al finalizar, informar la cantidad de dígitos pares y de dígitos 
    impares leídos en total. 
'''
# Coloque la resolución del Ejercicio 3 debajo de esta línea
import os
os.system ("cls")
print ("Bienvenido")
print ("Oprima cero (0) para finalizar y mostrar los resultados finales")
contpar = 0
contimpar = 0
contparT = 0
contimparT = 0
while True:
    n = int(input("Ingrese un numero positivo: \n"))
    if n == 0: 
        break
    elif (n<0):
        os.system ("cls")
        n = int(input("Error, vuelva a ingeresar un numero positivo: \n"))
    while n > 0:
        c = n%10
        if (c%2==0):
            contpar += 1
            contparT += 1 
        else:
            contimpar += 1
            contimparT += 1
        n//=10
    os.system ("cls")
    print ("Su numero elegido tiene: ", contpar,"numeros pares y tiene", contimpar,"numeros impares")
    c = 0
    contpar = 0
    contimpar = 0
os.system ("cls")
print ("El numero total de numeros pares contados es: ", contparT)
print ("El numero total de numeros impares contados es", contimparT)
'''
    -----------------------------------------------------------------
    Ejercicio Desafío.
    Deberá aplicar las estructuras de control que crea conveniente
    para resolver el ejercicio, puede ser condicional/repetitiva
    o una mezcla de ambas.
    -----------------------------------------------------------------
    EJERCICIO 4: 
    Crear un programa que permita al usuario ingresar los montos de 
    las compras de un cliente (se desconoce la cantidad de datos que 
    cargará, la cual puede cambiar en cada ejecución), cortando el ingreso 
    de datos cuando el usuario ingrese el monto 0.
    Si ingresa un monto negativo, no se debe procesar y se debe pedir 
    que ingrese un nuevo monto. Al finalizar, informar el total a pagar 
    teniendo que cuenta que, si las ventas superan el total de $1000, 
    se le debe aplicar un 10% de descuento.
'''
# Coloque la resolución del Ejercicio 4 debajo de esta línea
import os
os.system ("cls")
print ("BIENVENIDO")
inicio = True
while inicio:
    n = float(input("\nIngrese el monto/precio de su producto: "))
    op1 = int (input("\nPresione el numero 0 para terminar de contar"))
    m += n
    if n < 0:
        n = float(input("\nError. Ingrese nuevamente el monto/precio de su producto",i,": "))
        m += n
    elif op == 0:
        if m >= 1000:
            m -= (m*0.10)
        else:
            print ("Su monto total a pagar es $",m)
    n = 0
    op2 = int(input("\n¿Desea continuar? 1-SI o 0-NO: "))
    if op2 == 0:
        os.system ("cls")
        print ("Hasta luego. Que tenga buen día")
        inicio = False


