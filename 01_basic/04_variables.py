###
# 04 - Variables
# Python es un lenguaje de tipado dinamico y de tipado fuerte
###

my_name = "jordy"

# print(myname)

age = 31
# print(age)

# age = 39
# print(age)

# tipado dinamico: el tipo de dato se determina en tiempo de ejecucion
# no tienes que declararlo explicitamente
name = "Jordy"
# print(type(name))

name = 32
# print(type(name))

# tipado fuerte: Python no realiza conversiones de tipo automatico
# print(10 + "2")

# f-string (literal de cadena de formato)
print(f"Hola {my_name}, tengo {age + 5} años")

# forma no recomendada de asignar variables
name, age, city = "jordy", 32, "Bogota"

# convenciones de nombres de variables
mi_nombre_de_variable = "ok" # snake_case
nombre = "ok"

MiNombreDeVariable = "no" # PascalCase
minombredevariable = "no" # todo junto

mi_nombre_de_variable_123 = "ok"

MI_CONSTANTE = 3.14 # UPPER_CASE -> constantes

# nombres no validos de variables
# 1234_variable = "no"
# mi-variable = "no"
# mi variable = "no"

# el parametro :bool, es solo una anotacion, y no define el tipo de la variable
is_user_logged_in: bool = True
print(is_user_logged_in)

# is_user_logged_in = 42
# print(is_user_logged_in)



