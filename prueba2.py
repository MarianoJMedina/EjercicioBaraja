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