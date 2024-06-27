lista = [5, 7, 2, 10, 12, 3]

for i in range(len(lista)):
    min = i
    for x in range(i, len(lista)):
        #Remplazart el < cambia el orden de la lista
        if lista[x] < lista[min]:
            min = x 
    aux = lista[i]
    lista[i] = lista[min]
    lista[min]= aux
    #print(lista)
print(lista)