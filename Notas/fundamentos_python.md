---
geometry: "left=3cm,right=3cm,top=2cm,bottom=2cm"
fontsize: 12pt
---

# Fundamentos de Python

Python es un lenguaje interpretado de alto nivel multiparadigma,
permitiéndonos utilizar un enfoque **orientado a objetos**,
por **procedimientos**,
**funcional** (map, filter, reduce, list comprehension),
e incluso **programación lógica** mediante librerías como
PyKE, kanren, o pyDatalog.
El paradigma a emplear dependerá del problema y conocimientos del programador pero python pone a nuestra disposición todos los paradigmas.

Su implementación fundamental es **CPython**,
la cuál está escrita en **C**.
Esto nos permite escribir y utilizar módulos de extensión en C
(numpy, etc),
es decir,
podemos interactuar fácilmente con código en ese lenguaje.
Sin embargo,
como ya hemos discutido durante el curso,
existen muchas otras implementaciones;
algunas hechas en Java (**Jython**)
otras hechas en python mismo (**PyPy**)
y muchas más.

Este lenguaje es muy utilizado en la inteligencia artificial,
ciencia de datos,
en cálculos científicos,
creación de páginas web,
automatización de tareas,
microcontroladores,
etc.


## Instalación y Ejecución

Ya hemos visto que la herramienta **pyenv** nos permite instalar cualquier versión deseada de **python**
(refiérase al laboratorio 2).
Aquí repasamos el uso fundamental de esta herramienta.


### Utilizando pyenv

#### Instalando versiones de python

Actualizar `pyenv` para que me muestre las versiones mas nuevas:

    pyenv update

Listar versiones de `python` disponibles:

    pyenv install --list | less

Ver versiones 3.13 (CPython):

    pyenv install --list | grep " 3\.13" | less

Ver las implementaciones en Java de Python `jython`

    pyenv install --list | grep "jython"

Para instalar una versión mas reciente de `python3` (CPython) utilizamos

    pyenv install 3

Si deseamos la versión más reciente de `python3.13`

    pyenv install 3.13

O podemos instalar una versión específica con

    pyenv install 3.12.2

Para ver todas las implementaciones instaladas

    pyenv versions

dónde la versión que empieza con asterisco es la que estamos empleando en este momento.
La versión denotada como **system** se refiere a la versión de python preinstalada en tu sistema operativo.

Si solo deseamos ver la versión que estamos utilizando actualmente ejecutamos

    pyenv version

Para desinstalar una implementación tenemos

    pyenv uninstall 3.14.3


#### Cambiando entre versiones

Esta herramienta nos permite establecer una versión global para python mediante

    pyenv global 3.13

También podemos activar versiones locales.
Las versiones locales son aquellas que configuramoe en un directorio y se activan y desactivan automáticamente cuando entramos o salimos de este.
Por ejemplo, crea una carpeta y dentro de esta ejecuta

    pyenv local 3.12.2

Observa qué versión de python tienes al entrar y salir de este directorio con `python --version`.
Observa que la opción `local` crea un archivo en el directorio con nombre **.python-version** dentro del cual se tiene la versión local de python a utilizar. Si eliminamos este archivo se elimina la configuración local.

Por último pyenv nos permite establecer una versión de python para nuestra sesión en el shell sobreescribiendo cualquier ajuste global o local.
Esto lo logramos mediante

    pyenv shell 3.13

Lo que ocurre es que se crea una variable de ambiente
**PYENV_VERSION**
y esta contiene la versión a utilizar con este shell
(puedes verificarlo con `echo 'PYENV_VERSION'`)

Para desactivar esta versión podemos ejecutar

    pyenv shell --unset

o podemos eliminar la variable de ambiente

    unset PYENV_VERSION


#### Obteniendo ayuda

Tenemos algunas alternativas para encontrar ayuda. Podemos ver el manual del programa mediante

    man pyenv

Para ver una ayuda más resumida:

    pyenv --help

Para ver todos los comandos:

    pyenv commands

Si deseamos ayuda con un comando, digamos el comando virtualenv, utilizamos

    pyenv help virtualenv

## HelloWorld

Siguiendo la costumbre de empezar con nuestro programa más básico, aquí mostramos nuestro HelloWorld.
Abrimos el intérprete mediante `python` y dentro de este ejecutamos

    >>> print('HelloWorld!')

