    #LISTAS
comidas = ["hamburguesa", "pizza", "empanada", "perros", "arepa", "manzana"]#varios datos

persona_1 = ["alejandro", "lopez", "rojas", 16, 1.83]

numeros = [1,13232, 14, 6313, 22, -3145]

#puede almacenar datos de diferentes tipos

print(comidas)
print(comidas, persona_1)#mas de una por linea
print(comidas + persona_1)#en una sola celda

print(len(persona_1))#cuantos datos contiene

    #ACCEDER A DATOS
print("\tACCEDER A DATOS")
print(persona_1[2])
print(persona_1[2][3])#letra especifica de un dato
print(len(persona_1[0]))#contar letras de dato especifico

    #FUNCIONES DEL SISTEMA
print(persona_1.count("alejandro"))#cuantos datos iguales hay

persona_2 = persona_1.copy()#copiar una lista en otra
print(persona_2)

persona_2.reverse()#invertir orden de los datos
print(persona_2)

numeros.sort()#ordena los datos, y tambien puede por criterios
print(numeros)
comidas.sort()
print(comidas)

nombre, apellido1, apellido2, edad, estatura = persona_1#asignar datos de la lista a variables
print(f"{apellido2} {nombre} {estatura}")

    #AÑADIR UN NUEVO ELEMENTO

persona_1.append("floridablanca")
persona_1.append(2009)
print(persona_1)

persona_1.insert(3, "colombia")#insertar dato en pisición enpecifico
print(persona_1)

persona_1[3] = "argentina"#cambiar un dato por otro
print(persona_1)

    #ELIMINAR ELEMENTOS

print(persona_1.remove(2009))#elimina el dato que coincida
print(persona_1)

del persona_1[0]#elimina el dato por su indice
print(persona_1)

print(persona_1.pop(2))#borra y ademas muestra o sabe que dato borro
print(persona_1)
pop_dato = persona_1.pop(0)#almacena en una variable el elemento borrado de la lista

persona_1.clear()
print(persona_1)










