# Ejemplo if True:

a = 5
if a == 2:
    print("a vale 2")
if a == 5:
    print("a vale 5")


a = 5
b = 10
if a == 5:
    print("a vale",a)
    if b == 10:
        print("y b vale",b)


# Ejemplo if else:
n = 50
if n % 5 == 0:
    print(n,"es múltiplo de 5")
else:
    print(n,"no es múltiplo de 5")

#Ejemplo Elif
importe = float(input("Ingresar importe a cobrar: "))

if importe >= 1500:
    print("Descuento 30%")
elif importe >= 1000:
    print("Descuento 20%")
elif importe >= 750:
    print("Descuento 10%")
elif importe >= 500:
    print("Descuento 5%")
else:
    print("No hay Descuentos disponibles")