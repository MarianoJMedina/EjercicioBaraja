'''NIVEL FACIL'''
'''1'''
print ("BIENVENIDO")
print ("Vamos a ver si sos mayor de edad o no.")
while True:
	edad = int(input("\nIngrese su edad: "))
	if edad < 18:
		print("\nNo sos mayor de edad")
	elif edad >= 18:
		print ("\nSos mayor de edad")
	op = int(input("\n¿Desea continuar? Presione 1-'SI' o 0-'NO': "))
	if op == 0:
		break

'''2'''
print ("BIENVENIDO")
print ("Veamos cómo te fue en el cuestionario")
preg = int(input("\nIngresa la cantidad de preguntas que tuviste: "))
resp = int(input("\nAhora ingresa la cantidad de respuestas correctas que obtuviste: "))
resul = (resp*100)/preg
if resul >= 90:
	print("\nMuy bien, tu resultado es EXCELENTE")
elif resul >= 70:
	print ("\nBien, tu resultado es BUENO")
elif resul >= 60:
	print ("\nNo tan mal, tu resultado es APROBADO")
else:
	print ("\nOh no, tu resultado es NO ALCANZÓ")


'''3''' 
user = input("\nNombre de usuario: ") 
psw = input ("\nContraseña: ")
i = 1
if user == "INFORMATORIO":
	while i <=5:
		if psw == "INFO2020":
			print ("\nBIENVENIDO")
			break
		elif psw != "INFO2020":
			psw = input("\nContraseña incorrecta. Vuelva a ingresar su contraseña: ")
			i+=1
			if i == 5:
				print ("CUENTA BLOQUEADA\nHa alcanzado el máximo numero de intentos")
				break

'''NIVEL MEDIO'''
import os
os.system ("cls")
print ("BIENVENIDO")
print ("Vamos a calcular las ventas de los ultimos dos días")


dia1 = input("\n¿Cuál fué el día que más vendió?:   ")
c1 = int(input("\nIngrese la cantidad de ventas de ese día: "))

os.system ("cls")
dia2 = input("\nAhora, ¿cuál fué el segundo día que más vendió?:  ")
c2 = int(input("\nIngrese la cantidad de ventas de ese día: "))

if c1 > c2:
	print ("\nSe vendió más el día: ",dia1, "con", c1, "ventas")
elif c1 < c2:
	print ("\nSe vendió más el día: ", dia2, "con", c2, "ventas")
else: 
	print ("\nAmbos días vendieron la misma cantidad: ", dia1, "y", dia2, "con", c1, "ventas")

#NIVEL DIFICIL
import os
op = "1"
while op == "1":
	os.system ("cls")
	nom = str(input("Nombre: "))
	print ("Turno: Tarde - Noche - Ninguno")
	tur = str(input("Turno: "))

	if (tur == "Tarde" or tur == "tarde") or (tur == "Noche" or tur == "noche"): 

		if (nom >= "a" and nom < "n") or (nom >= "A" and nom < "N"):
			if (tur == "Noche" or tur == "noche"): 
				print ("\nLe han informado mal")
			print ("\nUsted pertenece al Grupo A del turno Tarde")
		
		else:
			if (tur == "Tarde" or tur == "tarde"):
				print ("\nLe han informado mal")
			print ("\nUsted pertenece al Grupo A del turno Noche")

	elif tur == "ninguno" or tur == "Ninguno":
		print ("\nUsted pertenece al Grupo B")

	op = input("\n¿Desea continuar? 1-(SI) o 0-(NO): ")
	while(op != 1 and op != 0):
		os.system ("cls")
		op = int(input("ERROR\nVuelva a ingresar 1(uno) para SI o 0(cero) para NO: "))