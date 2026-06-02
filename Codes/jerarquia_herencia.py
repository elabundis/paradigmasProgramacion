class Animal:
    def __init__(self, nombre, sexo, habitat):
        self.nombre = nombre
        self.sexo = sexo
        self.habitat = habitat

class Mamifero(Animal):
    caracteristica_unica = "Glándulas mamarias"

class Ave(Animal):
    caracteristica_unica = "Plumas"

class Pez(Animal):
    caracteristica_unica = "Branquias"

class Perro(Mamifero):
    def caminar(self):
        print("El perro está caminando")

class Gato(Mamifero):
    def caminar(self):
        print("El gato está caminando")

class Aguila(Ave):
    def volar(self):
        print("El águila está volando")

class Tiburon(Pez):
    def nadar(self):
        print("El tiburón está nadando")
