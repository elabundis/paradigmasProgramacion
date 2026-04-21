---
geometry: "left=3cm,right=3cm,top=2cm,bottom=2cm"
fontsize: 12pt
---
<div style="text-align: justify;">

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
utilizamos el comando `import` seguido por el nombre de este,
es decir,
`import math`.
Para acceder a sus objetos
(clases, funciones y constantes),
empleamos la notación de punto como mostramos más abajo.

Comenzamos introduciendo operaciones de punto flotante, en particular, las funciones:

* `math.floor(x)` regresa el entero más grande menor o igual a x,
* `math.ceil(x)` regresa el entero más chico mayor o igual a x,
* `math.trunc(x)` regresa la parte entera de x.

En esta sección,
ingresaremos las instrucciones en el archivo
matematicas.py
con nuestro editor favorito,
y posteriormente las ejecutaremos con el intérprete.
A continuación,
editamos nuestro archivo:

    import math

    print('Operaciones de punto flotante')

    # Apliquemos algunas funciones importantes
    x = math.floor(4.8)   # Operación piso
    y = math.ceil(7.1)    # Operación techo
    z = math.trunc(2.99)  # Truncar parte decimal
    print(x, y, z)

y lo ejecutemos desde la terminal mediante

    python matematicas.py

En este código hacemos uso de comentarios:

- **Los comentarios comienzan con el carácter #**,
a partir del cual,
el intérprete descarta todo a la derecha.
Note que estos pueden colocarse en cualquier parte de una línea.

Un detalle importante a mencionar;
se debe tener cuidado al comparar la igualdad de dos números de tipo `float`;
**no es recomendable comparar números reales con el operador `==`**.
Esto debido a la precisión finita de la computadora
y a la manera en que estos números son almacenados.
La manera más correcta es emplear la función
`math.isclose`
como se muestra aquí

    # Comparar igualdad de números reales
    x = 0.1 + 0.2
    y = 0.3
    print('Comparando dos números reales que deberían ser iguales\n')
    print("Utilizando '=='")
    print( x == y )
    print("Utilizando 'math.isclose'")
    print( math.isclose(x, y) )
    print()


Procedemos ahora con algunas funciones trigonométricas.
Recordemos que, básicamente en cualquier lenguaje de programación,
las funciones trigonométricas operan con radianes por default:

    import math

    print("Funciones trigonométricas")

    # Angulo en radianes
    theta = math.pi / 2
    print('theta = ', theta, ', sin(theta) = ', math.sin(theta) )

    # Para ángulos en sistema sexagesimal primero transformar a radianes
    GRADOS_A_RADIAN = math.pi / 180
    beta = 45  # 45 grados
    print(f'beta: {beta} grados')  # Utilizando f-strings
    print(f'tan(beta) = {math.tan(beta * GRADOS_A_RADIAN)}')

    # Las funciones inversas dan los ángulos en radianes.
    # Podemos transformar a grados si lo deseamos.
    RADIAN_A_GRADOS = 1 / GRADOS_A_RADIAN
    gama = math.acos(math.sqrt(2) / 2)
    print(f'acos(sqrt(2)/2) en grados: {gama * RADIAN_A_GRADOS}')
    print()  # Línea en blanco

Con respecto a los f-strings:

- Los **f-strings nos permiten utilizar el contenido de variables,
o ejecutar código en general,
dentro de un string**;
    La sintaxis es

        f'... {codigo} ...'
    dónde el prefijo **f**
    indica que el string será un f-string,
    y el código es colocado entre llaves.
    El intérprete automáticamente transforma (parsea) el resultado a un `str` y lo une al resto del string

**Note como se ha evitado el uso de *números mágicos***
(constantes numéricas directamente en el código sin explicación)
**para transformar entre radianes y grados**
(ver variables);
el contexto de las constantes es importante,
además, si introducimos un bug y repetimos la constante en múltiples lugares, tendríamos que ir y corregir cada una de sus apariciones.
También,
**observa como expresamos
RADIAN_A_GRADOS = 1 / GRADOS_A_RADIAN,
en lugar de 180 / math.pi**,
ya que de esta manera se expresa la relación entre las dos constantes,
y al corregir una,
la segunda se corrige automáticamente
(hay excepciones a esta regla que pueden darse por cuestiones de precisión en los cálculos).
Por último,
nota el uso de
**snake_case
en la declaración de las variables**,
y el uso de **mayúsculas para constantes globales**.

