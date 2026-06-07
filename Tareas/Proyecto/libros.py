from pathlib import Path
from string import punctuation


class Libro:
    def __init__(self, name, filename) -> None:
        """Crear atributos públicos """
        self.name = name
        self.filename = filename
        self.CARACTERES_ESPECIALES: str | None = None
        self.STOPWORDS: list[str] | None = None
        # hacer que estos atributos sean de tipo property (al setter hay que
        # incluirle validación)
        # @property
        # def name(self):
        #    ...
        # @name.setter
        # def name(self, value):
        #     """Checar que el nombre sea un string"""
        #     ...

        # @property
        # def filename(self):
        #    ...
        # @filename.setter
        # def filename(self, value):
        #     """Checar que el nombre sea un string y que el archivo existe"""
        #     ...

    def _limpiar_linea(self, linea):
        """Este método toma una línea de texto (str) y elimina los caracteres
        en `self.CARACTERES_ESPECIALES`.

        """
        pass

    def _limpiar_tokens(self, tokens):
        """Este método recibe una lista de palabras (`tokens`) y elimina
        aquellas que se encuentran en `self.STOPWORDS` modificando la lista
        original. (regresa lista de palabras sin stopwords)

        """
        pass

    def _preprocesar_linea(self, linea) -> list[str]:
        """Limpia una línea de texto regresando tokens  limpios. La limpieza
        debe considerar eliminar espacios blancos al principio y final de la
        línea, convertir a minúsculas, eliminar caracteres especiales, crear
        tokens y eliminar stopwords en estos tokens.

        Este método debe aplicar los métodos anteriores donde sea necesario.
        Debe regresar tokens limpios (lista de strings).

        """
        # eliminar espacios blancos al principio y final de la línea

        # convierte la linea a minúsculas

        # elimina los caracteres especiales

        # obten tokens: transforma la linea en una lista de palabras

        # limpia la lista de tokens
        pass


    def leer_libro(self) -> list[str]:
        """Lee cada línea del libro en `self.filename`, agregando aquellas que
        no esten vacías a una lista, es decir, debe regresar una lista cuyos
        elementos son las líneas no vacías del libro (el primer elemento es la
        primer línea no vacía y así sucesivamente).

        """
        pass

    def preprocesar_libro(self) -> dict[str, int]:
        """Regresa un diccionario de palabras relevantes del libro como llaves
        (los tokens limpios) y sus respectivas frecuencias como valores. Por
        ejemplo, puede regresar:
            {'shrek': 55, 'fiona': 43, 'caminando': 8}

        Para hacer esto, aplica `preprocesar_linea` a cada linea del `libro`
        agregando cada token limpio con un valor de 1 al diccionario si la
        palabra no existe o aumentado el contador de la palabra correspondiente
        en caso contrario.

        """
        pass

    def __str__(self) -> str:
        """Regresa la representación de este objeto en forma de un string.

        Esta es una representación informal que tiene como objetivo que el
        objeto sea entendible para el usuario cuando utilizamos `print` (esta
        función se ejecuta cuando utilizamos ese comando).

        Ver archivo: `Codes/clase_grupo.py` para un ejemplo.

        O bien puedes ver:
          https://realpython.com/python-classes/#special-methods-and-protocols

        """
        pass

    def __repr__(self) -> str:
        """Regresa la representación formal del objeto.

        En esta función regresamos un string que tome la forma en la que
        creariamos esta instancia.

        Ver archivo: `Codes/clase_grupo.py` para un ejemplo.

        O bien puedes ver:
          https://realpython.com/python-classes/#special-methods-and-protocols

        """
        pass

# Los libros del proyecto Gutenberg empiezan dando información sobre el
# copyright y los créditos. El contenido se encuentra después de una línea que
# inicia con `*** START` y antes de la linea `*** END`. Esto debe
# considerarse al momento de leer el libro. Por lo tanto, reescribimos el
# método copprespondiente.
class LibroGutenberg(Libro):
    def leer_libro(self) -> list[str]:
        """Lee cada línea del libro en `self.filename`, agregando aquellas que
        no esten vacías a una lista. Además, empieza a agregar solo despues de
        la línea que comienza con `*** START` y antes de la línea `*** END`.

        (Debe regresar una lista cuyos elementos son las líneas no vacías del
        libro que se encuentran entre las líneas `*** START` y `*** END`.)

        """
        pass

# Los libros en distintos idiomas tienen distintos `STOPWORDS`.
class LibroEnglish(LibroGutenberg):
    def __init__(self, name, filename) -> None:
        super().__init__(name, filename)
        # Agregar aquí los STOPWORDS en ingles (utiliza nltk).
        # (No ocupas hacer nada más que eso)
        # self.STOPWORDS = ...

class LibroSpanish(LibroGutenberg):
    def __init__(self, name, filename) -> None:
        super().__init__(name, filename)
        # Agregar aquí los STOPWORDS en español (utiliza nltk).
        # (No ocupas hacer nada más que eso)
        # self.STOPWORDS = ...

class LibroFrench(LibroGutenberg):
    def __init__(self, name, filename) -> None:
        super().__init__(name, filename)
        # Agregar aquí los STOPWORDS en francés (utiliza nltk).
        # (No ocupas hacer nada más que eso)
        # self.STOPWORDS = ...

# La siguiente función asume que todos los libros se encuentran en el
# directorio `directory`, tienen extensión `txt` y todos son en inglés.
def crear_lista_libros_ingles(directory: str, caract_especiales=punctuation):
    """Crea una lista de instancias `LibroEnglish` a partir de libros
    localizados en `directory`.

    No ocupas modificar esta función, se encuentra ya implementada.

    """
    libros = []
    path = Path(directory)
    for file in path.glob('*.txt'):
        filename = str(file.relative_to(path.parent))
        libro = LibroEnglish(file.name, filename)
        libro.CARACTERES_ESPECIALES = caract_especiales
        libros.append(libro)
    return libros

