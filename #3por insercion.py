lista = [5, 7, 2, 10, 12, 3]

for i in range(1,len(lista)):
    #se incerta una pocision -1 para poder comparar y almacernar el valor a remplazar 
    aux = lista[i]
    j = i -1
    #cambiando el signo < depsues de aux por > cambia el orden de la lista 
    while j >= 0 and aux < lista[j]:
        lista[j+1] = lista[j]
        lista[j] = aux 
        j-=1
        
print(lista)