Por cierto,
`math` incluye funciones para transformar entre los sistemas sexagesimal y circular (radianes)
(ver `math.degrees` y `math.radians`).

A continuación agregamos algunas funciones hiperbólicas a nuestro archivo.
En el caso del módulo `math`,
estas funciones están definidas para cualquier número real
(si necesitamos emplear números complejos,
python incluye el módulo `cmath`)
y nos regresa un `float`.

    print('Funciones hiperbólicas')

    # coseno hiperbólico
    print(f'cosh(1.5) = {math.cosh(1.5)}')
    # arco seno hiperbólico (inversa del seno hiperbólico)
    print(f'asinh(1) = {math.asinh(1)}')
    print()

Para tomar el logarítmo de una base deseada empleamos

    # Logarítmos
    print('Logaritmos')

    # logarítmo de base e
    y = math.e  # constante de Euler
    print('y =  ', y)
    print(f'ln(y) = {math.log(y)}') # Utilizando f-strings
    # logaritmo de base 2, 10 y cualesquiera
    print(f'log_2(16) = {math.log2(16)}')
    print(f'log_10(100) = {math.log10(100)}')
    print(f'log_3(27) = {math.log(27, 3)}')
    print()

Por último,
mostramos algunos ejemplos de funciones de probabilidad y estadística

    # Probabilidad y estadística
    print("Funciones en Probabilidad y Estadística")

    print('factorial de un entero n (número de permutaciones de n objetos)')
    print(f'4! = {math.factorial(4)}')
    print('Combinaciones con dos elementos de un conjunto de cuatro elementos')
    print('(todos los subconjuntos de dos elementos)')
    print(f'comb(4, 2) = {math.comb(4, 2)}')
    print('Permutaciones con tres elementos tomados de un conjunto de cuatro elementos')
    print('(el orden importa en las permutaciones)')
    print(f'perm(4, 3) = {math.perm(4, 3)}')
    print('Función error')
    print(f'erf(1.0) = {math.erf(1.0)}')

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
#### Operaciones básicas

Los operadores encontrados en aritmética básica toman un significado distinto dependiendo del tipo de datos sobre los que operen.
En el caso de strings,
python define la suma de strings y
su multiplicación por un número entero.

La sumatoria conduce a la **concatenación**:

    >>> print("Hola" + " Mundo" + "!")
    'Hola Mundo!'

mientras que la **multiplicación por un entero** como en

    >>> print(3*"Ja")
    'JaJaJa'

repite el string multiplicado
(debido a que la multiplicación se interpreta como sumatoria).
Desde luego podemos combinar las operaciones recordando que el lenguaje tiene su orden de precedencia:

    >>> saludo = 2*'¡' + 'Hola' + 2*'!'
    >>> saludo
    '¡¡Hola!!'

#### Comparaciones

Podemos comparar dos strings utilizando los operadores de comparación;
`>`, `>=`, `==`, `!=`, `<`, `<=`.
Estos comparan carácter a carácter utilizando el orden lexicográfico,
es decir,
de acuerdo al diccionario.
Específicamente,
utilizan el código unicode durante la operación.

* Para verificar si dos strings son indénticos utilizamos `==`,
  mientras que `!=` nos informa si los strings son distintos.

* El resto de operadores nos permiten determinar el orden alfabético entre dos strings,
  comparando el valor unicode del primer caracter que difiera entre estos.

Tenemos, por ejemplo

    >>> 'cargo' < 'cargamento'
    False

ya que la 'o' es mayor a la 'a'.
Por otro lado,

    >>> 'mate  ' > 'mate'
    True

debido a los caracteres extra en `'mate  '`.
También,

    >>> 'hola' == 'Hola'
    False

