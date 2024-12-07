import itertools

lista1 = [1,2,3]
lista2 = [4,5,6]
lista_unida = [*lista1, *lista2]
lista_suma = lista1 + lista2
lista_unida_suma = [elemento for elemento in lista1] + [elemento for elemento in lista2]
lista_iter = list(itertools.chain(lista1,lista2))
lista_aux = list()
lista_aux.extend(lista1)
lista_aux.extend(lista2)

lista2.append(7)

print(lista_unida) #resultado[1,2,3,4,5,6]
print(lista_suma) #resultado[1,2,3,4,5,6]
print(lista_unida_suma) #resultado[1,2,3,4,5,6,7]
print(lista_iter) #resultado[1,2,3,4,5,6]
print(lista_aux) #resultado[1,2,3,4,5,6,7]