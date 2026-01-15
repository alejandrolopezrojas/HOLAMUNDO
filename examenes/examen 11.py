#punto 1
""" dat = input("ingrese dato=")
if dat.isspace():
    print("Dato vacío o con espacios")
elif dat.isnumeric() or (dat.isnumeric and "." in dat):
    print("Número válido")
elif dat.isalpha():
    print("Contiene letras")
elif dat.isalnum:
        print("contiene letras y numeros") """


#punto 2
""" dat2 = input("ingrese dato=")

if dat2 == "0":
    print("0")
elif "-" in dat2:
    intdat2 = int(dat2)
    if intdat2 < 0:
        print("negativo")
elif dat2.isnumeric():
    print("positivo")
elif dat2.isalpha():
    print("dato invalido")
else:
    print("XD") """

#punto 3
""" edad = input("ingrese su edad= ")

if not edad.isdigit():
    print("edad invalida")
elif int(edad) < 18:
    print("acceso permitido")
elif int(edad) > 18:
    print("acceso denegado") """

""" #punto 4
a, b = input("a="), input("b=")
if not a.isnumeric() or not b.isnumeric():
    print("datos invalidos")
elif b == "0":
    print("no se puede dividir en 0")
else:
    print(int(a) / int(b)) """

#punto 5
val = input("valor= ")

if val.isspace():
    print("vacio")
elif val.isalnum():
        print("mixto")
elif val.isalpha():
    print("texto")
elif val.isnumeric():
    print("numeros")





















