# La i, j, k son los iteradores mas comunes

for i in range(5): #For es para repetir acciones, realizar iteraciones en listas, cadena de texto, rango de numeros
    #range: Es una función que crea una lista range(n), crea una lista desde 0 hasta n-1.
    print(i)

for i in range(1, 6): # en este caso definimos el parametro de la lista desde 1 hasta (el segundo parametro) n-1 (6-1)
    print(i)

for i in range(0, 10, 2): # range(inico, fin-1, espaciado)
    print(i)

frutas = ["manzana", "pera", "uva", "uva"]

for i in list(frutas):
    print(i)

primer_elemento = frutas[0] #Se coloca entre corchete el numero de indice de la lista declarada
print("primer_elemento: ", primer_elemento)

segundo_elemento = frutas[1]
print(segundo_elemento)
print(frutas.count("uva"))
print(len(frutas))

