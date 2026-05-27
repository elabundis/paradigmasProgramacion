def minusculas(linea):
    """Esta función toma una linea de texto (string) y transforma todos los
    carácteres a minúsculas (regresa un string)

    """
    pass

def limpiar_linea(linea):
    """Esta función acepta una línea de texto (str) y regresa un nuevo string
    sin caracteres especiales (.,?!*/).
    El módulo string de la librería estándar de python contiene estos
    caracteres si los desean. Los incluyo al principio de su código.

    """
    from string import punctuation

def obtener_tokens(linea):
    """Esta función recibe una línea de texto y la transforma en una lista
    cuyos elementos son las palabras en la linea.

    """
    pass

def limpiar_tokens(tokens, stopwords):
    """Esta función recibe una lista de palabras (tokens) y elimina aquellas
    que se encuentren en la lista de stopwords (regresa lista de palabras sin
    stopwords).

    """
    pass

def preprocesar_linea(linea):
    """Esta función aplica las funciones anteriores a una línea de texto
    (string). Debe regresar tokens limpios (lista de strings).

    """
    pass

def preprocesar_libro(libro):
    """Aplica preprocesar_linea a cada linea de un libro. El libro consiste en
    una lista, donde cada elemento es una linea del libro.

    Debe regresar una lista de listas. Las listas interiores son los tokens
    limpios de cada línea.
    """
    pass

def leer_libro(filename):
    """Dado el nombre de un archivo, debe leer línea a línea agregandolas a una
    lista, es decir, debe regresar una lista cuyos elementos son las líneas.
    """
    pass
