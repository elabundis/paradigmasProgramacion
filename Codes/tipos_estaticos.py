# ATRAPANDO ERRORES CON TIPOS ESTÁTICOS

age: int = 25
age = 18.0

height: float
height = 2.0
height = '2.0'

# -------------------------------------------------
# Corriendo funciones

# Tipo estático
def presentacion(edad: int, nombre: str) -> str:
    return nombre + " tiene " + str(edad) + "años."

# Tipo dinámico
def es_adulto(edad: int) -> bool:
    if(edad >= 18):
        return True
    else:
        return False

presentacion( 'Maria', 19 )
es_adulto('19')
es_adulto(20)

# -------------------------------------------------
# Sin correr las funciones
def saludo(nombre:str) -> str:
    return ["Hola " + nombre]

def son_adultos(edades: list[int]) -> bool:
    '''Verifica que todos sean adultos'''
    if(edades >= 18):
        return True
    else:
        return False

# saludo('Rosa')
# grupo1_1 = [18, 19, 18, 17]
# son_adultos(grupo1_1)
# -------------------------------------------------
