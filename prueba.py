print("Proceso de login")
print("Bienvenido, solo podes ingresar la contraseña hasta 3 veces.")
print("Si ingresas mal la contraseña 3 veces, tu cuenta se bloqueará :(")
num = 17
x = 3
print (num%x)
usuario = input("Nombre usuario: ")
contraseña = input("Contraseña: ")

i = 1

while (i<3) & (contraseña != "INFO2020"):
	print ("Contraseña incorrecta")
	contraseña = input("Ingrese nuevamente su contraseña: ")
	i += 1

if contraseña == "INFO2020":
	print("Loguin correcto\nHola")
else :
	print("Cuenta bloqueada...Te lo dije ")


print ("Bienvendo")
n = int(input ("\nIngrese un numero a dividir (Dividendo): "))
m = int(input ("\nAhora, ingrese otro numero (Divisor): "))
print ("\nEstos son tus numeros ingresados: ", n,"como Dividendo y", m, "como Divisor")
print ("\nA continuacion, haremos la division entera de estos numeros: ")
c = n/m
r = n%m
print ("\nEl resultado o cociente de la division es: ", c, "con un resto de: ", r)


print ("Bienvenido")
print ("Oprima cero (0) para finalizar")
i = 0
contpar = 0
contimpar = 0
contparT = 0
contimpart = 0
while i !=0:
    n = int(input("Ingrese un numero positivo: \n"))
    if (n<0):
        n = int(input("Error, vuelva a ingeresar un numero positivo: \n"))
    m = int(input("Cuantos digitos tiene su numero?: \n"))
    for i in range(m):
        n = n%10
        if (n%2==0):
            contpar += 1
            contparT += contpar 
        else:
            contimpar += 1
            contimparT += contimpar
        n = n/10
    print ("Su numero elegido tiene: ", contpar,"numeros pares y tiene", conimpar,"numeros impares").

print ("El numero total de numeros pares contados es: ", contparT)
print ("El numero total de numeros impares contados es", contimparT)




print ("\nBienvenido")
print ("\nNotaras que tu barra de chocolate tiene n x m (filas x columnas) cuadraditos o pedacitos de chocolate")
n = int(input("\nIngrese el numero de filas de tu chocolate: \n(Es la cantidad de pedacitos que podes contar en la parte lateral de tu chocolate)\n"))
m = int(input("\nAhora ingrese el numero de columnas: \n(Es la cantidad de pedacitos que podes contar en la parte superior de chocolate)\n"))

if ((n*m)%2 == 0):
    k = (n*m)/2
    print ("\nSe puede dividir en dos partes iguales con",k,"pedacitos para cada uno")
else:
    print ("\nNo se puede dividir en pedacitos iguales para cada uno")