ya que los valores unicode de 'H' y 'h' son distintos.
De hecho,
en este caso

    >>> 'hola' > 'Hola'
    True

ya que las mayúsculas van antes que las minúsculas en unicode.
**Para conocer el valor unicode de un caracter,
utilizamos la función `ord`**
(acepta *strings* de un sólo caracter,
*strings* más grandes generarán un error):

    >>> ord('H')
    72

    >>> ord('h')
    104

Observamos que las comparaciones se pueden concatenar
(al igual que con objetos numéricos)

    >>> print( 'cajon' < 'cancion' < 'casa' )

Por último,
hacemos mención de la palabra reservada `is`,
la cuál puede confundirse con el operador `==`;
mientras que el operador `==`,
verifica si dos *strings* son idénticos en valor,
`is` checa si dos variables apuntan al mismo objeto en memoria.
De esta manera

    >>> x = 'bye' + '!'
    >>> y = 'bye' + '!'
    >>> z = x
    >>> print(x == y)
    >>> print(x is y)
    >>> print(z is x)

Nota: Para checar si dos objetos son idénticos en python se utiliza la función `id`;
esta mapea cada objeto a un entero único,
el cuál típicamente es la dirección del objeto.

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

Cuando no declaramos **end**,
la selección llega hasta el último carácter:

    In [21]: nombre[2:]
    Out[21]: 'ria Rojas'

    In [22]: nombre[2::2]
    Out[22]: 'raRjs'

Por otro lado,
**start** toma el valor cero si no es declarado.
Por ejemplo,

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


## Decisiones

El control de flujo en python se lleva acabo con las palabras reservadas:
`if` - `elif` - `else`,
utilizando la siguiente sintaxis

    if condicion_1:
        bloque_1
    elif condicion_2:
        bloque_2
    ...
    else:
        bloque_n

    mas_codigo

dónde las condiciones `elif` y `else` son **opcionales**.
Observa que los bloques se encuentran indentados
(con sangría)
con respecto a cada una de las palabras reservadas.
Cada `condicion_x` debe corresponder a un valor booleano,
tras el cual se debe incluir dos puntos.

Al concluir con los bloques,
se debe eliminar la indentación como se aprecia en la linea:
`mas_codigo`.

El flujo opera de la siguiente manera:
* Se evalúa la **condicion_1** y se verifica si esta es `True`.
  De no ser así,
  se evalúa la **condicion_2** para checar si esta es `True`.
  El proceso continúa hasta encontrar una condición verdadera.
  Posteriormente,
  se ejecuta el bloque al interior de dicha condición,
  e inmediatamente después,
  se transfiere el control a la línea `mas_codigo`,
  es decir,
  fuera de la estructura.

* Si ninguna condición es `True`,
  entonces se ejecuta el bloque de `else`
  (si dicha condición existe).

El uso de la indentación para indicar la región de cada bloque,
es parte de la filosofía de python;
al no utilizar algún tipo de paréntesis como separador,
la escritura y lectura se asemeja más al lenguaje natural,
ofreciendo,
desde su perspectiva,
mayor claridad.

Ejemplo 1: Encuentra si el usuario nos da un entero par o impar.

```python
# Encuentra si el entero es par o impar
x = int(input('Introduzca un entero: '))
if(x % 2 == 0):
    print(f'{x} es un numero par')
else:
    print(f'{x} es impar')
```

Ejemplo 2: Se hace una venta de boletos de loteria con las siguientes reglas:
* Si compras hasta 20 boletos, el precio por boleto es de $100.
* Si compras más de 20 boletos y menos de 30, se te da un precio de $90.
* Si compras 30 o más boletos, obtienes un precio de $60.

Crea un programa que me de el precio para cualquier cantidad de boletos deseados.

```python
# Compra de boletos
boletos = int(input('Numero de boletos: '))
if boletos < 21:
    costo_boleto = 100
elif boletos < 30:
    costo_boleto = 90
else:
    costo_boleto = 60

costo_total = boletos * costo_boleto
print(f"Pagar: {costo_total}")
```

