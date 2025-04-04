###
# 01 - Sentencias condicionales (if , elif, else)
# Permiten ejecutar bloques de codigo solo si se cumplen ciertas condiciones
###

import os 
os.system("clear")

print("\nSentencia simple condicional")

edad = 18

if edad >= 18:
    print("Eres mayor de edad")
    print("Felicidades!")

edad = 15

if edad >= 18:
    print("Eres mayor de edad")
    print("Felicidades!")

print("\nSentencia condicional con else")
edad = 15
if edad >= 18:
    print(f"Eres mayor de edad")
else:
    print(f"Eres menor de edad")

print("\nSentencia condicional con elif")

nota = 7

if nota >= 9:
    print("Sobresaliente!")
elif nota >=7:
    print("Notable")
elif nota >= 5:
    print("Aprobado!")
else:
    print("No estas calificado")

print("\nCondiciones múltiples")
edad = 25
tiene_carnet = False

if edad >= 18 and tiene_carnet:
    print("Puedes conducir 🚗")
else:
    print("Policia!! 🚓🚓")


if edad >= 18 or tiene_carnet:
    print("Puedes conducir en la Isla Margarita 🚗")
else:
    print("Paga al policia y te deja conducir!! 💰👮‍♂️")

es_fin_de_semana = False

if not es_fin_de_semana:
    print("de peter")

print("\nAnidar condicionales")
edad = 20
tiene_dinero = True

if edad >= 18:
    if tiene_dinero:
        print("Puedes ir a la discoteca")
    else:
        print("Quédate en casa")
else:
    print("No puedes entrar a la disco")

# Mas legible:
# if edad < 18:
#     print("No puedes entrar a la disco")
# elif tiene_dinero:
#     print("Puedes ir a la discoteca")
# else:
#     print("Quédate en casa")
