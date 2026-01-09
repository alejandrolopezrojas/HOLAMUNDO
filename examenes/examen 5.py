"""
RETO EXTREMO – EL JUEZ LÓGICO

RESTRICCIONES:
- No usar if / else
- No usar for / while
- No usar listas, funciones ni imports

SOLO SE PERMITE:
input, print
variables
int, str, bool
operadores aritméticos
operadores comparativos
operadores lógicos
len
acceso a caracteres (texto[0])

EL PROGRAMA DEBE PEDIR:
1. Nombre
2. Apellido
3. Año de nacimiento
4. Palabra secreta
5. Número favorito (entero)

OBJETIVO:
El programa debe imprimir UN SOLO valor booleano (True o False).

El resultado será True SOLO SI TODAS estas condiciones se cumplen:

1. El nombre tiene más de 3 caracteres
2. El apellido tiene longitud impar
3. La edad en 2026 es mayor o igual a 18
4. La palabra secreta tiene longitud par
5. El nombre y la palabra secreta no son iguales
6. La primera letra del nombre es menor (ASCII) que la primera letra del apellido
7. La última letra del apellido es mayor (ASCII) que la última letra de la palabra secreta
8. El número favorito es mayor que 10 y menor o igual a 100
9. La suma de la longitud del nombre y del apellido es mayor que
   el número favorito dividido entre 2
10. El valor booleano de la palabra secreta es True

CONDICIONES FINALES:
- Todo debe resolverse en una sola expresión lógica final
- El print final solo imprime True o False
- El código debe estar comentado y sin errores
"""

nombre = input("nombre= ")
apellido = input("apellido= ")
naci = int(input("nacimiento= "))
sec = input("palabra secreta= ")
num = int(input("numero= "))

print(len(nombre) > 3 and (len(apellido)%2) != 0 and (2026 - naci) >= 18 and (len(sec)%2) == 0 and nombre != sec and nombre[0] < apellido[0] and apellido[-1] > sec[-1] and (num > 10 and num <= 100) and (len(nombre) + len(apellido)) > (num/2) and bool(sec) == True)




























