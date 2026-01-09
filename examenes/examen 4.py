"""
RETO PYTHON – NIVEL FINAL

Reglas:
No se permite el uso de if, else, for, while, listas, funciones ni imports.
Solo se pueden usar: input, print, variables, int, str, bool,
operadores aritméticos, comparativos, lógicos y len.
El programa debe ejecutarse sin errores.

Reto: Validador humano

Punto único:
El programa debe solicitar al usuario:
- Nombre
- Edad
- Una palabra clave

El programa debe imprimir UN SOLO valor booleano (True o False).

El resultado será True únicamente si todas las siguientes condiciones
se cumplen al mismo tiempo:

1. El nombre tiene más de 3 caracteres.
2. La edad es mayor o igual a 16.
3. La palabra clave tiene una longitud par.
4. El nombre y la palabra clave no son iguales.
5. La primera letra del nombre es menor, según orden ASCII,
   que la primera letra de la palabra clave.

Todas las condiciones deben evaluarse en una sola expresión lógica,
sin utilizar if.

Notas:
- Usar len() para tamaños.
- Usar el operador % para verificar si una longitud es par.
- Se puede acceder a un carácter de un string usando indice [0].
- El código debe estar comentado y ser claro.
"""

nombre = input("ingrese su nombre= ")
edad = int(input("ingrese su edad= "))
clave = input("ingrese palabra clave= ")

print(len(nombre) > 3 and edad >= 16 and len(clave)%2 == 0 and nombre != clave and nombre[0] < clave[0])





