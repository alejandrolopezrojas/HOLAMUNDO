"""los operadores hacen operaciones
 matematicas, estos son algunos basicos"""

#estos son los aritmeticos

print(10+3) #SUMA
print(10-3) #RESTA
print(10*3) #MULTIPLICACIÓN
print(10/3) #DIVISIÓN

#ahora algunos mas avanzados

print(10**3) #EXPONENTE
print(10%3) #TE DICE CUENTO SOBRA DESPUES DE LA DIVISIÓN
print(10//3) #FLOORDIVICIÓN SIEMPRE APROXIMA A UN ENTERO

#claro que tambien funcionan todos dentro de una misma operación
print(214+466-86*563/1//21**122%35465)

#si queremos que la operación tenga un orden agregamos parentesis
print(5+5/2)
print((5+5)/2)


#con datos str solo podemos sumarlos
print("hola python" + "¿como estas?")
#si queremos sumar con un numero tiene que ser un str o pasarlo=
print("este es el numero " + str(5))
#tambien podemos multiplicarlos incluso por operaciones
print("hola mundo " * 3)
print("IA " * (int(12+4**3/15))) #tiene que ser int


