
"""
🧠 NIVEL 1 – VARIABLES (CALENTAMIENTO)
🟢 Ejercicio 1

Crea variables con:

tu edad

tu altura

tu nombre

Luego imprime una frase así:

Hola, me llamo ___, tengo ___ años y mido ___ metros

📌 Pista:

print("texto", variable)

🟢 Ejercicio 2

Crea dos variables:

a = 10

b = 3

Imprime:

suma

resta

multiplicación

división

🧠 NIVEL 2 – INPUT (YA COMO PROGRAMADOR)
🟡 Ejercicio 3

Pídele al usuario:

su nombre

su edad

Imprime:

Nombre registrado: ___
Edad el próximo año: ___

📌 Pista:

edad = int(edad)

🟡 Ejercicio 4

Pídele al usuario dos números y muestra:

suma

multiplicación

⚠️ Ojo: input() siempre llega como texto.

🧠 NIVEL 3 – LÓGICA SIMPLE (YA SE VE SERIO 😎)
🔵 Ejercicio 5

Pide la edad al usuario y muestra:

True si es mayor o igual a 18

False si no

📌 Pista:

print(edad >= 18)

🔵 Ejercicio 6

Crea una variable numero
Imprime:

su tipo con type()

y el número multiplicado por 2

🧠 NIVEL 4 – RETO (ESTE ME GUSTA 👀🔥)
🔴 Ejercicio 7

Pide:

nombre

año de nacimiento

Calcula e imprime:

Hola ___, en 2026 tendrás ___ años

📌 Pista:

edad = 2026 - nacimiento"""

#punto 1

edad= 16
nombre= "Alejandro"
altura= 1.83
print("hola, mi nombre es", nombre, "mi edad es", edad, "y mi altura es", altura)



#punto 2
a = 10
b = 3

print(a+b)
print(a-b)
print(a*b)
print(a/b)



#punto 3

nombre = input("ingrese su nombre= ")
edad = int(input("ingrese su edad= "))
print("nombre registrado=", nombre)
print("esta es tu edad el proximo año= ", edad+1)



#punto 4

n1, n2 = int(input("ingrese n1= ")), int(input("ingrese n2= "))
print(n1+n2)
print(n1*n2)


#punto 5
edad = int(input("ingrese su edad= "))
print(edad>=18) 



#punto 6

num = int(input("ingrese numero= "))
print(type(num))
print(num * 2)


#punto 7

nombre, naci = input("escribe tu nombre "), int(input("y tu año de nacimiento= "))
print("hola", nombre, "en 2026 tendras", 2026-naci)

