(Tengo dinero para comprar 20 boletos. ¿Será inteligente de mi parte comprar 20 boletos?)

Si nuestro bloque `if`
consiste en una sola declaración,
python nos permite la siguiente sintaxis corta
(esto solo se recomienda si el cuerpo del `if` es muy corto):

```python
estudiantes = ['Pedro', 'Laura']
activo = False

persona = 'Laura'
if persona in estudiantes: activo = True

print(f'Activo: {activo}')
```

Por último,
en python se cuenta con las
**expresiones condicionales**.
Estas son sentencias de una linea para una declaración
`if`-`else`,
cuya sintaxis es:

```python
valor_si_True if condicion else valor_si_falso
```

En este caso,
se evalúa la `condicion`;
si esta es verdadera se regresa el valor `valor_si_True`,
en caso contrario se regresa `valor_si_falso`.
Ejemplo:

```python
x = -5
signo = 'positivo' if x > 0 else 'negativo'

print(signo)
```

Ejercicios:

* Programa que lea la calificación en porcentaje de un estudiante y retorne su calificación en formato de letras.
  Considere la siguiente relación:

  <table>
  <tr>
      <td>A</td>
      <td>90-100</td>
  </tr>
  <tr>
      <td>B</td>
      <td>80-89</td>
  </tr>
  <tr>
      <td>C</td>
      <td>70-79</td>
  </tr>
  <tr>
      <td>D</td>
      <td>60-69</td>
  </tr>
  <tr>
      <td>F</td>
      <td>0-59</td>
  </tr>
  </table>

* Implemente el algoritmo de FizzBuzz.

  Para un entero `i` de 1 a 20:

    * Si 3 y 5 dividen a `i`, imprime: 'FizzBuzz'
    * De no ser así, si 3 divide a `i`, imprime: 'Fizz'
    * De no ser así, si 5 divide a `i`, imprime: 'Buzz'
    * En cualquier otro caso imprime `i`.

* Programa que, dados tres enteros, diga cuál es el menor.

* Cree un programa que lea la edad de una persona y,
  mediante una expresión condicional
  (una sola linea),
  retorne a **stdout** si la persona es adulta o menor de edad.

## Loops

Para repetir un conjunto de declaraciones en python,
contamos con dos  tipos de estructuras: `for` y `while`.

El bucle `for` presenta la siguiente sintaxis:

    for variable in iterable:
        linea_1
        linea_2
        ...
        linea_n

donde el `iterable`, como ya mencionamos anteriormente,
es un objeto capaz de regresar sus elementos uno a la vez
(`str`, `list`, `tuple`, `dict`),
y las lineas,
representan un conjunto de instrucciones a repetir.
Observa los dos puntos delante del `iterable`
y la indentación que se le debe dar al bloque de instrucciones.

Los bucles `for` operan de la siguiente manera;

* A la `variable` se le asigna el primer elemento de `iterable`
  y ejecuta cada una de las instrucciones en el bloque
  de arriba hacia abajo
  (`linea_1` a `linea_n`).

* Al finalizar,
  el flujo regresa para asignarle a la `variable` el segundo valor de `iterable` y volver a ejecutar las instrucciones.
* Este proceso se repite para cada uno de los elementos en `iterable`.

Antes de ver un ejemplo,
veamos un objeto muy útil para la estructura `for`,
el objeto `range`.
Este objeto se utiliza para generar una secuencia de enteros con espaciamiento constante.
Podemos generar una secuencia de enteros del 0 al 9 mediante

    >>> x = range(10)
    >>> type(x)
    >>> print(x)
    >>> print( list(x) )

Utilizamos el comando `list`
para transforma el objeto en una lista,
ya que el objeto `range` no muestra sus elementos.
Si deseamos un entero inicial distinto a cero,
digamos de 2 a 8, utilizamos

    >>> y = range(2, 9)

La función range también acepta un argumento para la separación entre enteros.
Por ejemplo, si deseamos los enteros impares del 1 al 13

    >>> z = range(1, 14, 2)

