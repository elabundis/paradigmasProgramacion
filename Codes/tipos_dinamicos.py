# 'variable' tiene un tipo 'int'
# El entero se almacena en memoria y la 'variable' luego apunta a su direccion
variable = 5
print(f"valor: {variable}, tipo:{type(variable)}")

# 'variable' ahora tiene tipo 'str' y esto no genera un error
# El string se almacena en una nueva direccion y 'variable' apunta a esta
variable = "Jesus"
print(f"valor: {variable}, tipo:{type(variable)}")

# 'variable' ahora tiene tipo 'float'
variable = 3.14
print(f"valor: {variable}, tipo:{type(variable)}")
