class Persona: 
	'Texto para decir que hace esta clase'
	def _init_(self, nombre, edad, genero, estatura, peso): 
		self.nombre = nombre
		self.edad = edad
		self.genero = genero
		self.estatura = estatura
		self.peso = peso

	def hablar (self):
		print("Hola soy {}".format(self.nombre))

	def correr (self): 
		print("{} esta corriendo".format(self.nombre))

	def caminar (self):
		print("{} esta caminando".format(self.nombre))

persona1 = Persona("Juan", 23, "Masculino", 170, 80)
persona2 = Persona("Maria", 25, "Femenino", 150, 50)


