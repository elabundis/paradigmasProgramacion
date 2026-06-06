def limpiar_linea(linea, caracteres_especiales):
    """Esta función toma una línea de texto (str) y un iterable de caracteres
    especiales y regresa la línea sin dichos caracteres (.,?!*/).

    """
    pass

def limpiar_tokens(tokens, stopwords):
    """Esta función recibe una lista de palabras (`tokens`) y elimina aquellas
    que se encuentren en el iterable `stopwords` modificando la lista original.
    (regresa lista de palabras sin stopwords)

    """
    pass

def preprocesar_linea(linea, caracteres_especiales, stopwords) -> list[str]:
    """Limpia una línea de texto regresando tokens  limpios. La limpieza debe
    considerar eliminar espacios blancos al principio y final de la línea,
    convertir a minúsculas, eliminar caracteres especiales, crear tokens y
    eliminar stopwords en estos tokens.

    Esta función debe aplicar las funciones anteriores donde sea necesario.
    Debe regresar tokens limpios (lista de strings).

    """
    # eliminar espacios blancos al principio y final de la línea

    # convierte la linea a minúsculas

    # elimina los caracteres especiales

    # obten tokens: cada palabra debe aparecer como un elemento de una lista

    # limpia la lista de tokens
    pass

def leer_libro(filename) -> list[str]:
    """Dado el nombre de un archivo debe leer cada línea, agregando aquellas
    que no esten vacías a una lista, es decir, debe regresar una lista cuyos
    elementos son las líneas no vacías del libro (el primer elemento es la
    primer línea no vacía y así sucesivamente).

    """
    pass

def preprocesar_libro(
    libro: list[str], caracteres_especiales, stopwords
) -> dict[str, int]:
    """Regresa un diccionario de palabras relevantes del libro como llaves
    (los tokens limpios) y sus respectivas frecuencias como valores. Por
    ejemplo, puede regresar:
        {'shrek': 55, 'fiona': 43, 'caminando': 8}

    Para hacer esto, aplica `preprocesar_linea` a cada linea del `libro`
    agregando cada token limpio al diccionario si la palabra no existe o
    aumentado el contador de palabras correspondiente en caso contrario.

    El libro consiste en una lista con las líneas de este.

    El módulo string de la librería estándar de python contiene estos
    caracteres si los desean. Los incluyo al principio de su código.
    """
    # La siguiente línea puede serte de ayuda
    # from string import punctuation
    pass

