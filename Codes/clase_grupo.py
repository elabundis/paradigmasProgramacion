import matplotlib.pyplot as plt
import numpy as np


class Estudiante:
    """Documentación de la clase"""
    num_estudiantes: int = 0
    def __init__(self, name:str):
        type(self).num_estudiantes += 1
        self.name = name
        self._id = type(self).num_estudiantes  # privada de solo lectura
        self.calificaciones = []

    # Este es el getter para el atributo name
    @property
    def name(self):
        return self._name

    # Este es el setter para el atributo name
    @name.setter
    def name(self, value: str):
        self._name = value.lower()

    # Hacer el id de solo lectura! (no defino un setter)
    @property
    def id(self):
        return self._id

    # No permitir crear una nueva lista, solo modificarla (no defino un setter)
    @property
    def calificaciones(self):
        return self._calificaciones

    @calificaciones.setter
    def calificaciones(self, value) -> None:
        calif = []
        for elem in value:
            elem = float(elem)
            if elem < 0: raise ValueError(f'valores deben ser positivos: {elem}')
            calif.append(elem)
        self._calificaciones = calif

    def agregar_calif(self, calificacion):
        """Docstring de función"""
        # assert isinstance(calificacion, (int, float)) and calificacion >= 0,  "calificacion debe ser un número"
        while True:
            try:
                calificacion = float(calificacion)
                if calificacion < 0: raise ValueError
                break
            except ValueError:
                calificacion = input('Introduzca calificación con un número no negativo: ')
        self.calificaciones.append(calificacion)

    def obtener_promedio(self):
        try:
            promedio = sum(self.calificaciones)/len(self.calificaciones)
            return promedio if promedio >= 5 else 5.0
        except ZeroDivisionError:
            msg = f'Debe agregar calificaciones a estudiante: {self.name}'
            return ZeroDivisionError(msg)

    def __add__(self, other):   # método llamado por `+`
        if not isinstance(other, type(self)):
            raise TypeError(f"{'type(self)' and 'type(other)'}")
        grupo = Grupo('')
        grupo.estudiantes = [estudiante for estudiante in (self, other)]
        return grupo

    def __str__(self):   # método llamado por función `print`
        return f'{self.name}'

    def __repr__(self):  # método llamdo por funcion `repr`
        return f"{type(self).__name__}('{self.name}')"


class Grupo:
    def __init__(self, name: str):
        self.name = name
        self.estudiantes = []

    @property
    def estudiantes(self):
        return self._estudiantes

    @estudiantes.setter
    def estudiantes(self, value: list[Estudiante]):
        if not isinstance(value, list):
            raise TypeError('estudiantes se deben dar en una lista')
        elif len(value) > 0 and not isinstance(value[0], Estudiante):
            raise ValueError('debes agregar objetos de tipo Estudiante')
        self._estudiantes = value

    def agregar_estudiante(self, estudiante) -> None:
        msg = 'ingresa objeto de clase Estudiante'
        assert isinstance(estudiante, Estudiante), msg
        self.estudiantes.append(estudiante)

    def historial_estudiante(self, estudiante):
        calif = estudiante.calificaciones
        plt.figure()
        plt.plot(calif, 'o--r')  #  marcador, estilo de linea, color
                                 # Si solo grafico una variable esta se toma
                                 # como el eje `y`,
                                 # el eje `x` toma valores 0, 1, ..., hasta el
                                 # último punto.
        plt.show()

    def ver_resultados(self):
        promedios = []
        for estudiante in self.estudiantes:
            promedios.append(estudiante.obtener_promedio())
        plt.figure()
        bins = np.linspace(4.5, 10.5, 7)  # (start, end, num) Este método si
                                          # toma el valor `end` por default
                                          # (6 bins implican 7 coordenadas)
        params_hist = dict(bins=bins, color='skyblue', edgecolor='black',
                           alpha=0.7)

        plt.hist(promedios, **params_hist)
        plt.xlabel('Calificaciones')
        plt.ylabel('Frequencia')
        plt.title(f'Grupo: {self.name}')

    def __contains__(self, item) -> bool:  # método correspondiente a keyword in
            # Aquí podemos agregar la lógica deseada regresando al final un
            # booleano.
            #
            # Quizás tu desearías implementar que un estudiante se encuentra en
            # el grupo si su nombre se encuentra entre los nombres de los
            # estudiantes. En mi caso decidí checar si el objeto de tipo
            # Estudiante se encuentra en self.estudiantes.
        return item in self.estudiantes

    def __getitem__(self, indice):  # método utilizado para llamar elementos con índices y []
        return self.estudiantes[indice]

    def __iter__(self):   #  metodo que me permite iterar con `for`
        # Podemos crear un objeto iterable de nuestros atributos en un iterador con 'iter'.
        #
        # Otra opción más personalizada es implementar dos métodos: __iter__ y __next__:
        #   __iter__ debe regresar el objeto iterable mismo:
        #       normalmente utilizamos en el cuerpo `return self`
        #   __next__ debe regresar el siguiente elemento en la secuencia y regresar un
        #   excepción StopIteration cuando esta se acabe.
        return iter(self.estudiantes)  # Este método debe regresar un iterador

    def __len__(self) -> int:   # método que se utiliza con la función `len`
        return len(self.estudiantes)


class Universitario(Estudiante):
    num_estudiantes = 0  #  Establesco contador independiente para
                         #  universitarios
    def __init__(self, name: str, universidad: str, facultad: str):
        super().__init__(name)
        self.universidad: str = universidad
        self.facultad: str = facultad

class UniversitarioUAS(Universitario):
    num_estudiantes = 0

    def __init__(self, name: str, facultad: str):
        universidad = 'UAS'
        super().__init__(name, universidad, facultad)

    # Los métodos de clase se utilizan muchas veces para tener más de un
    # constructor. Su primer argumento lo llena Python automáticamente y se
    # refiere a la clase misma (no la instancia). En la comunidad todos solemos
    # llamar a la variable correspondiente `cls`.
    @classmethod
    def desde_secuencia(cls, secuencia):
        """La secuencia debe contener dos argumentos: name y facultad"""
        return cls(*secuencia)

    # Los métodos estáticos no actuan sobre la instancia ni sobre la clase.
    # Podrían colocarse como una función fuera de la clase. Sin embargo, las
    # creamos cuando la función tiene mucha relación con la clase o para
    # empaquetar todo junto o para respetar una API propuesta.
    @staticmethod
    def info_servicio_social() -> None:
        info = ('Listado de lugares para realizar tu servicio social:\n'
                '...\n\n'
                'Duración servicio:\n'
                '...')
        print(info)


# if __name__ == '__main__':
est1 = Estudiante('Mario')
est2 = Estudiante('Karla')
est3 = Estudiante('Rosa')
est4 = Estudiante('Juan')

est1.calificaciones = [7.5, 9.2]
est1.agregar_calif(8)
est2.agregar_calif(10)
est3.agregar_calif(9)
est4.calificaciones = [8, 9, 10]

mi_grupo = Grupo('4-2')
mi_grupo.estudiantes = [est1, est2]
mi_grupo.agregar_estudiante(est3)
mi_grupo.agregar_estudiante(est4)
# print(mi_grupo.estudiantes)
# mi_grupo.historial_estudiante(est1)

est_UAS = UniversitarioUAS('Lisa', 'Informática')
est_UAS_2 = UniversitarioUAS.desde_secuencia(['Bart', 'Musica'])

