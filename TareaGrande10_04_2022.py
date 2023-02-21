"""
Primera tarea de 20%
Estiven Hernández Alfaro
3stiven366@gmail.com
"""

lista = []

accion = True
while accion == True :
    valoringresado = input("Ingrese un valor numerico / si desea terminar escriba salir: ")
    if valoringresado == "salir" :
        accion = False
        print("_"*75)
        print("los elementos ingresados a la lista son: ", lista)
    else :
        try:
            lista.append (int(valoringresado))
        except ValueError:
            print("El valor ingresado no es correcto, por favor ingrese un valor numerico: ")

"""
Lo primero era hacer que el usuario ingresara los valores, entonces mientras que el usuario
ingresara un valor numerico, la accion va a ser verdadera, en caso de escribir salir se cumpliría el
if y el programa se detiene, mostrando los valores que el usuario ingresó.
Se me ocurrió hacer un "try" en caso de que el usuario ingrese un valor que no sea valido, en este caso
el error que ocurriría es un ValueError, donde se le pide que ingrese un valor valido.
"""

print("_"*75)

for recorrido in range(1,len(lista)):
   for posicion in range(len(lista) - recorrido):
    if lista[posicion] > lista[posicion + 1]:
        temp = lista[posicion]
        lista[posicion] = lista[posicion + 1]
        lista[posicion + 1] = temp
print("El orden de los digitos ingresados en la lista de menor a mayor es: ",lista)

"""
En este caso el programa debe de utilizar 2 for, el primero que debe definir el rango
el segundo debe de ubicar el numero que se evalua con respecto al siguiente.
en el caso de ser mayor que el que tiene a la derecha, toma el espacio que tenía, más 1 a la derecha.

"""

print("_"*75)

for recorrido in range(1,len(lista)):
   for posicion in range(len(lista) - recorrido):
    if lista[posicion] < lista[posicion + 1]:
        temp = lista[posicion]
        lista[posicion] = lista[posicion + 1]
        lista[posicion + 1] = temp
print("El orden de los digitos ingresados en la lista de mayor a menor es: ",lista)

"""
Esta situación es muy similar a la anterior, en diferencia de que si es menor, toma la posición derecha.
Haciendo así que los menores queden al final y los más grandes al inicio.
"""

print("_"*75)

moda = None
VCantidad = 0
for index, numero in enumerate(lista):
    aparece = lista.count(numero)
    if aparece > VCantidad :
        VCantidad = aparece
        moda = numero
print("La moda de la lista es el número ", moda)

"""
El primer numero (aparece) se evalua con Vcantidad que valia 0
como es mayor que 0, entonces toma el valor de VCantidad
El siguiente número se evalua con el que tomó VCantidad y si es mayor
tomará su posición, en caso de no ser mayor, se evalua hasta que se encuentre a otro mayor en
cantidad de veces que se repite (evaluando las cantidades con "count")
El que mayor "count" tenga, tomará el valor de la variable "moda":
"""

print("_"*75)

suma = 0
for elementos in lista:
    suma += elementos
print("La suma de los elementos ingresados en la lista es: ", suma)

"""
utilizando el for en el rango de la lista, se suma cada uno de los elementos de
ella hasta llegar al último
"""

print("_"*75)

promedio = suma/len(lista)
print("El promedio de los números ingresados es: ",promedio)

"""
La suma de la lista anterior, dividida por el rango de la lista, es decir la cantidad de
numeros sumados
"""

print("_"*75)

#Media
for posicionmedia in lista:
    x = int(len(lista)/2)
    y = int(len(lista)/2) - 1
    media = (lista[x] + lista[y])/2
print("La medida mediana en la lista es: ",media)

"""
sería suficiente ncontrar el elemento que está en el medio del rango diviendolo entre 2
sin embargo, en el caso de una cantidad de cifras par, el programa toma el numero que
está a la derecha de la mitad, por lo cual hay que tomar el que está en el lado izquierdo
sumar ambos y luego dividirlos entre 2.
"""

print("_"*75)

#Elemento mayor y menor

elementomayor = lista[0]
elementomenor = lista[len(lista) - 1]
print("El elemento mayor en la lista es: ",elementomayor)
print("El elemento menor de la lista es: ",elementomenor)

"""
Debido a que la lista quedó ordenada de mayor a menor, el elemento mayor
se encuentra ubicado en la posicion 0
Y el elemento menor se encuentra ubicado en la ultima posición, es decir en el rango - 1.
"""

print("_"*75)
if elementomenor < 0:
    elementomenor = elementomenor * -1
else:
    print(" ")
rangodelalista = elementomayor - elementomenor
print("El rango de la lista es de: ",rangodelalista)
"""
Tomando ambos elementos de la función anterior, es simplemente de restar,
sin embargo a la hora de restar un numero negativo, este por ley de signos se convierte en
positivo y se hace una suma, en vez de sacar la diferencia de los extremos.
para solunionar el problema hay que convertirlo en positivo.
"""
print("_"*75)

print("EL PROGRAMA HA FINALIZADO")













# QUESTION:
