#¿Como Declarar una Lista?
myList = [] #lista vacia
myList = ["Apple", "Orange", "Donkey"] # La única forma de declarar una lista
myTuple = ("Apple", "Orange", "Donkey") # Esto no es una lista, es una version más limitada llamada "Tupla"
mySet = {"Apple", "Orange", "Donkey"} # Esto no es una lista, es una version más limitada llamada "set" (cojunto).

#Acceder a los items en la lista
print(myList[0])  # Esto imprimirá el 1er elemento en la consola.
aux = myList[2]
print(aux); # Esto imprimirá el 4to elemento en la consola.
print(len(myList))
# print(myList[myList.length-1]);  #vEsto imprimirá el último elemento en la consola.
print(myList[len(myList)-1]);  #vEsto imprimirá el último elemento en la consola.

#Actualizar Elementos en el Arreglo
myList[2] = 'Whatever value'
# Esto asignará el valor 'Whatever value' en el sexto elemento de la lista.
print(myList)

#Añadiendo elementos a una lista (función append o insert)

#Utilizando append en las listas de Python
myList = ['Pedro','Juan','Maria']
myList.append('Chris') # esto agrega a chris al final del arreglo
print(myList); # esto imprimirá ['Pedro','Juan','Maria','Chris'];

#Utilizando insert (seleccionando posición) en Python
myList = ['Pedro','Juan','Maria']
myList.insert(1,'Chris') # esto agrega a chris entre Pedro y Juan
print(myList); # esto imprimirá ['Pedro','Chris','Juan','Maria'];

#Eliminando items de una lista con Python(función pop, remove, delete)

#Eliminando elementos de una lista con POP
myList = ['Pedro','Chris','Juan','Maria']
myList.pop()
print(myList) # esto imprimirá ['Pedro','Chris','Juan']

#Eliminando elementos de una lista con Remove
#Si deseas eliminar 'Chris', necesitas hacer lo siguiente: 
myList = ['Pedro','Chris','Juan','Maria']
myList.remove('Juan')
print(myList) # esto imprimirá ['Pedro','Chris','Juan'];

#Eliminando elementos de una lista con Delete
#Si deseas eliminar 'Chris', necesitas hacer lo siguiente: 
myList = ['Pedro','Chris','Juan','Maria','Pepe','Mario','Bob']
print(myList)
del myList[2:5]
print(myList) # esto imprimirá ['Pedro', 'Chris', 'Mario', 'Bob']

#Iterando sobre una lista (bucles)
myList = [3423,5,4,47889,654,8,867543,23,48,56432,55,23,25,12]
for number in myList:
    print(number)

#Iterando usando la posicion
for i in range(0,len(myList)):
    print("La posicion es "+ str(i) +" para el elemento "+ str(myList[i]))
    # print("La posicion es "+str(i)+" para el elemento "+myList[i])

### Imprimira lo siquiente
# La posicion es 0 para el elemento Pedro
# La posicion es 1 para el elemento Chris
# La posicion es 2 para el elemento Mario
# La posicion es 3 para el elemento Bob