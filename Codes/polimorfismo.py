# Aquí crearé dos clases que comparten su API, dónde los métodos tienen
# comportamientos distintos.
#
# El polimorfismo es la capacidad de objetos pertenecientes a distintas clases
# de ser tratados como instancias de la misma clase base, permitiendo que un
# método tengo su propio comportamiento de acuerdo al objeto que lo llame.
#
# Nos permite utilizar objetos de distinta clase como argumentos en una función
# siempre y cuando compartan la misma interfaz.

# En python exite un tipo de polimorfismo que se conoce como "tipos pato" (duck
# typing; si se mueve como pato y hace como pato, entonces debe ser un pato),
# dónde lo único que nos importa es el comportamiento y la interfaz (no la
# clase ni la herencia). En este tipo de polimorfismo los objetos no son
# forzados a heredar de una super clase común.

# Nota: puedo forzar el polimorfismo utilizando los ABCs, ya que estas forzan
# una misma interfaz, sin embargo, esto no es necesario para definir métodos e
# instancias con los mismos nombres y esto es lo único necesario en el
# polimorfismo.

import numpy as np


class Dado:
    """"
    Una clase que representa un dado.

    Parameters
    ----------
    n : int
        Número de caras del dado

    Attributes
    ----------
    caras : lista de enteros
        Caras del dado.
    """
    def __init__(self, n:int) -> None:
        self.caras = list(range(1, n+1))
    def arrojar_dado(self) -> int:
        return np.random.choice(self.caras)
    def info(self):
        print(f'El dado tiene {len(self.caras)} caras.')

class DadoCargado(Dado):
    def __init__(self, n: int, cara_pesada=1) -> None:
        super().__init__(n)
        self._cara_pesada = cara_pesada
        self._set_prob()
    def arrojar_dado(self) -> int:
        return np.random.choice(self.caras, p=self._probabilidades)
    def info(self):
        super().info()
        print(f'La cara pesada es: {self._cara_pesada}')
    def _set_prob(self):
        n = len(self.caras)
        prob = 1 / (n + 1)
        prob_cara_pesada =  2 * prob
        self._probabilidades = n * [prob]  # lista con probabilidades iguales
        self._probabilidades[self._cara_pesada - 1] = prob_cara_pesada

d1 = Dado(6)
d2 = DadoCargado(6)

for dado in [d1, d2]:
    print(f'arrojar dado: {dado.arrojar_dado()}')
    dado.info()
    print()

