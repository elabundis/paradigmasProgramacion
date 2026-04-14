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
    >>> complejo = 3+4j
    >>> verdad = True
    >>> falso = False

Estas variables almacenan objetos de tipo
**str**, **int**, **float**, **complex** y **bool**.
Para ver su tipo basta con ejecutar

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
    *, @, /, //, %   Multiplicación,
                     multiplicación matricial,
                     división,
                     división entera,
                     módulo
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

### Tipos numéricos

Tenemos en esta categoría a los objetos de tipo
`int`, `float` y `complex`.
Las instancias de tipo `int` son lo números enteros sin decimales
(positivos, negativos y el cero),
los `float` son aquellos números con al menos un decimal (2.7, 4.0),
y los `complex` son aquellos que tienen parte imaginaria y probablemente una parte real (`-2.7j, 5+1j`).
En el caso de los complejos,
la parte imaginaria se da mediante un
`int` o `float` seguido por la letra `j` (unidad imaginaria),
sin dejar de tener un número frente a esta,
es decir,
`j` nos arroja un error,
mientras `1j` o `-1j` son correctos.

Al llevar acabo operaciones de
**sumatoria**, **resta** y **multiplicación**
con instancias de un mismo tipo numérico,
el intérprete regresará ese tipo.
La **exponenciación** de una base elevada a un entero
regresará el tipo de la base.
Por su parte una **división** que incluya números enteros o reales
siempre regresará un número real,
mientras q si tenemos un número complejo en el numerador o denominador el resultado sera complejo.

    >>> 4 ** 2
    >>> 4.0 ** 2
    >>> 6 / 2
    >>> 2 * (3 + 4) - 3 ** 2
    >>> 2j ** 2
    >>> -3**2
    >>> -4j ** 2

En el caso de la división, contamos con dos funciones que pueden resultar útiles;
la **división entera** (`//`)
y el **módulo** (`%`),
definidos para los tipos
`int` y `float`
(no funcionan con el tipo complex).
**Nota:** en las versiones de CPython 2 el operador `/`
corresponde a la división entera a menos que un operando sea `float`.

La división entera regresa el cociente,
es decir,
el número entero de veces que el divisor cabe en el dividendo.
Además,
si ambos operandos son de tipo `int` el resultado es `int`,
de otra manera regresa un `float`.

El módulo retorna el residuo de la división
y utiliza la misma regla que la división entera para el tipo de dato que regresa.
**Nota importante:**
al utilizar números de punto flotante,
se introducen pequeños errores debido a la manera en que estos objetos son almacenados en memoria.
Esto también aplica con la división entera.

    >>> 7 // 4
    >>> 7 % 4
    >>> 4.4 // 2.2
    >>> 6.6 // 2.2
    >>> 1 % 0.3

#### Conversión de tipos
##### Explícita

Contamos con las funciones: `int`, `float` y `complex`.
Las primeras dos funciones están definidas para números reales y strings.

La función `int` retorna una nueva instancia de tipo `int`;
si se le da un `float` recorta la parte decimal
y solo acepta objetos `str` que representen números enteros.

Por su parte `float` retorna un número de punto flotante siempre que sea posible.

Por último `complex` toma un número o un string y los convierte en un número complejo.
Esta función también nos permite dar dos argumentos;
en este caso el primer argumento es la parte real y la segunda la imaginaria.

    >>> float(5)
    5.0
    >>> int(8.7)
    8
    >>> complex(3)
    (3+0j)
    >>> complex(2, 5)
    >>> complex('13')
    >>> int('18.9')

##### Implícita

Para evitar la pérdida de información al llevar acabo ciertas operaciones entre datos con distintos tipos,
python convierte el tipo de dato menor a mayor
(int &lt; float &lt; complex)
sin intervención del programador.
En particular,
esto ocurre con las operaciones de suma, resta y multiplicación.

    >>> x = 2
    >>> y = 4.5
    >>> z = 1 - 3j
    >>> suma = x + y
    >>> type(suma)
    >>> y - z
    >>> x * z
    >>> type(5 * x)
    >>> 1 + 4 / 2
    >>> 2 + (1 - 2.0) * 3 + 1j
    >>> -3 + 5 // 2.0 ** 2

#### Sistemas numéricos

