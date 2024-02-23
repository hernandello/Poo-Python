"""2. Crear una lista con 5 elementos y luego aplica los siguientes accionables:
↪ Imprimir el último elemento
↪ Modiﬁcar el valor del tercer elemento
↪ Agregar dos elementos
↪ Eliminar algún elemento
"""

lista = [1,2,3,4,5]

print (lista)

print (lista[-1])

lista[2]=0
print(lista)

lista.append (6)
lista.append(7)
print (lista)

lista.pop(2)
print (lista)


