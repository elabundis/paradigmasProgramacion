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

```python
>>> strings = "Hola Mundo"
>>> entero = 5
>>> reales = 3.7
>>> complejo = 3+4j
>>> verdad = True
>>> falso = False
```

Estas variables almacenan objetos de tipo
**str**, **int**, **float**, **complex** y **bool**.
Las variables de tipo string pueden declararse con comillas simples o dobles

```python
>>> otro_string = 'Bye'
```

Observa que no se requiere declarar el tipo de las variables.
Además,
el tipo de una variable puede cambiar después de haber sido creada

```python
>>> var = True
>>> var = 9
```

Para ver el tipo de una variable empleamos

```python
>>> type(verdad)
<class 'bool'>
```

Python es sensible a mayúsculas y minúsculas,
de tal manera que variables como

```python
>>> astro = 'Polaris'
>>> Astro = 'Betelgeuse'
```

son distintas.

Podemos crear varias variables en un mismo renglón

```python
>>> pasos = 500; nombre='Laura'; pi = 3.14;
>>> x, y, z = 10.7, 5.1, -2.3
>>> a, b, c = 1.0  #  las tres variables toman el valor 1.0
```

Si realizamos una operación larga y requerimos otro renglón
contamos con el operador `\` para continuar la linea

```python
suma = 1 + 2 + 3 + 4 + \
       5 + 6 + 7
```

También podemos utilizar paréntesis para una continuación implícita de renglón
(método preferido)

```python
suma = (1 + 2 + 3 + 4 +
       5 + 6 + 7)
```

Esta característica nos permite unir strings largos de una manera más legible

```python
>>> poema = ("Dos cuerpos frente a frente "
             "son a veces raíces "
             "en la noche enlazadas. "
             "Octavio Paz")
>>> print(poema)  #  muestra el `poema` en la terminal (stdout)
```

Como podemos apreciar,
los comentarios se crean con el operador `#`;
todo lo que se encuentre a la derecha de este,
se considera comentario y es ignorado por el intérprete.

Los objetos mencionados en esta sección son del tipo
**inmutable**
(como ya hemos visto en clase),
es decir,
no pueden ser modificados;
cada que creemos haberlos modificado realmente hemos creado un nuevo objeto.

```python
>>> carros = 'Bently'
>>> id(carros)  #  dirección de memoria para `carros`
4316417072  #  este número es distinto para ti
>>> carros += ', Ferrari'  #  carros = carros + ', Ferrari'
>>> print(carros)
Bently, Ferrari
>>> id(carros)
4316404400  #  el id ha cambiado al ser un nuevo objeto
```

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
(raíz cuadrada, exponencial, logaritmo),
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

Para tomar el logaritmo de una base deseada empleamos

    # Logarítmos
    print('Logaritmos')

    # logaritmo de base e
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

Un **string** es un objeto que actúa como contenedor de caracteres.
En términos de python un string es un **iterable**,
esto es,
un objeto que es capaz de regresar sus elementos uno a la vez;
los elementos de un **string** son cada uno de sus caracteres.

Para crear un string podemos utilizar comillas simples

```python
saludo = 'Hola'
```

comillas dobles

```python
frase = "corre Forest"
```

o bien transformando un objeto en un string mediante la función `str`
(de forma más precisa este es un constructor de objetos de clase `str`)

```python
altura = str(1.80)  #  '1.80'
```

> [!NOTE]
>
> Podemos aplicar la función `str` a cualquier objeto en python.
> Esto debido a que todos los objetos heredan de la clase `object`
> y esta implementa el método `__str__`
> (método dunder o de doble guión bajo).

Este método también nos permite crear strings vacíos mediante

```python
msg = str()  #  ''
```

lo cuál se puede lograr con `msg = ''` si prefieres.

Si nuestro objeto debe contener una comilla `'`,
debemos definir el string utilizando comillas dobles `"`:
```python
negocio = "Joe's"
print(negocio)  #  Joe's
```

De igual manera,
utilizamos `'` si necesitamos incluir `"`.

Para iterar sobre cada uno de los elementos de un string utilizamos la estructura `for`

```python
>>> fruta = 'pera'
>>> for char in fruta:
...     print(char)
...
p
e
r
a
```

Los strings son iterables de un tipo especial conocido como **secuencias**
cuyas características se discutirán en la siguiente sección;
**no todos los iterables son secuencias**.

Una función muy útil para toda secuencia es
`len`,
la cuál regresa su número de elementos.
Por ejemplo,

```python
>>> texto = 'Mi perrito'
>>> len(texto)
10
```

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

* Para verificar si dos strings son idénticos utilizamos `==`,
  mientras que `!=` nos informa si los strings son distintos.

