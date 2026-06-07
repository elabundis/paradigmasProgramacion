class Recomendador:
    def __init__(self, libros) -> None:
        """
        libros: lista con instancias de tipo `Libro`
        """
        self.libros = libros
        self._pesos = None  # Se calcularan con un setter (ver `set_pesos`)

    def set_pesos(self) -> None:
        """Calcula los pesos del algorítmo TF-IDF requeridos para las
        recomendaciones y los guarda en `self._pesos`

        """
        pass

    def get_pesos(self):
        """Regresa los pesos calculados"""
        pass

    def _producto_punto(self, idx_1:int, idx_2:int) -> float:
        """Producto punto entre los libros con índices idx_1 y idx_2."""
        pass

    def _similitud(self, idx_1, idx_2) -> float:
        """Similitud entre los libros con índices idx_1 y idx_2 de acuerdo al
        coseno del ángulo que forman sus vectores.

        """
        pass

    def mostrar_libros(self):
        """Mostrarle al usuario el índice y nombre para cada libro de acuerdo a
        nuestra lista de libros `self.libros`.

        """
        pass

    def resumen(self, idx_libro, num_palabras) -> list[str]:
        """Regresa una lista con las palabras más representativas de un libro
        de acuerdo a los pesos.

        idx_libro: índice del libro cuyo resumen deseamos.
        num_palabras: número de palabras en el resumen.

        """
        pass

    def libros_similares(self, idx_libro, num_libros) -> list[str]:
        """Regresa una lista con los libros más parecidos a un libro dado.

        idx_libro: índice del libro a partir del cual quiero recomendaciones.
        num_libros: número de libros en mi recomendación.


        """
        pass
