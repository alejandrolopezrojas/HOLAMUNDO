    #algunos ejemplos de funciones de strings

print("este es un string con \nsalto de linea")#no dejar espacio 

print("\teste es un string con tabulación")

print("\\teste es un string \\n escapado")#para poder escribir las funciones

    #FORMATEO=

a, b, c, d = "alejandro", "lopez", 16, 121.23131421134
print(f"mi nombre es {a} y mi apellido es {b} y tengo {c} años \ny este es un decimal {d}")
#no necesita cambiar el type}

    #DESEMPAQUETADO DE STRINGS=
pal = "univerSidad"
a,b,c,d,e,f,g,h,i,j,k = pal
print(k)
print(j)
print(i)#nos permite asignar cada letra a una variable
print(h)
print(g)
print(f)
print(e)
print(d)
print(c)
print(b)
print(a)

    #división=

print(pal[0:4])#los caracteres que escojamos sin contar el ultimo
print(pal[4:6])
print(pal[5:9])
print(pal[9:12])
print(pal[6])#solo imprime una letra
print(pal[-1])#escoje desde adelante hacia atras

    #invertir string

print(pal[::-1])

    #funciones del sistema

print(pal.capitalize())
print(pal.upper())
print(pal.isnumeric())
print(pal.lower())
print(pal.count("i"))
print(pal[6].isupper())
print(pal.startswith("uni"))



