Regresando a los bucles `for`,
estos se utilizan cuando conocemos el número exacto de iteraciones,
o si este se encuentra determinado por la longitud de una sequencia.
A continuación mostramos algunos ejemplos.

Utilizando la secuencia de enteros range

    # Imprime del 0 al 5
    for i in range(6):
        print(i)

    # Imprime los número pares del 2 hasta el 8
    for j in range(2, 9, 2):
        print(j)

Con los elementos de un string

    saludo = '¡Hola!'
    for char in saludo:
        print(char)

o los de una lista

    ingredientes = [
        'camaron', 'tomate', 'cebolla', 'chile serrano',
        'cilantro', 'limon', 'pepino'
    ]
    print('Ingredientes para un ceviche:')
    for ingredient in ingredientes:
        print(ingredient)

Las temperaturas de grados Celsius a Farenheit

    # Tamaño de un grado Celsius en Farenheit
    one_deg = 9 / 5
    # Origen de Celsius (0) en Farenheit
    origin_F = 32

    # De cero a cien grados en pasos de diez grados
    print('Celsius', 'Farenheit')
    for Celsius in range(0, 101, 10):
        Farenheit = Celsius * one_deg + origin_F
        print(Celsius, Farenheit)

Como mencionamos al principio de esta sección,
contamos con un segunda estructura para la repetición de instrucciones,
el búcle `while`.
Este sigue la sintaxis

    while condicion:
        linea_1
        ...
        linea_n

donde la `condicion` es un booleano.

En este caso;

* El intérprete checa el valor de `condicion`.
Si el valor es `False`,
el flujo se pasa automáticamente debajo del bloque,
sin ejecutar instrucciones.
Si el valor es `True`,
se ejecuta la `linea_1`
hasta llegar a la `linea_n`.
Posteriormente,
el flujo regresa arriba y verifica el valor de `condicion`,
repitiéndose el proceso.

* Para no caer en un bucle infinito,
  debemos asegurarnos
  que las lineas del bloque
  transformen la `condicion` a `False`
  después de un número finito de repeticiones de este.

Un ejemplo sencillo se muestra a continuación

```python
entero = int(input('Introduzca un entero: '))
while entero > 0:
    entero -= 1
    print(entero)
```

A continuación implementamos un juego de la rueda de la fortuna.

    import random
    import time

    import tqdm  # Este módulo es externo y debe instalarse

    # Enteros presentes en la rueda
    rango = (0, 10)

    # Selecciona un numero ganador arbitrareo para el juego
    numero_ganador = random.randint(0, 10)

    # Al inicio no hay ganador
    ganador = False
    while (not ganador):
        input('Tira de la rueda ')
        # Da tiempo para que la rueda gire
        # Para mayor diversion agreguemos barra de progreso
        for i in tqdm.tqdm( range(10) ):
            time.sleep(0.2)
        numero = random.randint(0, 10)
        print(numero)
        if numero == numero_ganador:
            print('Ganaste!')
            ganador = True
        else:
            print('Sigue intentando')
            print()


En ocasiones,
no deseamos ejecutar todas las lineas dentro de un bloque,
ya sea un bucle de tipo `for` o `while`.
Para esto,
contamos con los comandos:
`break` y `continue`.

El comando `break`,
transfiere el flujo hacia la primer linea debajo
(afuera)
del bucle.
Por su parte,
`continue` lo transfiere al principio del bucle;
en el caso de `for`,
la `variable` tomará el siguiente valor del `iterable`.


Creemos un programa que lea las calificaciones de un estudiante,
las almacene en una lista y luego nos entregue el promedio.
El programa debe funcionar para distintas clases,
es decir,
el numero de calificaciones es desconocido de antemano.

```python
calificaciones = []
msg = 'Introduzca calificación (seleccione "end" para terminar): '
while True:
    grade = input(msg)
    if grade.lower() == 'end':
        print('Listo\n')
        break
    # No olvidemos transformar a un tipo numérico
    grade = float(grade)
    calificaciones.append(grade)
promedio = sum(calificaciones) / len(calificaciones)
print(f"Promedio: {promedio}")
```


## Funciones
## Estructuras de Datos

</div>