Además de utilizar cantidades numéricas en formato decimal,
python reconoce otros tres sistemas:
**binario** (base 2),
**octal** (8) y
**hexadecimal** (base 16).
Para declarar un entero en uno de estos sistemas,
utilizamos el prefijo
**0b**, **0o** o **0x**,
respectivamente.
El primer carácter es el número cero y
el segundo es una letra que puede darse en
**minúscula o mayúscula**.

Los caracteres numéricos que cada sistema permite son los siguientes:

- binario 0,1
- octal   0-7
- hexadecimal 0-9, A-F

<!-- -->

    >>> x = 0B110
    >>> print(x)
    >>> print(0o15)
    >>> print(0x1A)
    >>> y = 0b110 + 0x1A
    >>> print(y)

En ocasiones,
necesitamos introducir números enteros en estos sistemas mediante **strings**
(al leer información desde un archivo).
Esto se logra utilizando la función **int**
con un segundo argumento `base=0`.
Por ejemplo,

    >>> entero = int('0x11', base=0)
    >>> print(entero)

**Cuando usemos el argumento `base` debemos dar el entero mediante un string.**
Este argumento se refiere a la base usada para el entero;
podemos usar cualquier base en el rango 2-36
(con caracteres de 0-9 y a-z en minúscula o mayúscula).
Un valor de cero
le indica a python que interprete el string de acuerdo a sus reglas.

    >>> int('z', base=36)
    >>> int('1Y', base=36)
    >>> int('z', base=35)

### Matemáticas en Python

La librería estándar de python incluye el módulo **math**,
el cual puede ser suficiente para tareas sencillas.
Para funciones complejas no incluidas u operaciones con vectores,
podemos utilizar una librería externa especializada como
**numpy** o **scipy**.

El módulo **math** incluye:
* constantes típicas
($\pi$, $e$),
* funciones comunes
(raíz cuadrada, exponencial, logarítmo),
* funciones trigonométricas
(coseno, seno hiperbólico),
* funciones encontradas en probabilidad y estadística
(factorial, combinaciones, permutaciones, función error).

Una lista completa de las funciones
(con su respectiva documentación)
la puedes ver
[aquí](https://docs.python.org/3.13/library/math.html).

Para importar un módulo incluido en la librería estándar,
utilizamos el comando `import` seguido por el nombre de este.
Para acceder a sus objetos
(clases, funciones y constantes),
utilizamos la notación de punto como mostramos abajo.

En esta sección empleamos un editor para ingresar las instrucciones y posteriormente correrlas con el intérprete.
Introducimos los siguientes comandos en un archivo con extensión py:
matematicas.py

    import math

    # seno de pi / 2
    x = math.pi / 2
    print( 'x = ', x, ', sin(x) = ', math.sin(x) )

    # logarítmo de base e
    y = math.e
    print(f'y = {y}, ln(y) = {math.log(y)}', )

    # logaritmo de base 2, 10 y cualesquiera

#### Notas sobre objetos numéricos

Los **enteros** (`int`) en python,
pueden ser tan grandes como se desee
(**precisión arbitraria**);
como se ha mencionado en las diapositivas,
el intérprete asignará la cantidad necesaria de bits para representar cualesquier entero de manera exacta.
Esta característica no se presenta en un lenguaje con tipos estáticos
(C++, Haskell, Rust, etc.),
donde se asigna una cantidad de bytes a cada tipo de dato durante el proceso de compilación.

Los `float`,
por su parte,
representan números de **punto flotante** con una
**precisión de 15 a 17 cifras significativas**
(para mayor precisión existe el módulo `decimal`).
Internamente,
estos son representados mediante 64 bits,
utilizando el estándar IEEE 754 de doble precisión
(**binary64**).
En esta representación,
se utilizan 53 bits de precisión
(1 bit para el signo y 52 para la mantisa o base)
y 11 para representar el exponente.
Este es el estándar que casi todas las implementaciones de C o C++ utilizan para el tipo `double`
(recordemos de la clase,
que distintas implementaciones pueden almacenar tipos de datos con distinta cantidad de bits).
De hecho, la mayoría de lenguajes de programación modernos utilizan este estándar bajo distintos nombres:
**double** en Java,
**real(dp)** en Fortran,
**float64** en Go,
**f64** en Rust,
etc.

Los objetos `complex` representan tanto la parte real como la parte imaginaria mediante **binary64**.

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