* El resto de operadores nos permiten determinar el orden alfabético entre dos strings,
  comparando el valor unicode del primer carácter que difiera entre estos.

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
**Para conocer el valor unicode de un carácter,
utilizamos la función `ord`**
(acepta *strings* de un sólo carácter,
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

    In [6]: nombre_correcto = nombre.replace('Maria', 'Elena')

    In [7]: texto = ' Tenemos espacio  '

    In [8]: texto.strip()

    In [9]: texto.lstrip()

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

Un método muy útil es `join`,
el cual crea un string uniendo los elemento de un objeto iterable
como una lista, tupla, diccionario, etc
(definición más abajo)
con el separador que yo desee.
La sintaxis es la siguiente

```python
separador.join(iterable)
```

dónde el `separador` es un string y el `iterable` solo debe tener strings como elementos.
Por ejemplo,

```python
cafes = ' '.join(['capuchino', 'latte'])
print(cafes)  #  'capuchino latte'
```

crea un string uniendo cada elemento de la lista con un espacio como separador.
O podemos ejecutar

```python
# unir mediante coma y espacio
bebidas = ', '.join(('jugo', 'cerveza', 'tequila'))
print(bebidas)  #  'jugo, cerveza, tequila'

# unir mediante renglón nuevo
cafes = '\n'.join(('espresso', 'frappé'))
print(cafes)
```

para unir los elementos de una tupla mediante una coma y un espacio,
o bien mediante un nuevo renglón.
Este método regresa un nuevo string y no afecta el `iterable`.

#### Membresía

Para verificar si un conjunto contiguo de caracteres,
conocido como substring,
pertenece a un string,
contamos con la **palabra reservada** `in`.
Por ejemplo,

```python
In [1] estudiante = 'Estudiante ID\nScarlett 201456'

In [2] '201456' in estudiante
Out[2] True
```

Si deseas checar que un substring no pertenezca a un string,
contamos con `not in`:

```python
In [3] 'Bart' not in nombre
Out[3] True
```

#### Indexación

Los strings
(al igual que toda secuencia)
cuentan con índices que identifican cada carácter
(elemento).
Estos índices comienzan en cero y
nos permite extraer uno o más elementos de la secuencia.

Aquí mostramos un string con sus índices correspondientes:

| 0 | 1 | 2 | 3 | 4 |
| - | - | - | - | - |
| p | a | s | t | o |

```python
palabra = 'pasto'
In [13]: palabra[2]
Out[13]: 's'
```

También podemos referirnos a los elementos de una secuencia mediante índices negativos.
En este caso,
el último carácter toma el índice -1,
el penúltimo -2 y así sucesivamente.

| -5 | -4 | -3 | -2 | -1 |
| -- | -- | -- | -- | -- |
|  p |  a |  s |  t |  o |

Los índices negativos nos facilitan llamar caracteres al final de la secuencia fácilmente.

```python
palabra = 'pasto'
In [14]: palabra[-2]
Out[14]: 't'
```

También contamos con un método que nos regresa el índice de la primera aparición de un carácter
o substring en un string dado,
el método `find`.
Si el método encuentra el substring,
regresa el índice de inicio,
en caso contrario regresa `-1`
(nunca regresa un error).
Por ejemplo,

```python
In [1]: obra_civil = 'carretera'

In [2]: obra_civil.find('a')
Out[2]: 1

In [3]: obra_civil.find('ete')
Out[3]: 4

In [4]: obra_civil.find('Era')
Out[4]: -1
```

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

Ejemplo 2: Se hace una venta de boletos de lotería con las siguientes reglas:
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

## Secuencias

En python,
una **secuencia** es una colección de objetos ordenados,
de tal manera que cada elemento se identifica por un índice entero.

Definimos como secuencia todo objeto de python que cumpla con las siguientes tres condiciones:

1. Es **iterable**:

    El objeto tiene elementos sobre los cuales podemos iterar en un bucle `for`.

2. Tiene una **longitud** la cual se obtiene mediante la función `len`:

    Se llama longitud al número de elementos que contiene.

3. Se puede acceder a sus elementos mediante corchetes `[]`,
utilizando un **índice** entero el cual **empieza en cero**:

    Los elementos tienen un orden fijo y predecible.

Las secuencias se pueden clasificar en
**mutables** e **inmutables**;
llamamos mutables a aquellas cuyos elementos pueden cambiar después de su creación.

Python cuenta con las siguientes secuencias principales:
* `list` (mutable),
* `tuple` (inmutable),
* `range` (inmutable),
* `str` (inmutable),
* `byte` (inmutable)
y
* `bytearray` (mutable).

Observemos estas tres propiedades:

```python
In [1]: lista = [2.0, 'hola', True]

In [2]: tupla = ('bye', False, 3)

In [3]: rango = range(10)  # Enteros del 0 al 9

In [4]: print(type(lista), type(tupla), type(rango))

In [5]: lista[1]

In [6]: tupla[-1]

In [7]: rango[3]

In [8]: print(len(rango), len(tupla))

In [9]: for num in rango:
   ...:     print(num)

In [10]: for elem in lista:
    ...:    print(elem)

In [11]: for char in 'Hello!':
    ...:    print(char)
```

En esta parte hemos hecho uso del bucle `for`
el cual discutiremos en la siguiente sección junto a la secuencia `range`.

> [!NOTE]
>
> Observa que todas las secuencias son iterables por definición.
> Sin embargo,
> existen también otros objetos sobre los que podemos iterar
> que no permiten el uso de índices,
> es decir,
> existen iterables que no son secuencias
> (diccionarios, conjuntos, generadores, etc.).

En ocasiones debemos tratar con secuencias muy largas.
Para tales casos es recomendable utilizar la
**continuación implícita de líneas de python**;
los paréntesis, corchetes y llaves
se pueden extender a lo largo de líneas en python,
luego el intérprete se encarga de procesar el contenido
en un solo objeto.

La recomendación en PEP8
([ver aquí](https://peps.python.org/pep-0008/#code-lay-out))
para listas y tuplas
es mantener líneas de código a un máximo de 79 caracteres
y utilizar la continuación implícita de líneas.
Al cerrar la lista o la tupla,
tenemos dos opciones de alineación:

1. Alineamos el corchete o paréntesis (o llave) con el primer carácter de la última línea

```python
comidas = [
    'tacos', 'carnitas', 'sushi',
    'pizza', 'pozole', 'menudo',
    ]
```

2. Alineamos con respecto al primer carácter de la linea que comenzó la construcción multilínea

```python
comidas = (
    'tacos', 'carnitas', 'sushi',
    'pizza', 'pozole', 'menudo',
)
```

Por cierto,
la continuación implícita funciona en todos los casos,
al definir una función o realizar una operación:

```python
# Se recomienda alinear argumentos con el delimitador de apertura
def my_fun(arg1, arg2, arg3,
           arg4, arg5):
    pass

# O cuando tenemos una función con nombre largo
# alineamos con cuatro espacios abajo de su nombre
def este_nombre_esta_largo(arg1, arg2,
        arg3, arg4, arg5):
    pass

# En una operación largas
mensaje = 'Este es un mensaje: '
nombre = 'jesus'
resultado = ( mensaje.upper() + 'Hello ' +
    f'{nombre.title()}' + '!' )
print(resultado)  #  esto es un string no una tupla
```

### Creación de listas y tuplas

Además del uso de corchetes y paréntesis para crear una lista o tupla,
respectivamente,
contamos con constructores de estas clases.
Para la creación de una lista a partir de un iterable,
contamos con la función `list`,
mientas que para una tupla existe `tuple`.

Cuando `list` recibe un iterable
regresa una nueva lista con los elementos del iterable.
Si el argumento recibido ya es una lista,
entonces retorna una copia superficial
(*shallow copy*)
de la misma,
y si no se introduce ningún argumento,
retorna una lista vacía.
Las mismas reglas aplican para `tuple`.

Por ejemplo,

```python
In [1]: lista = list('Robocop')

In [2]: lista_vacia = list()

In [3]: tupla = tuple([True, True, False])

In [4]: print(lista, lista_vacia, tupla)

In [5]: lista_copia = list(lista)

In [6]: print(id(lista), id(lista_copia))
```

Para crear listas vacías basta con
`L = []` o bien `L = list()`,
mientras que para una tupla vacía tenemos
`t = ()` o `t = tuple()`.
El caso de una tupla con un sólo elemento es especial,
y se logra mediante
`tupla = (3,)` (observa la coma);
la asignación `t = (3)`
resulta en que `t` es el `int` 3,
no una tupla con ese elemento.

Por otro lado,
python transforma valores separados por una coma en una tupla
de manera implícita, de tal manera que

```python
In [1]: carros = 'Versa', 'Civic', 'K4'

In [2]: print(type(carros))
<class 'tuple'>
```

Las listas y las tuplas pueden contener elementos de cualquier tipo,
de tal manera que una tupla puede contener otra tupla

```python
tupla = ('Maria', 'Roberto', (12, 15))
```

o bien otro iterador
```python
tupla = ('Maria', [True, False], range(10))
```

### Rebanado (*slicing*)

Además de las propiedades descritas para toda secuencia,
las secuencias principales mencionadas anteriormente
**soportan el rebanado** (*slicing*).
Este utiliza un rango de índices para obtener
nuevos objetos del mismo tipo,
pero solo con los elementos dados por el rango.
Por ejemplo,
si declaramos la lista
`L = [2, 6.1, 'a', 'b']`,
entonces `L[1:3]` regresa `[6.1, 'a']`,
es decir,
una nueva lista cuyos elementos corresponden a los índices `1` y `2` de `L`.

> [!NOTE]
>
> No todas las secuencias  te permiten el *slicing*.
> Un ejemplo es el objeto mutable `deque`
> (*double end queue*)
> del módulo `collections` de la librería estándar.
> El `deque` es una estructura similar a una lista,
> dónde las operaciones para agregar y
> eliminar elementos al principio o fin de la secuencia
> son operaciones muy eficientes
> (tiene orden O(1) en lugar de O(n) de una lista).

Las reglas para el *slicing* fueron abordadas con los *strings*.
Aquí unos ejemplos

```python
tupla = tuple('abcdefgh')
personajes_avatar = ['Aang', 'Katara', 'Sokka', 'Toph', 'Zuko']

print(tupla)
print(tupla[0:3])
print(tupla[1:7])
print(tupla[1:7:2])
print(tupla[1::2])

print(lista[:2])
print(lista[-2:])
print(lista[1:])
print(lista[::2])
print(lista[::-1])
```

### Desempaquetado

Cuando tenemos un **iterable** con pocos elementos,
podemos extraerlos utilizando una tupla o lista
del lado izquierdo de una asignación,
con una
variable por elemento
como mostramos a continuación

```python
(nombre, edad, altura) = ['Maria', 19, 1.62]
[a, b] = "Hi"
```

Ya que python crea de manera implícita una tupla al separar valores por una coma,
podemos omitir el paréntesis de una tupla y declarar

```python
grupo, ids = '5_1', [153642, 762231, 384994]  #  tuplas ambos lados

punto = (-1.2, 3.8, 1.4)
x, y, z = punto
```

Hacemos notar que el desempaquetado funciona con cualquier iterable,
no solo secuencias.

Esta funcionalidad nos permite escribir código más limpio y legible que la utilización de índices para tales casos.
Hay ocasiones que son de bastante ayuda,
como al iterar sobre un iterable que contiene iterables.
Por ejemplo,
digamos que contamos con la siguiente información

```python
examenes = [('Luis', 8), ('Penelope', 9), ('Liz', 7)]
```

y deseamos agregar la calificación de cada estudiante a otras calificaciones que ya tenemos en una base de datos.
Si no contáramos con el desempaquetado,
tendríamos que iterar por cada elemento,
el cual es una tupla,
y después indexar para extraer cada elemento.
Observa que

```python
for examen in examenes:
    print(examen)
```

retorna

```python
('Luis', 8)
('Penelope', 9)
('Liz', 7)
```

lo que muestra que cada elemento es una tupla.
Utilizando el desempaquetado en la propia declaración de `for` resulta en

```python
for estudiante, calif in examenes:
    print(estudiante)
    print(calif)
    print()  #  línea en blanco
```

obteniendo acceso a cada elemento de la tupla directamente.

#### Desempaquetado extendido

Por último,
discutimos otro uso importante.
Existe una sintaxis de desempaquetado que nos permite atrapar múltiples elementos de un iterable en vez de uno a la vez;
al agregar un prefijo `*` a una variable,
esta se convierte en **atrapa todo**,
capturando en una **lista** todos los valores que no fueron asignados a las variables normales
(**obligatorias**).
Por ejemplo,

```python
id, *info = (125631, 'cocinero', 22, '6 meses')
print(id)  #  125631
print(info)  #  ['cocinero', 22, '6 meses']

negocio, *trabajadores, direccion = (
    'sushi', 'Hulk', 'Thor', 'Viuda Negra', 'Cd. Universitaria'
    )
print(negocio)  #  'sushi'
print(trabajadores)  #  ['Hulk', 'Thor', 'Viuda Negra']
print(direccion)  #  'Cd. Universitaria'
```

El número de variables obligatorias
(sin `*`)
debe ser menor o igual a los elementos en el iterable;
en el caso de ser igual,
la lista de la variable *estrellada* estará vacía.

```python
*a, b, c = [3, 4]
print(a)
print(b)
print(c)
# Imprime
# []
# 3
# 4
```

Observa que

```python
numeros = range(5)
val1, *val2, val3 = numeros # val1=0, val2=[1, 2, 3], val3=4
```

es mucho más claro que

```python
numeros = range(5)
val1, val2, val3 = numeros[0], numeros[1:-1], numeros[-1]
```

Esta sintaxis también se puede emplear durante la asignación en un bucle `for`

```python
serie_avatar = (
    ('Aang', 'Avatar', 112),
    ('Katara', 'Maestra agua', 14),
    ('Sokka', 'Simple humano', 15),
    )
for name, *info in serie_avatar:
    print(name)
    print(info)
    print()
```
el cual produce

```python
Aang
['Avatar', 112]

Katara
['Maestra agua', 14]

Sokka
['Simple humano', 15]
```


### Concatenación

Otra operación que las secuencias soportan frecuentemente,
aunque no siempre,
es la concatenación;
`range` no la soporta pero las demás secuencias principales sí.
Esta se logra mediante la adición como mostramos abajo.

```python
In[1]: frutas = ('manzana', 'plátano')

In[2]: verduras = ('tomate', 'cebolla', 'papa')

In [3]: frutas + verduras
Out[3]: ('manzana', 'plátano', 'tomate', 'cebolla', 'papa')
```

Para lograr la concatenación,
debemos emplear secuencias del mismo tipo;
**si intentamos concatenar una lista con una tupla obtendremos un**
`TypeError`.
La excepción son las secuencias `byte` y `bytearray`,
las cuales pueden mezclarse.
La operación de concatenación mediante `+` resulta en un nuevo objeto:

```python
ciudades_sin = ['Culiacán', 'Mochis']
ciudades_jal = ['Arandas']

ciudades = ciudades_sin + ciudades_jal
print(f"id(ciudades_sin): {id(ciudades_sin)}")
print(f"id(ciudades_jal): {id(ciudades_jal)}")
print(f"id(ciudades): {id(ciudades)}")
```

Sin embargo,
**si utilizamos el operador de asignación aumentado** `+=`
para llevar acabo una concatenación
**en una lista (objeto mutable)**,
**el resultado corresponderá al mismo objeto** pero con nuevos elementos.
**Para objetos inmutables** como una tupla o un string,
**el resultado siempre será un nuevo objeto**.
Aquí un ejemplo para una lista

```python
# Definir lista (mutable) y mostrar id
alturas_estudiantes = [1.68, 1.79]
print(f'alturas_estudiantes = {alturas_estudiantes}')
print(f"id de lista 'alturas_estudiantes': {id(alturas_estudiantes)}")
print()  # línea en blanco

# Concatenar mediante += y mostrar id
nuevas_alturas = [1.73, 1.82, 1.70]
alturas_estudiantes += nuevas_alturas
print(alturas_estudiantes)
print(f"id de 'alturas_estudiantes' posterior a '+=': {id(alturas_estudiantes)}")
```

Y acá para un string

```python
# Definir string (inmutable) y mostrar id
estudiantes = 'Juan, Maria'
print(f'estudiantes = {estudiantes}')
print(f"id de string 'estudiantes' (inmutable): {id(estudiantes)}")
print()  # línea en blanco

# Concatenar mediante += y mostrar id
estudiantes += ', Rosa'
print(estudiantes)
print(f"id de 'estudiantes' posterior a '+=': {id(estudiantes)}")
```

> [!NOTE]
>
> Cada que utilizamos la concatenación,
> python aloja memoria para el nuevo objeto que resulta de la operación,
> dejando intactos a los objetos usados en la suma.
> Además del gasto de memoria,
> debemos considerar que esto genera un pequeño *overhead*.
> Debemos tener especial consideración cuando realizamos concatenaciones dentro de un bucle,
> lo cual genera un costo en tiempo de ejecución de orden cuadrático y puede generarse mucho uso de memoria.
> Para solventar esta situación,
> en el caso de un objeto mutable como la lista,
> contamos con el método `extend` o el operador `+=`,
> y en el caso de strings tenemos a `join`.

### Comparaciones

La mayoría de las secuencias principales soportan los operadores de comparación ordinarios:
`>`, `>=`, `==`, `!=`, `<` y `<=`.
Las comparaciones en todos los casos son lexicográficas,
es decir,
se comparan los elementos índice por índice de la secuencia.

> [!NOTE]
> Las secuencias principales soportan `==` y `!=`, pero `range` no soporta comparaciones de desigualdad

El operador `==` realiza una serie de comparaciones:
checa que las dos secuencias sean del mismo tipo,
checa que ambas tengan la misma longitud
y finalmente checa la igualdad de cada elemento mediante
`a[j] == b[j]`,
dónde `a` y `b` son las dos secuencias.
Si alguna de estas comparaciones falla regresa `False`.
Por ejemplo,

```python
print([1, 2, 3] == [1.0, 2+0j, 3])  #  True

print([1, 2, 3] == [2, 1, 3])  #  False (lexicografía)

print([1, 2, 3] == (1, 2, 3))  #  False  (tipos)

print([1, 2, 3] == [1, 2, 3, 3])  #  False  (longitud)
```

Observa que `==` nunca regresa una `Exception` (error).

Reglas similares aplican para `!=` el cual checa que las secuencias sean distintas:

```python
print([1, 2, 3] != [2, 1, 3])  #  True

print([1, 2, 3] != [1.0, 2+0j, 3])  #  False

print([1, 2, 3] != (1, 2, 3))  #  True

print([1, 2, 3] != [1, 2, 3, 3])  #  True
```

Los operadores `>` y `<` solo comparan secuencias del mismo tipo;
`[3, 1] > (1, 0)` regresa un `TypeError`.
El resultado de la comparación resulta del primer elemento que sea distinto en ambas secuencias.
Por ejemplo,

```python
print((5, 3, 8) < (5, 6, 1))  #  True (ya que 3 < 6)

print([5, 3, 8] > [5, 3, -2, 9])  #  True (ya que 8 > -2)

print('cazo' > 'carretera')  #  True (ya que 'z' > 'r')
                              #  (o bien ord('z') > ord('r'))
```

En el caso de que una secuencia este contenida en otra del mismo tipo pero con más elementos decimos que la secuencia grande es mayor, esto es

```python
print('Caborca' > 'Cabo')  #  True

print([1, 2, 3] < [1, 2, 3, 0])  #  True
```

Las mismas reglas aplican para `>=` y `<=`;
se compara el primer elemento distinto en las secuencias mediante el operador correspondiente,
además,
una secuencia contenida en otra más grande se considera menor.

### Métodos para listas

Las listas y tuplas son objetos como todo en python.
Como tal,
tienen métodos que actúan sobre sus instancias.

Las listas,
al ser objetos mutables,
nos permiten cambiar elementos,
agregar y eliminarlos.

#### Agregar elementos

Ocurre frecuentemente que desconocemos el contenido de una lista por adelantado.
Es común que empecemos con una lista vacía y agreguemos elementos durante la marcha con el comando `append`

```python
alumnos = []
alumnos.append('Mayra')
alumnos.append('Jose')
alumnos.append('Arturo')

print(alumnos)
```

Para hacerlo más interesante podemos agregar aleatoriedad con el módulo `random`

```python
import random

dado = (1, 2, 3, 4, 5, 6)
juego = []  # lista vacía
for i in range(10): # esto hará que el bucle corra 10 veces
    lanzamiento = random.choice(dado)
    juego.append(lanzamiento)
print(juego)
```

Como hemos visto,
`append` agrega un elemento al final de la lista pero
¿Qué tal si quiero agregar un elemento en cualquier ubicación de la lista?
Para eso contamos con el método `insert(indice, elem)`

```python
L = ['a', 'b', 'd', 'e']
L.insert(2, 'c')  # Inserta 'c' en el índice 2
print(L)  # ['a', 'b', 'c', 'd', 'e']
```

También contamos con la opción de agregar varios elemento al final de la lista.
Para lograr esto ya hemos hablado sobre la concatenación.
Sin embargo,
contamos también con el método `extend(iterable)`.
La diferencia en este caso es que no se crea una nueva lista
sino que se agregan los elementos de un `iterable` al final de la lista original.
Otra diferencia es que se permite usar cualquier `iterable`,
mientras con la concatenación solo podemos utilizar otra lista.

```python
L = [1, 2, 3, 4]
L.extend((5, 6))
print(L)  #  [1, 2, 3, 4, 5, 6]
```

Por último,
podemos utilizar *slicing* para insertar la cantidad deseada de elementos en una posición deseada.
La sintaxis es la siguiente:

```python
lista[indice:indice] = [elementos]  # cualquier iterable a la derecha
```

Lo que hacemos es indicar el índice dónde queremos realizar la inserción
de los elementos que introduzcamos en el iterable de la derecha.
Por ejemplo,

```python
L = [5, 9, 1, 0, 3]
L[2:2] = [7]
print(L)  #  [5, 9, 7, 1, 0, 3]
```

Observa que ocupamos utilizar un iterable del lado derecho incluso para introducir un elemento.
También hacemos notar que los elementos que ya se encontraban en la lista se recorren en orden sin eliminarlos.
Además,
esta operación modifica el contenido de la lista pero no crea una lista nueva.
El objeto que se encuentra a la derecha puede ser cualquier iterable

```python
L = [5, 9, 1, 0, 3]
L[3:3] = 'Hola'
print(L)  #  [5, 9, 1, 'H', 'o', 'l', 'a', 0, 3]
```

#### Modificar elementos

Como ya sabemos,
podemos mandar llamar un elemento de la lista
(o cualquier secuencia)
utilizando su índice dentro de corchetes
(**recordemos que el índice inicial es cero**).
Esta misma notación se emplea para modificar un elemento.
Por ejemplo

```python
>>> libros = ['Farenheit 451', 'Un mundo feliz', '1984']
>>> libros[2] = 'Donde habitan las sirenas' # cambiar elemento 2
>>> print(libros)
['Farenheit 451', 'Un mundo feliz', 'Donde habitan las sirenas']
```

donde hemos modificado el elemento con índice 2.
Si deseamos modificar más de un elemento debemos utilizar
*slicing* mediante la sintaxis

```python
lista[start:end] = [elementos] # cualquier iterable a la derecha
```

dónde `start` es inclusivo y `end` exclusivo.
Si el rebanado y el iterable a la derecha contienen el mismo número de elementos,
el resultado es modificar los elementos correspondientes a los índices. Por ejemplo,

```python
alturas = [1.73, 1.82, 1.76, 1.90, 1.80]
# Modificar los elementos 2 y 3
alturas[2:4] = (1.68, 1.79)
print(alturas)  # [1.73, 1.82, 1.68, 1.79, 1.80]
```

Esta estrategia modifica la lista,
no crea una nueva.
Si el número de elementos en el iterable es menor a los elementos dados por los índices,
la lista reducirá su tamaño.
Si por el contrario,
el iterable contiene más elementos,
la lista crecerá.

```python
alturas = [1.73, 1.82, 1.76, 1.90, 1.80]
# Menos elementos que el rango
alturas[2:4] = [1.95]
print(alturas)  # [1.73, 1.82, 1.95, 1.80]

# Más elementos que el rango
letras = ['a', 'b', 'c', 'd', 'e']
letras[1:3] = ['A', 'B', 'C']
print(letras)  # ['a', 'A', 'B', 'C', 'd', 'e']
```

#### Eliminar elementos

Por otro lado,
para eliminar un elemento tenemos varias opciones.
Podemos utilizar el comando `del` seguido del elemento a eliminar como en

```python
calificaciones = [9.3, 8.2, 7.5, 8.8]

del calificaciones[1]  # elimina elemento con índice 1
print(calificaciones)  # resultado:[9.3, 7.5, 8.8]
```

También contamos con el método `pop`.
Este acepta un índice,
regresando y eliminando el elemento correspondiente.
Si no se le da un argumento regresa y elimina el último.

```python
>>> L = [2, 4, 6, 8, 10]
>>> L.pop() # retorna y elimina el último elemento
10
>>> print(L)
[2, 4, 6, 8]
>>> L.pop(2) # retorna y elimina el elemento con índice 2
6
>>> print(L)
[2, 4, 8]
```

Para eliminar la primera aparición de un elemento que tiene cierto valor,
utilizamos el método `remove`
e introducimos dicho valor.
Por ejemplo,

```python
mis_frutas = ['pera', 'manzana', 'fresa', 'manzana']
mis_frutas.remove('manzana')
print(mis_frutas)  # imprime ['pera', 'fresa', 'manzana']
```

nos permite eliminar la primera aparición de 'manzana'.

Si deseamos eliminar más de un elemento podemos utilizar el rebanado mediante

```python
list[start:end] = []  # cualquier iterable vacío a la derecha
```

Para eliminar los elementos 1 y 2 podemos ejecutar entonces

```python
consonantes = ['b', 'e', 'i', 'f', 'g']
consonantes[1:3] = []  #  ['b', 'f', 'g']
```

Por último,
para eliminar todos los elementos de una lista
contamos con su método `clear`.

```python
L = [3, 5, 8, 1, 0, 3]
L.clear()
print(L)  # imprime []
```

### Comprensiones de listas

Contamos con una manera más para la creación de listas
de manera concisa y legíble,
las comprensiones de listas.

Estas producen una lista a partir de otro iterable;
se aplica una expresión a cada elemento de dicho iterable agregando cada resultado a la lista.
A continuación mostramos la sintaxis:

```python
[expresion for var in iterable]
```

y ahora un ejemplo

```python
my_iter = (2, 4, 6)
my_list = [x**2 for x in my_iter]
print(my_list)  #  [4, 16, 36]
```

como podemos apreciar utilizamos `for` con la variable que
deseemos para extraer los elementos del iterable `my_iter`,
`x` en este caso,
y del lado izquierdo realizamos una operación cuyo resultado se agrega a la lista.

Podemos por ejemplo generar una lista de coordenadas con espaciamiento constante mediante

```python
coor = [0.5+num for num in range(6)]
print(coor)  #  [0.5, 1.5, 2.5, 3.5, 4.5, 5.5]
```

Las comprensiones también nos permiten utilizar lógica condicional mediante la sintaxis

```python
[expresion for var in iterable if condicion]
```

Veamos un ejemplo

```python
# filtrar solo los valores pares
numeros = (3, 5, 1, 4, 9, 2)
pares = [n for n in numeros if n % 2==0]
print(pares)  #  [4, 2]
```

Lo que sucede arriba es que `n` itera sobre cada valor de `numeros`,
al tomar un valor particular se evalua la condición lógica
`n % 2 == 0`
y cuando esta es verdadera se ejecuta la expresión de hasta la izquierda que en este caso es simplemente `n`
(agregar el valor que satisface mi filtro).

Podemos también usarla para limpiar texto

```python
texto = [' Hola', '  mis ', '  ', 'amigos ']
# recuerda que un string vacío es falsy
texto_limpio = [word.strip() for word in texto if word.strip()]
print(texto_limpio)  #  ['Hola', 'mis', 'amigos']
```

Por último,
iteramos sobre dos o más iterables con

```python
[expresion for x in iter1 for y in iter2]
```

dónde el primer `for` actúa como el bucle exterior y el otro como interior.
En otras palabras,
esta sintaxis equivale a

```python
my_list = []
for x in iter1:
    for y in iter2:
        my_list.append(expresion)
```

Un ejemplo vale mil palabras

```python
iter1 = (1, 2)
iter2 = [3, 4]
my_list = [(x, y) for x in iter1 for y in iter2]
print(my_list)  #  [(1, 3), (1, 4), (2, 3), (2, 4)]
```

> [!NOTE]
>
> Las comprensiones de lista son normalmente de 10% a 30%
> más veloces que los bucles `for` debido a que python
> las optimiza a nivel de *bytecode*.

### Métodos para tuplas

Debido a que las tuplas son inmutables,
no podemos agregar,
eliminar,
ni modificar elementos.
Para estas estructuras contamos con dos métodos:
`count` y `index`.

El primer método tiene la sintaxis
`count(elemento)`
y cuenta el número de apariciones del `elemento` dado

```python
tupla = (3, 4, [1, 2], [1], [3], [1, 2])
print(tupla.count(3))
print(tupla.count([1, 2]))

palabra = tuple('pelele')
print(palabra.count('e'))
```

El segundo toma la forma
`index(elemento, start, stop)`,
donde los índices `start` y `stop` son opcionales.
Este método regresa el índice menor donde el `elemento` se encuentra;
solo busca en los elementos comprendidos desde el índice `start` (inclusivo)
hasta el `stop` (exclusivo).
Por default,
`start` es cero
y `stop` es el final
(en realidad es un entero grandísimo).

```python
tupla = (35, 12, 39, 15, 12)
print(tupla.index(12))  #  1

palabra = tuple('pelele')
print(palabra.index('e', 2))  # 3 (start=2, stop=final)
```

Si el elemento no se encuentra,
el método regresa un `ValueError`:

```python
tupla = (35, 12, 39, 15, 12)
tupla.index(10)  #  ValueError
```

### Funciones para iterables

Habiendo discutido los métodos para las secuencias principales,
mostramos ahora algunas funciones que aplican para todo **iterable**.

Las siguientes funciones toman a un iterable como argumento:

* `list`, `tuple`, `set`, `dict`

    Estas funciones crean una lista, tupla, conjunto o diccionario, respectivamente, a partir de los elementos del iterable.

    ```python
    estudiantes = set(['Carlos', 'Laura', 'Liza'])
    print(estudiantes)  #  {'Carlos', 'Liza', 'Laura'}
    ```

* `enumerate`

    En un bucle `for` esta función nos permite extraer al mismo
    tiempo un contador de cada elemento y el elemento mismo

    ```python
    # funciona con cualquier iterable (aquí escogimos una lista)
    my_iter = ['a', 'b', 'c']
    for count, elem in enumerate(my_iter):
        print(count, elem)
    #imprime
    # 0 a
    # 1 b
    # 2 c
    ```

    Esto resulta mucho más legible en muchos casos.
    Por ejemplo,
    supongamos que tengo el registro de un estudiante con sus datos en una lista
    y decido agregar `None` para la información desconocida,
    podemos querer encontrar en que índices de la lista ocurre
    esto mediante

    ```python
    estudiante = ['Laura', 21, None, 'Culiacán', None,
                  'informática']
    indices_none = []
    idx = 0
    for info in estudiante:
        if info is None:
            indices_none.append(idx)
        idx += 1
    print(indices_none)
    ```

    pero lo podemos hacer más claro mediante

    ```python
    estudiante = ['Laura', 21, None, 'Culiacán', None,
                  'informática']
    indices_none = []
    for idx, info in enumerate(estudiante):
        if info is None:
            indices_none.append(idx)
    print(indices_none)
    ```

* `sum`

    Retorna la suma de los elementos en el iterable

    ```python
    # suma los enteros del 0 al 100
    print(sum(range(101)))   # ¿Puedes hacerlo a mano?
    ```

* `max`, `min`

    Retorna el valor máximo o mínimo de un iterable.
    Se permite introducir más de un argumento;
    en este caso se retorna el argumento de valor máximo o mínimo.

    > [!NOTE]
    >
    > Para obtener dicho valor,
    > python itera sobre cada elemento del iterador,
    > o sobre los argumentos,
    > y emplea el operador `>` en el caso de `max`,
    > o `<` en el caso de `min`.
    > No se permiten números complejos por default
    > ya que no están definidas las comparaciones
    > (`>` o `<`)
    > para este tipo.

    Para un solo iterable tenemos

    ```python
    # tupla
    calif = (8.4, 9.3, 9.7, 8.1)
    print(max(calif))  #  9.7

    # conjunto
    palabras = {'carro', 'carretera'}
    print(min(palabras))  #  'carretera'  (¿Porqué?)

    # string
    print(min('estupendo'))  #  ¿Qué imprime?

    # lista de tuplas
    # comparación elemento a elemento (tupla vs tupla)
    precios = [
        ('manzana', 10.25),
        ('platano', 27.90),
        ('mango', 36.99)
        ]
    print(min(precios))  # ('mango', 36.99)  (¿Porqué?)
    ```

    Observa que en el último ejemplo la comparación es entre tuplas;
    lo que estamos obteniendo es la comparación del primer elemento entre tuplas.
    Si lo que deseamos es el precio mínimo,
    debemos comparar los segundos elementos.

    Python nos permite utilizar una función de un solo argumento
    para personalizar el criterio de comparación
    mediante la opción `key`.
    Por ejemplo,
    si deseamos comparar los precios en el caso anterior

    ```python
    print(min(precios, key=lambda elem:elem[1]))  # ('manzana', 10.25)
    ```

    donde la función lambda
    (ver sección sobre funciones)
    se ejecuta para cada elemento del iterable y posteriormente se realiza la comparación con `<`.

    Este mismo truco lo puedo utilizar para comparar números complejos,
    los cuales compararé utilizando su módulo
    (el módulo de un número complejo
    $\sqrt{{\Re(x)}^2 + {\Im(x)}^2}$
    se encuentra mediante la función `abs` de python)

    ```python
    print(abs(3+4j))  #  5.0 (math.sqrt(3**2 + 4**2))
    print(abs(4j))  #  4.0
    print(abs(-3))  #  3.0

    psi = [3+4j, 4j, -3]
    print(max(psi, key=abs))  #  (3+4j)
    ```

    En caso de que el iterable este vacío,
    estas funciones retornan un `ValueError`;
    podemos evitar esto utilizando el argumento opcional `default`
    con el valor deseado para estos casos.
    Por ejemplo,

    ```python
    # lista vacía
    valor_maximo = max([], default='empty')
    print(valor_maximo)  #  'empty'
    ```

    Finalmente, para más de un argumento

    ```python
    # Esta notación permite extraer una objeto dentro de un módulo
    # (constante, función, clase)
    from math import pi   # extraer el número pi del módulo math
    print(max(3, pi, 2.7))  #  3.14159...
    ```

* `sorted`

    Regresa una nueva lista con los elementos ordenados de un iterable sin modificarlo.

    ```python
    lista = [4, 9, 1, -3, 5, 4]
    lista_ordenada = sorted(lista)

    print(f'lista: {lista}')
    print(f'lista_ordenada: {lista_ordenada}') # [-3, 1, 4, 4, 5, 9]

    # `sorted` regresa una lista nueva para todo iterable
    print(f"id(lista): {id(lista)}")
    print(f"id(lista_ordenada): {id(lista_ordenada)}")

    # `sorted` ordena cada elemento de un iterable con las reglas
    # que apliquen a los elementos que se tengan (tuplas aquí).
    precios = (
        ('manzana', 10.25),
        ('platano', 27.90),
        ('mango', 36.99)
        )
    print(sorted(precios))  # lista de tuplas con frutas ordenadas
                            # [('mango', 36.99),
                            #  ('manzana', 10.25),
                            #  ('platano', 27.90)]
    ```

    Esta función también cuenta con el parámetro opcional `key` para personalizar el criterio de ordenamiento
    (recuerda que `key` acepta una función de un argumento).
    Para ordenar nuestros precios por el valor numérico
    ejecutamos

    ```python
    def get_precio(elem):
        return elem[1]
    precios_ordenados = sorted(precios, key=get_precio)
    print(precios_ordenados)  # lista de tuplas con precios ordenados
    ```

    Además,
    esta función cuenta con el parámetro opcional `reverse`,
    el cual nos permite ordenar en orden descendente
    y el cual es `False` por default

    ```python
    print(sorted("auwnc", reverse=True))  # ['w', 'u', 'n', 'c', 'a']
    ```


* `any`, `all`

    La función `any` regresa `True` si al menos un elemento en el iterable es verdadero,
    en caso contrario `False`.

    Siendo más específicos,
    la función itera sobre los elementos,
    ejecutando `bool(elem)` en cada elemento `elem`;
    en el momento que `bool` resulte en `True`,
    la función regresa `True` inmediatamente sin checar otros miembros.

    > [!NOTE]
    >
    > Un objeto `obj` para el cual `bool(obj)` regrese `True`
    > se llama *truthy*,
    > en caso contrario se conoce como *falsy*.
    >
    > Valores *falsy*:
    >
    > * False
    > * número cero:
    >       `0`, `0.0`, `0j`
    > * iterables vacíos:
    >       `[]`, `()`, `''`, `{}`, `set()`, `range(0)`
    > * objeto nulo:
    >       `None`
    >
    > Valores *truthy*:
    >
    > * Todo lo demás
    > (esto incluye `'0'`, `[None]`, `[()]`)
    >
    >   ¿Qué piensas de `([])`?

    Por su parte `all` regresa `True` solo si todos los elementos son *truthy*.

    ```python
    print(any([False, 0, 1]))  #  True

    tupla = (0==1, 3>4)
    print(any(tupla))  #  False

    lista = [4>1, False or True, not False, '0']
    print(all(lista))  #  True

    rango = range(8)
    print(all(rango))  #  False
    ```


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
o si este se encuentra determinado por la longitud de una secuencia.
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
el bucle `while`.
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

Ejercicios

Cree un programa que lea dos enteros,
**a** y **b**,
donde **b** es distinto a cero.
Utilizando solo las operaciones algebraicas básicas
de suma y/o resta,
el programa nos debe dar el número entero de veces
que **b** cabe en **a**
(`a // b`),
así como el residuo
(`a % b`).
Obviamente no se permite utilizar `/`, `//`, ni `%`,
solo la suma y la resta.

## Funciones

La sintaxis para la creación de funciones en python es la siguiente:

```python
def nombre_funcion(arg1, arg2, ..., argN):
    '''
    docstring
    '''
    declaraciones
    return expresion
```

De acuerdo a las recomendaciones PEP8,
el nombre de la función `nombre_funcion`,
debería ser descriptivo,
usar un verbo,
así como un formato snake_case.

Los valores `arg1` hasta `argN` se conocen como parámetros,
siendo estos opcionales.
La sección **docstring** (opcional)
se refiere a lineas de texto que documentan nuestra función.
Es esta,
se anota el propósito de la función,
el tipo de datos de entrada y salida,
y en ocasiones detalles de implementación.
Para funciones sencillas una línea puede ser suficiente,
pero es común que esta sección se extienda.
Ver
[numpy docstyle](https://numpydoc.readthedocs.io/en/latest/format.html)
dónde se aborda un estilo de documentación muy empleado,
y luego visita
[aquí](https://numpydoc.readthedocs.io/en/latest/example.html#example)
para ver un ejemplo.

Para regresar un valor,
las funciones utilizan la palabra reservada `return`
seguida de la variable u objeto deseado.
Cuando el intérprete encuentra la palabra `return`,
el flujo retorna inmediatamente a la línea desde dónde se invocó la función,
sin importar si esta contiene  más lineas.

Si una función no cuenta con la palabra `return`,
el intérprete ejecuta todas las lineas de código,
de arriba a abajo,
y retorna el valor `None`,
es decir,
agrega como última línea para la función:
`return None`.

Una función sencilla puede verse así

```python
def saludar():
    return '¡Hola Matrix!'

saludo = saludar()
print(saludo)
```
la cual no toma argumentos y regresa la palabra `'Hola!'`.

Al estar planeando una aplicación,
es común anotar las funciones que requeriremos
para realizar la tarea sin aún ingresar su contenido.
Debido a que las funciones forzosamente deben tener al menos una linea en su cuerpo,
podemos usar en este caso la palabra reservada `pass`,
y de esta manera evitar que el intérprete arroje un error,
como en

```python
def aceleracion(planeta):
    pass

def distancia(gravedad, vel_inicial, tiempo):
    pass
```

Al llamar una función,
se crea un espacio local
(scope local)
con los parámetros de la función
(las variables),
a los cuales se le asignan los valores con que fue llamada esta.
Por ejemplo,

```python
import math

def distancia(x, y):
    """Regresa la distancia del origen a un punto dado.

    """
    dist = math.sqrt(x**2 + y**2)
    return dist

coor_x, coor_y = (3.0, 4.0)
print(distancia(coor_x, coor_y))
```

En el programa anterior,
python crea en el scope global los nombres:
`math`, `distancia`, `coor_x` y `coor_y`,
dónde las variables
`coor_x` y `coor_y` toman los valores de 3.0 y 4.0,
respectivamente.
Al invocar la función `distancia`,
se crea un scope local con las variables `x`, `y`,
las cuales toman los valores anteriores.
Posteriormente,
se crea la variable local `dist` y se regresa su valor,
retornando el flujo a la línea desde donde se llamo la función.
En este momento se elimina el scope local,
borrando todas sus variables.

### Parámetros opcionales

En python podemos asignar valores por default a los parámetros deseados de una función.
De esta manera podemos llamarla sin especificar un valor para estos argumentos.

La regla a respetar es que
**los parámetros opcionales deben aparecer al final**,
después de todos los obligatorios. Por ejemplo:

```python
def obtener_altura(tiempo, gravedad=9.8):
    """Distancia que recorre un objeto que se deja caer desde reposo.

    Parameters
    ----------
    tiempo : float o int
        `tiempo` de caída libre.
    gravedad : float, optional
        aceleración constante del objeto.

    Returns
    -------
    float
        La distancia recorrida por un objeto que experimenta aceleración
        constante.

    """
    return (gravedad * tiempo**2) / 2

# Altura de un pozo donde una piedra tarda 4 segundos en caer
print(obtener_altura(4))
```

Mientras que **una función especificada mediante**

```python
def sumar(a=3, b):
    return a + b
```

**retorna un error.**

Para llamar a la función `obtener_altura`,
podemos utilizar

```python
h_Tierra = obtener_altura(5)
```

en cuyo caso se asignan al scope local las variables
`tiempo = 5` y `gravedad = 9.8`.
O bien,
podemos llamar a la función mediante

```python
h_Luna = obtener_altura(5, 1.62)
```

en cuyo caso se tendrá
`tiempo = 5` y `gravedad = 1.62`.

En ambos casos,
respetamos el orden de los argumentos.
Podemos también introducir los parámetros en el orden deseado utilizando sus nombres.
Por ejemplo,

```python
h_Sol = obtener_altura(gravedad=274.2, tiempo=5)
```

Nota:
**No se pueden utilizar argumentos de posición después de un argumento de nombre (keyword argument)**;
Por ejemplo,
para la función

```python
def sumar(a, b, c=1):
    return a + b + c
```

es correcto llamarla de las siguientes formas:

```python
sumar(3, b=4)
sumar(3, b=4, c=-2)
```

pero las siguiente invocaciones retornan error de sintaxis (SyntaxError)

```python
sumar(a=3, 4)
sumar(3, b=4, 4)
```

ya que aparecen argumentos de posición después de un argumento de keyword.


### Funciones lambda

En python contamos con un segundo tipo de funciones,
conocidas como **funciones lambda**.
Estas funciones,
también llamadas en ocasiones **funciones anónimas**,
se describen en una sola línea y no tienen un nombre
(de ahí el nombre de anónimas)
a menos que sean almacenadas.

La instrucción

```python
lambda var1, ..., varN: expresion
```

regresa una función lambda con los `N` argumentos
`var1, var2, ..., varN`.
La declaración `expresion` indica la operación  que llevará acabo la función y no requiere la palabra `return`.
Observa que aunque podemos declarar la cantidad de argumentos deseados (o no declarar ninguno),
solo podemos introducir una expresión.

Estas funciones normalmente se utilizan como argumentos para funciones de mayor orden como
`map`, `filter`, `sort`,
las cuales requieren de una función para operar.
Sin embargo, también se pueden utilizar para declarar una operación sencilla que se está repitiendo en distintos lugares de nuestro código. Por ejemplo

```python
es_par = lambda x: x % 2 == 0

a = 11
print( es_par(a) )
```

o bien

```python
# Genera una parabola
x = [2, 4, 6, 8]
y = list(map( lambda num: num**2, x ))
```

Observa que estas funciones no tienen **docstring** ni tampoco pueden incluir bucles `for` ni decisiones con `if`.

A continuación mostramos un ejemplo más

```python
def log_2(x: int) -> tuple[int, int]:
    """Logaritmo entero de base 2 de un entero y su residuo.

    Regresa el entero 'm' más grande, tal que 2**m <= x,
    así como el residuo dado por x - 2**m.

    Parameters
    ----------
    x : int
        Un entero mayor a cero.

    Returns
    -------
    logaritmo : int
        Logaritmo de base 2 de `x`.
    residuo : int
        El residuo restante.

    Raises
    ------
    ValueError
        Si el argumento no es un entero positivo.

    Notes
    -----
    Se utilizan solo las operaciones aritméticas básicas.
    """
    # Checa que la entrada sea de tipo apropiado
    # De no ser así termina el programa con un error ValueError
    if not isinstance(x, int) or x <= 0:
        raise ValueError("El valor debe ser un entero positivo.")

    # El residuo se repite en diferentes secciones.
    # Es más adecuado determinarlo con una función.
    get_residue = lambda valor, potencia: valor - potencia

    # Caso base
    if x == 1:
        log = 0
        residuo = 0
        return (log, residuo)
    # En cualquier otro caso
    count = 1
    potencia = 2
    residuo = get_residue(x, potencia)
    while residuo > 0:
        count += 1
        potencia *= 2
        residuo = get_residue(x, potencia)
    # El residuo es cero o negativo en este punto
    # Actualiza count y residuo en el caso que residuo sea negativo
    if residuo < 0:
        count -= 1
        potencia //= 2 # esto es: potencia = potencia // 2
        residuo = get_residue(x, potencia)
    # count y residuo son correctos ahora
    log = count
    return (log, residuo)

x = int(input('Da un entero positivo: '))
print(f"(log_2, residuo) = {log_2(x)}")
```

Ejercicios

1. Cree una función que regrese si un niño tiene la altura para subirse a un juego.
La función debe aceptar la altura (en metros) de un niño y si esta es mayor a 1.5
la función debe retornar el booleano True. En otro caso debe regresar False.

2. Cree una función que le de un mensaje de bienvenida a un usuario.
La función debe pedirle al usuario que teclee su nombre y debe regresar
un string que contenga un mensaje de bienvenida con el nombre del usuario
(no se vale que sólo incluya el nombre de la persona).

3. Cree una función para calcular el precio de un producto con el interés correspondiente.
La función debe aceptar un precio y un interés (en porcentaje) y debe regresar el precio final.

4. Cree una función que calcule el área de un triángulo dadas sus tres longitudes
mediante la fórmula de Herón: [ver aquí](https://es.wikipedia.org/wiki/Fórmula_de_Herón)

5. Utiliza `map` y una **función lambda** para crear una lista con 101 coordenadas equidistantes del 0 al 1. Clave: recuerda la función `range`.

6. Grafica la función Gaussiana $\exp(-x^2)$ en el dominio
`[-3, 3]` mediante una línea continua utilizando 201 puntos equidistantes y la librería `matplotlib`.
La línea debe tener color rojo y un grosor de 1pt,
además,
el eje $X$ debe comprender [-3.5, 3.5]
y el eje $Y$ debe cubrir [-0.25, 1.25].
Para esto,
llena el código en las siguientes funciones

```python
import math
import matplotlib.pyplot as plt

# La siguiente función debe calcular la función Gaussiana
# en los puntos deseados.
# Los parámetros de entrada están dados por el punto de inicio
# x0, el final xf,
# y el numero de puntos en ese intervalo.
# La función debe regresar una tupla con dos listas:
# La primer lista debe contener los valores en x,
# y la segunda los valores de la Gaussiana en cada punto.
def Gaussiana(x0: float, xf: float, num: int) -> tuple(
        list[float], list[float]):
    """Agregar docstring

    """
    pass

# La siguiente función debe aceptar listas con las coordenadas
# en 'x' y en 'y',
# y debe graficarlos mediante una línea contínua de color rojo,
# grosor de linea de 1pt,
# ejes X de [-3.5, 3.5] y ejes Y de [-0.25, 1.25]
def graficar(x , y):
    """Agregar docstring

    """
    pass

x, y = Gaussiana(-3, 3, 201)
graficar(x, y)
```
Utiliza la la función `pyplot` de la librería externa `matplotlib`
para generar la gráfica.
Clave: investiga como funciona `pyplot` para generar una línea.


## Colecciones

En python se utiliza el termino colección para referirse a aquellos objetos
que contienen un número finito arbitrario
(cero o más)
de otros objetos
(cada uno con su tipo).
Estas se dividen en tres categorías principales:
secuencias
(las que hemos visto a excepción de los *strings*),
mapeos y conjuntos.

En esencia,
las colecciones son las listas,
tuplas, mapeos, conjuntos y
objetos que se encuentran en el módulo `collections`
de la librería estándar.
Hacemos notar que las colecciones son iterables.
**En esta sección hablamos sobre los mapeos y los conjuntos**.

> [!NOTE]
>
> Por cierto,
> un *strings* no es una colección
> ya que sus elementos no son objetos distintos almacenados
> mediante referencias;
> sus elementos siempre son *strings* nuevos de un sólo carácter.


> [!NOTE]
>
> Me gustaría darles una definición más precisa de lo que es una colección;
> una colección es un objeto que es iterable
> (tiene el método `__iter__` que nos permite iterar en un `for`),
> tiene un tamaño
> (posee el método `__len__` permitiéndonos usar la función `len`),
> es un contenedor,
> (tiene el método `__contains__` que nos permite probar membresía de elementos via `in`)
> y sus elementos se almacenan mediante referencias,
> permitiendo que estos puedan ser de cualquier tipo.

### Diccionarios (mapeos)

#### Creación y acceso

Un diccionario es una colección mutable de pares llave-valor
(mapeo).
Estos mapean llaves de tipo inmutable
(str, int, float, tuple)
a valores de cualquier tipo (mutable e inmutable).
Cada llave es única pero los valores se pueden repetir.

Podemos crear un diccionario mediante

```python
# mapea el 'code' a 'BKJ123' y 'route' a ['Mex', 'Frankfurt']
vuelo = {'code': 'BKJ123', 'route': ['Mex', 'Frankfurt']}
```

Cada llave se separa de su valor mediante `:`,
mientras que cada par se separa con comas.

A partir de python 3.7 los diccionarios mantienen el orden de inserción;
los pares clave-valor introducidos primero permanecen primero.

Otra manera de crearlos es inicializando un diccionario vacío
para posteriormente agregar cada par llave-valor:

```python
estudiantes = dict()  #  crea diccionario vacío

# agrega llave '0124' con un valor ['Mario', 9]
estudiantes['0124'] = ['Mario', 9]
                                    #
# agrega llave '3276' con un valor ['Rosa', 10]
estudiantes['3276'] = ['Rosa', 10]

print(estudiantes)  #  {'0124':['Mario', 9], '3276':['Rosa', 10]}
```

Y también podemos crearlos mediante un iterable que contenga pares llave-valor:

```python
my_dict = dict([('a',5), ('d',1)])
print(my_dict)  #  {'a': 5, 'd': 1}
```

Para crear diccionarios vacíos tenemos también la opción

```python
my_dict = {}
print(type(my_dict))  #  dict
```

Estas estructuras se emplean para almacenar grandes cantidades de datos de manera eficiente;
python las implementa
mediante una técnica conocida como *hashing*,
permitiéndonos buscar elementos por medio de la llave de manera muy eficiente.
Para acceder a los valores empleamos la llave correspondiente.

```python
print(vuelo['code'])  #  'BKJ123'
print(estudiantes['3276'])  # ['Rosa', 10]
```

Observa que **los diccionarios no tiene índices**,
accedemos a los valores mediante llaves,
por lo tanto no importa en que orden almacenemos la información.
Y ya que estamos en esto,
**tampoco soportan el rebanado** (*slicing*).

> [!NOTE]
>
> Un mapeo llave-valor podría implementarse mediante una lista de tuplas como `[('a',5), ('b':1)]`,
> sin embargo,
> esto sería muy ineficiente para listas grandes;
> para buscar cualquier llave tendríamos que explorar elemento a elemento de la lista,
> y en caso de no encontrarse el objeto
> tendríamos que haber recorrido la lista entera
> (algoritmo de orden N).

> [!NOTE]
>
> Las llaves son *hashable*,
> lo cual implica que deben ser de tipo inmutable;
> las llaves no pueden ser listas, otros diccionarios o conjuntos
> ya que obtendríamos un `TypeError`.

#### Operaciones

Ya hemos visto como buscar y añadir elementos.
Ahora vemos como modificar y eliminar entradas.

Para modificar valores utilizamos el mismo formato que
para acceder (corchetes con la llave).
Si tenemos el siguiente inventario de frutas a vender

```python
# este formato se conoce como indentación colgada
inventario = {
    'manzana': 120,  # podemos agregar comentario
    'plátano': 400,  # en las líneas que queramos
    'mango': 220,    # PEP8 recomienda esta coma
}
```

cambiamos la cantidad de plátanos mediante

```python
inventario['plátano'] = 370
print(inventario)  #  {'manzana': 120, 'plátano': 370, 'mango': 220}
```

Si nos llegaron 100 plátanos más,
podemos agregarlos con

```python
inventario['plátano'] += 100
print(inventario)  #  {'manzana': 120, 'plátano': 470, 'mango': 220}
```

Por otro lado,
si no venderemos más manzanas
eliminamos el elemento

```python
del inventario['manzana']
print(inventario)  #  {'plátano': 470, 'mango': 220}
```

Si intentamos acceder a un elemento cuya llave no existe,
obtenemos un `KeyError`

```python
res = inventario['manzana']
```

Podemos también checar si una llave existe en el diccionario
mediante `in` o que no existe con `not in`.
Por ejemplo,

```python
print('plátano' in inventario)  #  True
print('pera' not in inventario)  #  True
```

Esto lo podemos emplear para evitar
el error que ocurre con llaves inexistentes

```python
def tenemos(fruta:str, database:dict) -> bool:
    if fruta in database:
        return f'Si hay {fruta}'
    else:
        return f'No hay {fruta}'

print(tenemos('mango', inventario))
print(tenemos('pera', inventario))
```

Podemos saber el número de elementos mediante `len`

```python
print(len(inventario))  #  2
```

y podemos iterar por el diccionario;
la iteración utiliza el valor de las llaves

```python
# es recomendable utilizar nombres con significado apropiado
for fruta in inventario:
    print(fruta)

# imprime:
# plátano
# mango
```

Las colecciones,
por definición
(ver nota en *Colecciones*),
soportan la iteración,
la función `len`
y la palabra reservada `in`.

#### Métodos

Los diccionarios, siendo colecciones mutables,
tienen métodos tanto para obtener sus elementos como para modificarlos.
Aquí exploramos los principales.

> [!NOTE]
>
> Siempre puedes descubrir los métodos disponibles
> mediante `dir(dict)`
> (para listas `dir(list)`, tuplas `dir(tuple)`)
> y si deseas ayuda para un método,
> digamos `update`,
> puedes llamar `help(dict.update)`.
>
> Si estas en ipython `dir.` seguido de la tecla `TAB`
> nos indica los métodos y
> `dict.update?` o `dict.update??`
> nos da información sobre el método `update`
> (con `?` se da el docstring,
> con `??` trata de darnos también la implementación)

Para obtener la información de las llaves y valores en un diccionario
contamos con `keys`, `values` y `items`.
Cada uno de estos métodos regresa un objeto
que se conoce en python como una vista;
objetos que funcionan como una promesa de regresar su valor cuando sea requerido en lo que resta del programa,
es decir,
tienen evaluación perezosa (*lazy*).
Por cierto,
las vistas que regresan estos tres métodos son iterables.

Por su parte `keys` regresa una vista de las llaves:

```python
spanish = {'Hi': 'Hola', 'Bye': 'Adios', 'world': 'mundo'}
llaves = spanish.keys()
print(llaves)  #  dict_keys(['Hi', 'Bye', 'world'])
```

Una vista se puede transformar en una lista mediante `list`
(o una tupla con `tuple`)

```python
llaves_lista = list(llaves)
```

O podemos iterar por cada uno de sus valores

```python
for key in llaves:
    print(f'llave: {key}')
    print(f'valor: {spanish[key]}')
    print()
```

Aunque iterar por las llaves es lo que ocurre por default
al utilizar `for` con un diccionario y no sería útil llamar este método para dicha tarea.

Luego tenemos a `values`
el cual regresa una vista de los valores de cada llave:

```python
print(spanish.values())  #  dict_values(['Hola', 'Adios', 'mundo'])
```

Finalmente tenemos a `items`,
el cual regresa una vista que promete tuplas;
una tupla por cada par llave-valor
(dos elementos).

```python
elems = list(spanish.items())
print(elems)  # [('Hi', 'Hola'), ('Bye', 'Adios'), ('world', 'mundo')]

for item in spanish.items():
    print(item)

# imprime:
# ('Hi', 'Hola')
# ('Bye', 'Adios')
# ('world', 'mundo')
```

Desde luego podemos utilizar desempaquetado para acceder a estos valores inmediatamente:

```python
for llave, valor in spanish.items():
    print(llave)
    print(valor)
    print()
```

Otro método muy útil es `get`,
al cual le damos una llave y nos regresa el valor correspondiente.
Si la llave no se encuentra este regresa `None` por default en vez de un error.

```python
print(spanish.get('world'))  #  mundo
print(spanish.get('one') is None)  #  True
```

Por otro lado,
podemos agregar un argumento más indicando que valor deseamos
que regrese la función en caso de no encontrar una llave:

```python
print(spanish.get('Hi', 'my bad'))  # Hola
print(spanish.get('one', 'my bad'))  # my bad
```

Esta función resulta muy útil al procesar texto y contar la ocurrencia de palabras en un diccionario.
Por ejemplo,

```python
texto = 'al pan pan y al vino vino'
my_dict = {}
for word in texto.split():
    my_dict[word] = my_dict.get(word, 0) + 1
print(my_dict)
```

Al definir un diccionario mencionamos que es mutable.
En tales casos debemos tener cuidado con los alias;
otras variables que hacen referencia al mismo objeto
y que al modificarse alteran el contenido de la variable original.
Para crear una copia superficial de un diccionario contamos con `copy`

```python
frecuencias = {'carro': 3, 'alto': 5}

frec_alias = frecuencias
frec_copy = frecuencias.copy()

# modificar alias y copia
frec_alias['bajo'] = 1
frec_copy['estrella'] = 4

# alterar el alias afecta al mutable original
print(frecuencias)  #  {'carro': 3, 'alto': 5, 'bajo': 1}
# pero siempre podemos trabajar con una copia
print(frec_copy)  #  {'carro': 3, 'alto': 5, 'estrella': 4}
```

Si requerimos una copia profunda de una colección podemos hacer uso del módulo `copy`,
el cual contiene la función `deepcopy` para este fin

```python
import copy


my_dict = {'a': 5, 'b': 'Hi', 'c':[-3, 7]}

# una copia superficial no crea nuevos objetos para los elementos
# de tal manera que modificar un valor mutable de la copia
# también afectará al diccionario original
dict_copy = my_dict.copy()
dict_copy['c'][0] = 5
print(my_dict)  #  {'a': 5, 'b': 'Hi', 'c':[5, 7]}

# con `deepcopy` tenemos realmente dos diccionarios independientes
dict_deep = copy.deepcopy(my_dict)
dict_deep['c'][0] = 10
print(dict_deep)  #  {'a': 5, 'b': 'Hi', 'c':[10, 7]}
print(my_dict)  #  {'a': 5, 'b': 'Hi', 'c':[5, 7]}
```

Otro método útil es `update`,
el cual te permite agregar el contenido de otro diccionario.
Si el diccionario a agregar repite una llave del original,
su valor reemplazará al antiguo.
Por ejemplo,

```python
inventario = {'pera': 25, 'melon': 33}
inventario.update({'manzana':20, 'pera':18})
print(inventario)  #  {'pera': 18, 'melon': 33, 'manzana':20}
```

Este método también funciona con iterables;
cada elemento del iterable debe contener dos objetos,
uno para la llave y el otro el valor:

```python
my_list = [('compilador', 'gcc'), ('dir_lib', './lib')]
# inicialización
conf = {}
# agregar contenido de iterable
conf.update(my_list)
print(conf)  #  {'compilador': 'gcc', 'dir_lib': './lib'}
```

#### Comprensiones de diccionario (*dictionary comprehension*)

Podemos emplear `for` implícitos para la creación de diccionarios.
Por ejemplo,
a partir de un iterable como `range`

```python
square = {x: x**2 for x in range(1, 6)}
print(square)  #  {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
print(square[4])  #  16
```

o bien, a partir de otro diccionario

```python
# costo antes del iva
precio = {'camisa': 750.0, 'pantalon': 1200.0}
# costo final
iva = 1.16
precio_total = {key: val * iva for key, val in precio.items()}
print(precio_total)  #  {'camisa': 870.0, 'pantalon': 1392.0}
```

Un uso típico es tener iterables separados para las llaves y los valores los cuales deseamos unir.
Para lograr esto requerimos del objeto iterable `zip`.

Para crear este objeto empleamos la función `zip`
seguida de `n` argumentos.
Cada elemento será una tupla con `n` objetos.
La primer tupla toma el primer elemento de cada argumento,
la segunda tupla tiene los segundos elementos de cada argumento
y así sucesivamente.
Los elementos terminan cuando a alguno de los argumentos dados a `zip` se le acaban sus elementos.

```python
a = ['a', 'b', 'c', 'd']
b = (2, 4, 6)
my_zip = zip(a, b)
for elem in my_zip:
    print(elem)

# imprime:
# ('a', 2)
# ('b', 4)
# ('c', 6)
```

Una vez llamados sus elementos no podemos volver a utilizarlos;
el siguiente código

```python
count = 0
for elem in my_zip:
    count += 1
    print(count)
    print(elem)
```

no imprime nada.

Podemos transformar el objeto `zip` en una lista si lo deseamos

```python
x = (2.0, 2.5, 3.0, 3.5)
y = (1.0, 1.5, 2.0, 2.5)

z = map(lambda a, b: a**2 + b**2, x, y)
z = tuple(z)  #  (5.0, 8.5, 13.0, 18.5)

coor_zip = zip(x, y, z)
coor_lista = list(coor_zip)
print(coor)

# imprime:
#  [(2.0, 1.0, 5.0),
#   (2.5, 1.5, 8.5),
#   (3.0, 2.0, 13.0),
#   (3.5, 2.5, 18.5)]
```

Observa que al transformarlo en una lista hemos agotado la extracción de sus elementos
y ya no podemos iterar sobre el objeto `zip`:

```python
# no imprimirá nada
for elem in coor_zip:
    print(elem)
```

Regresando a nuestro problema original;
para unir dos iterables,
digamos nombres y edades,
podemos ejecutar

```python
nombres = ['Aang', 'Katara', 'Sokka']
edades = (112, 14, 15)

edad = {key: val for key, val in zip(nombres, edades)}
print(edad)  #  {'Aang': 112, 'Katara': 14, 'Sokka': 15}
```

### Conjuntos

Los conjuntos de tipo `set`
son colecciones mutables que no permiten la repetición de elementos.
Estos se crean directamente mediante llaves
(sin el separador `:` que se utiliza en mapeos)
o con el constructor `set`
al cual le damos un iterable:

```python
# utilizando llaves directamente
pelis = {'Matrix', 'El Padrino'}
print(type(pelis))  #  <class 'set'>

# no se agregan elementos repetidos
conjunto = {'a', 'a'}  #  no agrega elementos repetidos
print(conjunto)  #  {'a'}

# con `set` y un iterable
series = set(['Breaking Bad', 'Juego de Tronos'])
print(series)  #  {'Breaking Bad', 'Juego de Tronos'}
```

Para crear un conjunto vacío debemos emplear

```python
conjunto_vacio = set()
```

ya que introducir `a = {}` crea un diccionario vacío `a`,
no un conjunto.

Los elementos deben ser *hashable*,
lo cual fuerza a que sean de tipo inmutable
(números, strings, bool, tuplas);
esto debido a que internamente se almacenan en una tabla de *hash*.
Por ejemplo,

```python
# correcto
my_set = {1, 'hola', (2, 3)}
type(my_set)  #  set

# incorrecto
other_set = {1, 'hola', [2, 3]} # TypeError: unhashable type: 'list'
```

Además, sus elementos no siguen el orden en que fueron ingresados;
el almacenamiento es de acuerdo al valor de hash de cada elemento,
como podemos apreciar con el conjunto `my_set`

```python
print(my_set)  #  {(2, 3), 1, 'hola'}
```

Estos objetos soportan métodos para añadir y eliminar elementos,
pero no permiten modificar aquellos ya ingresados
ni utilizar la indexación o rebanado
(no tendría sentido ya que desconocemos el orden).

```python
# no soporta índices
my_set[0]  #  TypeError: 'set' object is not subscriptable
```

Para añadir o eliminar un elemento a la vez utilizamos
`add` o `remove`,
respectivamente:

```python
simpsons = set()
simpsons.add('Homero')
simpsons.add('Bart')
simpsons.add('Luigi')  # Ups me equivoqué
print(simpsons)  #  {'Luigi', 'Bart', 'Homero'}

simpsons.remove('Luigi')
print(simpsons)  #  {'Bart', 'Homero'}
```

donde el método `remove` regresa un `KeyError`
si el elemento a eliminar no se encuentra.
Si no deseamos este comportamiento tenemos a `discard`
el cual elimina un elemento y no hace nada si este no se encuentra

```python
simpsons.discard('Mario')  #  no pasa nada
simpsons.remove('Mario')  #  KeyError: 'Mario'
```

Para agregar múltiples elementos contamos con `update`;
este recibe un iterable con objetos *hashable*

```python
simpsons.update(('Lisa', 'Marge'))
print(simpsons)  #  {'Marge', 'Lisa', 'Bart', 'Homero'}

# no es lo mismo agregar una tupla que un string
my_set = set()
my_set.update('Lisa')
print(my_set)  #  {'s', 'a', 'L', 'i'}
```

Dado que los conjuntos son **colecciones**,
estos permiten checar si un elemento existe o no
mediante `in` y `not in`,
respectivamente,
soportan la iteración
y tienen un tamaño dado por `len`:

```python
conjunto = {'uva', 'mango', 'melon'}

print('fresa' in conjunto)  #  False
print(len(conjunto))  #  3

# al iterar recuerda que los elementos están desordenados
for fruta in conjunto:
    print(fruta)
# imprime:
# uva
# melon
# mango
```

> [!NOTE]
>
> Aquí es importante detenernos a hacer una mención importante:
> debido a la implementación mediante la tabla de *hash*,
> checar si un elemento existe (`in`) en un conjunto
> es muchísimo más rápido que para una lista
> (tiempo con orden $O(1)$ contra $O(n)$ en una lista).
> También tenemos que el insertar y eliminar elementos
> es más veloz ya que las listas requieren mover los elementos
> al insertar o eliminar un objeto de el medio.
> La iteración por otro lado es más veloz en las listas.

Existe un segundo tipo de conjunto,
**el conjunto congelado** `frozenset`.
Este es la **versión inmutable de un** `set`.
Además este objeto es *hashable*,
es decir,
puede usarse como elemento en los conjuntos.

Su creación requiere del constructor `frozenset`
al cual le pasamos un iterable:

```python
U = frozenset('Hola')
print(U)  #  frozenset({'o', 'H', 'l', 'a'})
```

Al igual que un `set` sus elementos están desordenados
y es una colección; soporta `in`, iteración y `len`.

Siendo inmutable no soporta:
`add`,
`update`,
`remove` y
`discard`.

En este objeto no se soporta agregar ni eliminar elementos

#### Operaciones de conjunto

Al estar inspirados en los conjuntos matemáticos,
tanto `set` como `frozenset` permiten las operaciones:
unión,
intersección,
diferencia,
diferencia simétrica,
verificar subconjuntos,
etc.

Para la **unión** tenemos el método `union`
y el operador `|`,
los cuales regresan un nuevo conjunto que resulte
de la unión de dos o más conjuntos:

```python
a = {1, 2, 'a', 'b', 'c'}
b = {'a', 'b', 'f'}

c = a.union(b)
print(c)  #  {1, 2, 'a', 'c', 'f', 'b'}
# equivalentemente pudimos ejecutar (teniendo el mismo resultado)
# c = a | b
```

La **intersección** se obtiene con el método `intersection`
o el operador `&`:

```python
c = a & b
print(c)  #  {'a', 'b'}
# equivalentemente
# c = a.intersection(b)
```

Para verificar si un conjunto es **subconjunto** de otro tenemos
al métodos `issubset` y el operador `<=`

```python
a = {2, 4, 6}
b = {2, 4, 6, 8}
c = {2, 4, 6}

print(b.issubset(a))  #  False
print(a.issubset(b))  #  True
print(a.issubset(c))  #  True
```

En teoría de conjuntos existe otro concepto conocido como
**subconjunto propio**:
un conjunto `U` es subconjunto propio de `V`
sí y solo sí `U` es subconjunto de `V` y
`U` es distinto a `V`.
Para verificar esto contamos con el operador `<`:

```python
print(a < b)  #  True
print(a < c)  #  False
```

En el caso opuesto,
podemos verificar si un conjunto es **superconjunto** de otro con
`issuperset` o `>=`
(superconjunto propio con `>`).


También podemos verificar si dos conjuntos son **disjuntos** mediante
`isdisjoint`

```python
U = {'a', 'g'}; V = {'b', 'c', 1}
print(U.isdisjoint(V))  #  True

# dos conjuntos son disjuntos si no se intersectan,
# por lo tanto, también podríamos verificar con
W = U.intersection(V)
# cuyo resultado debería ser el conjunto vacío
print(W)  #  set()
```

Otras operaciones importantes son la **diferencia**
y la **diferencia simétrica**.

Para la diferencia podemos emplear `difference`
o el operador `-`;
`U - V` regresa el conjunto con los elementos de `U` que no están en `V`.

Para la segunda operación tenemos el método `symmetric_difference`;
`U.symmetric_difference(A)`
regresa los elementos únicos en ambos conjuntos.

```python
U, V = set('carbon'), set('arbol')
print(V)  #  {'a', 'b', 'o', 'r', 'l'}

print(U - V)  #  {'n', 'c'}
print(V - U)  #  {'l'}

W = U.symmetric_difference(V)
print(W)  #  {'n', 'l', 'c'}   la diferencia simétrica es igual a
          #                    (U-V) | (V-U)
```

Los conjuntos tienen muchas operaciones disponibles.
Para ver una lista completa visita
[aquí](https://docs.python.org/3.13/library/stdtypes.html#set-types-set-frozenset)


## Generadores

Los generadores son objetos iterables que tienen una evaluación perezosa.
No almacenan todos los valores del iterable en la memoria
sino que regresan valor a valor en un bucle `for`
o mediante la función `next`.
Estos nos permiten procesar cantidades grandes de información,
trabajar con secuencias infinitas
o procesar un flujo continuo de datos.

Para crear un generador utilizamos la sintaxis de una función
pero en vez de utilizar `return` empleamos `yield`.
En una función,
`return` termina la ejecución,
en cambio el generador utiliza `yield` para generar un valor y pausar,
guardando el estado de la función para que esta pueda
resumir donde nos quedamos cuando se pida el siguiente valor.
Si pedimos un valor después de haber consumido todos,
se obtiene la excepción `StopIteration`.

A continuación creamos un generador

```python
def mi_gen(x):
    x += 2
    yield x**2
    if x%2 == 0:
        print('es par')
        yield x//2
```

Hay que hacer hincapié que dicho objeto no es una función,
es un generador.
Para ver esto creamos dos instancias
(dos entidades específicas e individuales de su clase)
mediante:

```python
inst_1 = mi_gen(5)
inst_2 = mi_gen(8)
```

Si `mi_gen` fuera una función se habría corrido el código del cuerpo.
En cambio,
lo que hemos hecho es crear dos generadores independientes
los cuales no han ejecutado el código.
Si aplicamos la función `next` sobre el primer generador

```python
print(next(inst_1))  #  49
```

se ejecuta el código del cuerpo hasta llegar al primer `yield`
y ahí se detiene a esperar que solicitemos un nuevo valor,
almacenando el estado actual de la función
(variables locales hasta ese punto: `x=7`).

Si vuelvo a solicitar un valor

```python
print(next(inst_1))  #  StopIteration
```

obtengo un error ya que no hay más valores que regresar
(`x=7` no es un número par y no se entra en el `if`).

Si ahora ejecutamos el segundo generador

```python
print(next(inst_2))  #  100
```

Este almacena su propio estado independiente (`x=10`) y
puede resumir donde se quedó

```python
val = next(inst_2)  #  se imprime: es par
print(val)  #  5
```

> [!NOTE]
> Debemos considerar que una vez evaluado un valor no podemos regresar al anterior.

Podemos obtener una secuencia de enteros ´donde el
i-ésimo elemento sea la suma de $1$ a $i$ mediante

```python
def sumatoria(n:int):
    """
    n > 0

    """
    suma = 0
    for i in range(1, n+1):
        suma += i
        yield suma
```

En esta ocasión recorreremos los valores del generador,
el cual es un iterador,
en un bucle `for`:

```python
for num in sumatoria(10):
    print(num)
# imprime
# 1
# 3  (1+2)
# 6  (1+2+3)
# 10  (1+2+3+4)
# ...
# 55 (1+2+3+...+10)
```

¿Cómo modificarías el generador `sumatoria` para tratar de obtener la secuencia hasta el infinito?

Aquí creamos un generador que retorna la secuencia de *Fibonacci*
(la cual toma valores $(0, 1, 1, 2, 3, 5, 8, ...)$ ya que cada valor se obtiene de sumar los dos anteriores)

```python
def fibonacci():
    a = 0
    b = 1
    while True:
        yield a
        a, b = b, a + b
```

Para obtener todos los número Fibonacci ejecutamos
(esta serie es infinita,
para detener el programa presiona las teclas Ctrl+C):

```python
import time


# creamos el objeto
mi_fibo = fibonacci()
# ahora lo ejecutamos
while True:
    print(next(mi_fibo))
    time.sleep(0.5)  # dormimos medio segundo para ver resultados
```

Una manera concisa de crear generadores es utilizar paréntesis y
comprensión `for` como para las listas:

```python
gen = (x**2 for x in range(5))
print(type(gen))  #  <class 'generator'>
```

Podemos iterar sobre el generador o bien transformarlo en una lista
lo cual hará que se ejecute hasta obtener su último valor:

```python
cuadrados = list(gen)
print(cuadrados)  #  [0, 1, 4, 9, 16]
```


</div>
