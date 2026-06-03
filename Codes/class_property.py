class Cuad:
    def __init__(self, lado) -> None:
        self.lado = lado

    # getter
    @property
    def lado(self):
        return self._lado

    # setter
    @lado.setter
    def lado(self, value):
        if float(value) <= 0:
            raise ValueError("El lado debe ser un número positivo")
        self._lado = value

# Creando un atributo de solo lectura
class Student:
    def __init__(self, name) -> None:
        self.name = name
        self._id = 5

    # solo defino el getter cuando no deseo permitir escritura
    # (En realidad lo que se evita es escribir mediante self.id = num,
    # aún podiras sobreescribir con self._id = num)
    @property
    def id(self):
        return self._id