Antes de continuar utilicemos un intérprete más avanzado que el que viene de manera estándar con python.
Este se encuentra disponible como una librería y se llama **ipython**.
Siempre que nuestro proyecto vaya a necesitar hacer uso de librerías debemos crear un ambiente virtual.

## Ambientes virtuales

Los ambientes virtuales nos permiten aislar ambientes de programación para que podamos instalar librerías en las versiones que requiramos en distintos proyectos.

El aislamiento se consigue
creando una estructura de directorios por proyecto,
dentro de la cual se almacenan las librerías que instalamos.
Dentro de esta estructura,
se crea una copia o un enlace
(dependiendo del sistema operativo, versión)
al python con que fue creado el ambiente virtual.
Además,
se crean enlaces a módulos y librerías incluidas en la librería estándar de python para que la instalación del ambiente sea ligero y de rápida creación.

Gracias al aislamiento,
si dos proyectos requieren la misma librería pero con distinta versión (la nueva versión incluye una característica necesaria en uno de los proyectos),
no tendremos que desinstalar una librería
para poder trabajar en uno de los proyectos
y repetir el proceso.
Además,
es común que una librería dependa de otra,
la cual debemos instalar en una versión compatible,
es decir, tenemos una restricción de las versiones a utilizar en nuestro proyecto.
Con los ambientes virtuales cada proyecto tendrá sus librerías en las versiones específicas que requiramos y no existirán conflictos entre proyectos.

Existen distintas herramientas para la creación de ambientes virtuales;
la librería estándar de python incluye el módulo **venv**,
existen herramientas externas como
**virtualenv**
(ofrece las funcionalidades de **venv** y algunas extras),
**pipenv**
(la comunidad quiere hacer de esta herramienta el nuevo manejador de ambientes virtuales recomendado),
**poetry**,
entre otras.
Nosotros utilizaremos el módulo **venv** incluido en nuestra instalación.


### Creación y uso de ambientes virtuales

Para crear un ambiente virtual primero nos aseguramos de seleccionar el python con que deseemos trabajar (`pyenv global <version>`).
Posteriormente, utilizamos el módulo **venv** dándole como argumento el nombre que deseamos para el ambiente virtual; si deseamos que nuestro ambiente se llama **.venv** utilizamos

    python -m venv .venv

Esto crea una estructura de archivos y carpetas dentro de **.venv**.
Dentro de esta, existe una liga (softlink) a la versión de python con que fue creado el ambiente virtual y a su interior se almacenaran cada una de las librerías que instalemos en el ambiente.

Una vez creado el ambiente debemos activarlo mediante:

    source .venv/bin/activate

Aparecerá en tu prompt el nombre del ambiente virtual entre paréntesis para que sepas que se encuentra activo.

Una vez activo podemos instalar las librerías que deseemos.
Por ejemplo,  para instalar la librerías **numpy** y **mypy**

    python -m pip install numpy mypy

