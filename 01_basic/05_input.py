###
# 05 - Entrada de usuario (input()) - version simplificada
# La funcion input(), permite obtener datos del usuario a traves de la consola
###

nombre = input("Hola, como te llamas?\n")
print(f"Hola {nombre}, encantado de conocerte")

age = input("Cuantos años tienes?\n")
age = int(age)
print(f"Dentro de 20 años, tendrás {age + 20} años")

print("Obtener multiples valores a la vez")
country, city = input("En que pais y ciudad vives?\n").split()

print(f"Vives en {country}, {city}")