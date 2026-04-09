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


## Preámbulo

### Instalación y Ejecución

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

donde la versión que empieza con asterisco es la que estamos empleando en este momento.
La versión denotada como **system** se refiere a la versión de python preinstalada en tu sistema operativo.

Si solo deseamos ver la versión que estamos utilizando actualmente ejecutamos

    pyenv version

Para desinstalar una implementación tenemos

    pyenv uninstall 3.14.3


#### Cambiando entre versiones

Esta herramienta nos permite establecer una versión global para python mediante

    pyenv global 3.13

También podemos activar versiones locales.
Las versiones locales son aquellas que configuramos en un directorio y se activan y desactivan automáticamente cuando entramos o salimos de este.
Por ejemplo, crea una carpeta y dentro de esta ejecuta

    pyenv local 3.12.2

Observa qué versión de python tienes al entrar y salir de este directorio con `python --version`.
Observa que la opción `local` crea un archivo en el directorio con nombre **.python-version** dentro del cual se tiene la versión local de python a utilizar. Si eliminamos este archivo se elimina la configuración local.

Por último pyenv nos permite establecer una versión de python para nuestra sesión en el shell sobrescribiendo cualquier ajuste global o local.
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


### Ambientes virtuales

Siempre que nuestro proyecto vaya a hacer uso de **paquetes**
(librerías sería el término común en otros lenguajes)
no incluidos en el **standadrd library**,
debemos crear un ambiente virtual.

Los ambientes virtuales nos permiten aislar ambientes de programación para que podamos instalar librerías en las versiones que requiramos en distintos proyectos.

El aislamiento se consigue
creando una estructura de directorios por proyecto,
dentro de la cual se almacenan los paquetes que instalamos.
Dentro de esta estructura,
se crea una copia o un enlace
(dependiendo del sistema operativo, versión)
al python con que fue creado el ambiente virtual.
Además,
se crean enlaces a módulos y paquetes incluidos en la librería estándar de python para que la instalación del ambiente sea ligero y de rápida creación.

Gracias al aislamiento,
si dos proyectos requieren el mismo paquete pero con distinta versión (la nueva versión incluye una característica necesaria en uno de los proyectos),
no tendremos que desinstalar uno
para poder trabajar en uno de los proyectos
y repetir el proceso.
Además,
es común que un paquete dependa de otro,
el cual debemos instalar en una versión compatible,
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
Este módulo ya lo hemos puesto en práctica en el laboratorio 2 y aquí realizamos un repaso.


#### Creación y uso de ambientes virtuales

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

Concluido el preámbulo pasamos a discutir los fundamentos del lenguaje.

## HelloWorld

Siguiendo la costumbre de empezar con nuestro programa más básico,
aquí mostramos nuestro HelloWorld en python.
Abrimos el intérprete (**REPL**) mediante `python` y dentro de este ejecutamos

    >>> print('HelloWorld!')

El comando `print` toma como argumento cada uno de los valores dados y los imprime a **stdout** por default

    >>> print('Mis', 2, 'amores')
    Mis 2 amores

donde los valores no tienen que ser **strings**.
Para salir del **REPL**,
invocamos `exit()` o `quit()`.
En versiones de CPython 3.13 y superiores,
es suficiente escribir cualquiera de los dos comandos sin los paréntesis.

## Ayuda

Para ver la documentación y obtener ayuda con
comandos, funciones, clases e incluso módulos,
contamos con la función `help`.

    >>> help(print)

    >>> help(float)

Podemos ver la documentación de módulos no importados utilizando su nombre en un string

    >>> help('sys')

Podemos entrar a un intérprete interactivo de ayuda ejecutando
`help()` sin argumentos.
En este intérprete escribimos el nombre del
módulo, palabra clave o incluso tema de interés
y obtenemos la documentación correspondiente.
Para salir del modo de ayuda utilizamos
`q`, `quit`, o `exit`.
Para ver los temas posibles invocamos `topics`
o para ver los módulos `modules`.


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

### Precedencia de operadores

La precedencia de operadores se refiere al orden en que se llevan acabo las operaciones.
Los operadores, por su parte,
son funciones que actúan sobre uno (unarios) o más objetos.
A continuación una lista de operadores con precedencia de mayor a menor por renglón
(dos operadores en el mismo renglón tienen la misma precedencia):

    ()            Paréntesis
    **            Exponenciación
    +x, -x, ~x    Operadores unarios: positivo, negativo y NOT bit a bit
    *, /, //, %   Multiplicación, división, división entera, módulo
    +, -          Suma, resta
    <<, >>        Desplazamiento a la izquierda o derecha
    &             AND bit a bit
    ^             XOR bit a bit
    |             OR bit a bit
    ==, !=, >, >=, <, <=, is, is not, in, not in   Comparaciones lógicas,
                                     operadores de identidad y membresía
    not           NOT
    and           AND
    or            OR

Si una expresión contiene dos operadores con la misma precedencia, esta se evalúa de izquierda a derecha.

Los operadores pueden actuar sobre más de un tipo de objeto
(sobrecarga o polimorfismo de operadores),
por ejemplo,
el operador de sumatoria `+`
realiza una suma sobre enteros pero una concatenación sobre strings.


### Strings (str)
#### Métodos

Antes de continuar utilicemos un intérprete más avanzado que el que viene de manera estándar con python.
Este se encuentra disponible como un paquete en PyPI y se llama **ipython**.

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

Probemos algunos métodos de los objetos inmutables **str**,
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

Por cierto,
en ipython se almacena el historial de la entrada y salida en las variables
In (lista)
y
Out (diccionario),
respectivamente.
Por ejemplo,
podemos acceder a la entrada (código) de la celda número 6 mediante `In[6]` o bien la salida (resultado) de la celda 5 con `Out[5]`.
La última salida se almacena en la variable `_`
y la última entrada en `_i`.

Continuando con el uso de strings,
también podemos combinar **palabras reservadas** con nuestros strings.
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

#### Indexación

Los strings cuentan con índices para cada carácter comenzando en cero.
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

#### Slicing

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

Cuando no declaramos **end** automáticamente se selecciona el índice del último carácter más uno.

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

Para ir de derecha a izquierda y llegar hasta el primer carácter simplemente no declaramos **end**

    In [28]: nombre[4::-1]
    Out[28]: 'airaM'

Cuando declaramos incrementos negativos el papel de
**start** y **end** se invierten;
si no declaramos el **start** se selecciona el último carácter,
y si no declaramos **end**
se selecciona el primer carácter. Vea los siguientes ejemplos

    In [29]: nombre[:3:-1]
    Out[29]: 'sajoR a'

    In [30]: nombre[7::-1]
    Out[30]: 'oR airaM'

¿Cómo invierto el string por completo?

#### Operaciones básicas

Los operadores encontrados en aritmética básica toman un significado distinto dependiendo del tipo de datos sobre los que operen.
En el caso de strings,
python define la suma de strings y
su multiplicación por un número entero.

La sumatoria conduce a la **concatenación**:

    In [31]: print("Hola" + " Mundo" + "!")
    Out[31]: 'Hola Mundo!'

mientras que la **multiplicación por un entero** como en

    In [32]: print(3*"Ja")
    Out[32]: 'JaJaJa'

repite el string multiplicado
(debido a que la multiplicación se interpreta como sumatoria).
Desde luego podemos combinar las operaciones recordando que el lenguaje tiene su orden de precedencia:

    In [33]: saludo = 2*'¡' + 'Hola' + 2*'!'

    In [34]: saludo
    Out[34]: '¡¡Hola!!'

## Loops

## Decisiones

## Funciones
## Estructuras de Datos
