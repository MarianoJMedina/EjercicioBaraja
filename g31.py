'''
Ejercicio 1:
Escribir un programa que reciba una lista de números y devuelva la suma acumulada, es decir, 
una nueva lista donde el primer elemento es el mismo, el segundo elemento es la suma del 
primero con el segundo, el tercer elemento es la suma del resultado anterior con el siguiente 
elemento y así sucesivamente. 
Por ejemplo, la suma acumulada de [1,2,3] es [1, 3, 6].
'''
# Coloque la resolución del Ejercicio debajo de esta línea


'''
Ejercicio 2:
Escriba un programa que permita crear una lista de palabras y que, 
a continuación, pida una palabra y diga cuántas veces aparece esa palabra en la lista.
'''
# Coloque la resolución del Ejercicio debajo de esta línea
import os
os.system ("cls")
print ("Bienvenido")
lista = []
op = "1"
while op == "1": 
	palabra = input("Escriba su palabra a continuación: ")
	lista += [palabra]
	op = input ("\n¿Desea continuar escribiendo? 1-(SI) o 0-(NO): ")
	while(op != "1" and op != "0"):
		os.system ("cls")
		op = input("ERROR\nVuelva a ingresar 1(uno) para SI o 0(cero) para NO: ")
os.system ("cls")
print("La lista creada es:", lista)

busca = input ("\nAhora, escriba una palabra y la buscaremos en la lista: ")
if busca in lista:
	contpalabra = lista.count(busca)
	os.system ("cls")	
	print ("Se encontro la palabra en la lista ! \nLa palabra aparece",contpalabra,"veces en la lista.")
else:
	os.system ("cls") 
	print ("No se encontro la palabra en la lista creada")
	op2 = input ("¿Desea agregarla? 1-(SI) o 0-(NO): ")
	while(op != "1" and op != "0"):
		os.system ("cls")
		op = input("ERROR\nVuelva a ingresar 1(uno) para SI o 0(cero) para NO: ")
	if op2 == "1":
		palabra = input("Escriba su palabra a continuación: ")
		lista += [palabra]
		os.system ("cls")
		print ("Palabra agregada")
	elif op2 == "0": 
		os.system ("cls")
		print ("Hasta luego :)")
