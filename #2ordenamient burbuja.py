lista = [5, 7, 2, 10, 12, 3]

for i in range(len(lista)):
    for x in range(len(lista)-1):
        #camabiando el sigdo de < y > se cambiar el orden de la lista  
        if lista[x] < lista	[x+1]:
            aux = lista	[x] 
            lista[x] = lista[x+1]
            lista[x+1] = aux
            
print(lista)
