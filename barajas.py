import random
import system
system."cls"
class Carta():
	PALO = ["ORO", "ESPADA", "COPA", "BASTO"]
	VALOR = [1, 2, 3, 4, 5, 6, 7, 10, 11, 12]

	def _init_ (self,numero, palo):
		self.numero = numero
		self.palo = palo

	def_str_ (self):
		return (self.VALOR[self.numero] + "de" + self.PALO[self.palo])


class Baraja():

	def _init_ (self):
		self.cartas = []

		for i in range(4): #Por cada palo
			for j in range(10):#Por cada valor
				self.cartas.append(Carta(numero, palo))
	


	def barajar():
		nCartas = len(self.cartas)
		for i in range (nCartas):
			j = random.randrange(i, nCartas)
		self.cartas [i], self.cartas[j] = self.cartas[j], self.cartas[i]

	def siguienteCarta():

	def cartasDisponibles():

	def darCartas(self):
		cartasDar = int(input("¿Cuántas cartas desea? Indique un número: "))
		for i in range(cartasDar):
			return self.cartas.pop()

	def cartasMonton():

	def mostrarBaraja(self):
		for carta in self.cartas:
			print (carta)