El módulo **pip** es la herramienta estándar para
instalar, actualizar y eliminar
bibliotecas de terceros a partir del
Python Package Index
([PyPI](https://pypi.org/)).
También podemos utilizar más resumidamente

    pip install ipython

Para desinstalar utilizamos

    pip uninstall numpy mypy

Una vez concluimos con nuestro trabajo podemos desactivar el ambiente virtual mediante

    deactivate

Para eliminar un ambiente virtual basta con que eliminemos la carpeta donde se almacenó este.

    rm -r .venv

y si esta función no da resultados forzamos la eliminación mediante

    rm -rf .venv


## Variables y Tipos de Datos Básicos

Ya hemos visto las reglas que tenemos con respecto a los nombres de variables, funciones y clases, tanto públicas como privadas.

Volvemos a mencionar los tipos de datos básicos en Python

    >>> strings = "Hola Mundo"
    >>> entero = 5
    >>> reales = 3.7
    >>> verdad = True
    >>> falso = False

Estas variables almacenan objetos de tipo **str**, **int**, **float** y **bool**. Para ver su tipo basta con ejecutar

    >>> type(verdad)
    <class 'bool'>

Recordamos que estos objetos son del tipo **inmutable** como ya hemos visto en clase,
es decir,
no pueden ser modificados;
cada que creemos haberlos modificado realmente hemos creado un nuevo objeto.

### Métodos para los objetos **str**

Abramos
**IPython** (Interactive Python),
el intérprete (shell) de comandos interactivo para python.
Este representa una actualización significativa sobre el
intérprete estándar de python
(**REPL** - **Read-Eval-Print Loop**).
Investiga sobre sus características
(intérprete interactivo,
comandos mágicos,
introspección de objetos,
acceso a comandos del shell).

Provemos algunos métodos de los objetos inmutables **str**,
así como algunas características de **ipython**.

    In [1]: nombre = "Maria Rojas"

Introspección en ipython:

    In [2]: nombre.isascii?

Ejecución de método:

    In [3]: nombre.isascii()
    Out[3]: True

Para ver todos los métodos disponibles podemos escribir
`nombre.` y presionar \<TAB> para que **ipython** nos muestre todos los métodos del objeto.
Python provee la función `dir` para ver los métodos y atributos de cualquier objeto como ya hemos visto en clase.

Experimentar con algunos métodos:

    In [4]: nombre.lower()

    In [5]: nombre.capitalize()

    In [6]: texto = ' Tenemos espacio  '

    In [7]: texto.strip()

    In [8]: texto.lstrip()

También podemos utilizar algunas **palabras reservadas** en combinación con nuestros strings.
Por ejemplo,
para verificar si una cadena de caracteres está contenida en nuestro string

    In [9] 'Rojas' in nombre
    Out[9] True

o para verificar que una cadena no aparece en el string

    In [10] 'rojas' in nombre
    Out[10] False

    In [11] 'rojas' not in nombre
    Out[11] True

Un **string** es un objeto **iterable**,
esto es,
un objeto que es capaz de regresar sus elementos uno a la vez;
los elementos de un **string** son cada uno de sus caracteres.
Una función muy útil para todo objeto iterable es
`len`,
la cuál regresa el número de elementos del iterable.
Por ejemplo,

    In [12]: len(texto)
    Out[12]: 18

Para acceder a los elementos del string utilizamos índices como se muestra a continuación.

### Indexación

Los strings cuentan con índices para cada caracter comenzando en cero.
Esto nos permite extraer información o seleccionar parte de este.

    In [13]: nombre[2]
    Out[13]: 'r'

    In [14]: nombre.find('a')
    Out[14]: 1

    In [15]: nombre.find('jas')
    Out[15]: 8

    In [16]: nombre.find('Jas')
    Out[16]: -1

    In [17]: nombre.replace('Maria', 'Elena')

    In [18]: nombre_correcto = nombre.replace('Maria', 'Elena')

### Slicing

Podemos utilizar los índices para seleccionar un subconjunto de caracteres del string. La sintaxis a utilizar es

    texto[start:end]

o bien,

    texto[start:end:inc]

donde **start** es el índice de inicio,
**end** es el índice final más uno
y **inc** es el incremento entre índices.
Cuando no declaramos el incremento,
este toma el valor de uno
(sintaxis superior).
A continuación algunos ejemplos.

    In [19]: nombre[6:9]
    Out[19]: 'Roj'

    In [20]: nombre[0:10:2]
    Out[20]: 'MraRj'

Cuando no declaramos **end** automáticamente se selecciona el índice del último caracter más uno.

    In [21]: nombre[2:]
    Out[21]: 'ria Rojas'

    In [22]: nombre[2::2]
    Out[22]: 'raRjs'

Si no declaramos **start** se selecciona para este parámetro el índice cero. Por ejemplo,

    In [23]: nombre[:7]
    Out[23]: 'Maria R'

¿Cómo se vería el resultado de las siguientes declaraciones?

    In [24]: nombre[:7:2]

    In [25]: nombre[:]

    In [26]: nombre[::2]

También podemos utilizar un incremento negativo

    In [27]: nombre[4:1:-1]
    Out[27]: 'air'

Para ir de derecha a izquierda y llegar hasta el primer caracter simplemente no declaramos **end**

    In [28]: nombre[4::-1]
    Out[28]: 'airaM'

Cuando declaramos incrementos negativos el papel de
**start** y **end** se invierten;
si no declaramos el **start** se selecciona el último caracter,
y si no declaramos **end**
se selecciona el primer caracter. Vea los siguientes ejemplos

    In [29]: nombre[:3:-1]
    Out[29]: 'sajoR a'

    In [30]: nombre[7::-1]
    Out[30]: 'oR airaM'

¿Cómo invierto el string por completo?

## Loops

## Decisiones

## Funciones
## Estructuras de Datos
