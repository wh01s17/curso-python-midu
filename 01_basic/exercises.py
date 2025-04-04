###
# exercises.py
# Ejercicios para practicar los conceptos aprendidos en las lecciones.
###

from os import system
if system("clear") != 0: system("cls")

print("\nEjercicio 1: Imprimir mensajes")
print("Escribe un programa que imprima tu nombre y tu ciudad en líneas separadas.")

### Completa aquí
name="Jordy"
city="Cartagena"

print(name)
print(city)

print("--------------")

print("\nEjercicio 2: Muestra los tipos de datos de las siguientes variables:")
print("Usa el comando 'type()' para determinar el tipo de datos de cada variable.")
a = 15
b = 3.14159
c = "Hola mundo"
d = True
e = None

### Completa aquí
print("Tipo de a: ", type(a))
print("Tipo de b: ", type(b))
print("Tipo de c: ", type(c))
print("Tipo de d: ", type(d))
print("Tipo de e: ", type(e))

print("--------------")

print("\nEjercicio 3: Casting de tipos")
print("Convierte la cadena \"12345\" a un entero y luego a un float.")
print("Convierte el float 3.99 a un entero. ¿Qué ocurre?")

### Completa aquí
cadena= "12345"
entero = int(cadena)
decimal = float(entero)
print("Numero entero: ", entero)
print("Numero flotante: ", decimal)

flotante = 3.99
flotante_a_entero = int(flotante)
print("Numero flotante original: ", flotante)
print("Numero convertido a entero: ", flotante_a_entero)

print("--------------")

print("\nEjercicio 4: Variables")
print("Crea variables para tu nombre, edad y altura.")
print("Usa f-strings para imprimir una presentación.")

# "Hola! Me llamo midudev y tengo 39 años, mido 1.70 metros"

### Completa aquí
# nombre = input("Ingresa tu nombre: ")
# edad = int(input("Ingresa tu edad: "))
# estatura = float(input("Ingresa tu estatura: "))
nombre = "Jordy"
edad = 31
estatura = 1.68
print(f"Hola! Me llamo {nombre} y tengo {edad} años, mido {estatura} metros")

print("--------------")

print("\nEjercicio 5: Números")
print("1. Crea una variable con el número PI (sin asignar una variable)")
print("2. Redondea el número con round()")
print("3. Haz la división entera entre el número que te salió y el número 2")
print("4. El resultado debería ser 1")

print("1 - Valor aprox de PI: ", 3.1416)
print("2 - Valor redondeado de PI: ", round(3.1416))
print("3 - Resultado: ", int(round(3.1416) / 2))

