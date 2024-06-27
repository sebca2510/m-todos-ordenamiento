def Blineal(valor):
    for x in range(len(lista)):
        if lista[x] == valor :
            return x 
    return None
def dato(valor): 
    if Blineal(valor) == None:
        return "El valor %d buscado no existe"%(valor)
    else:
        return "El valor %d se econtros en indice: %d"%(valor, Blineal(valor))


lista = [23, 7, 785, 4, 15, 47, 200]    


for i in range(len(lista)):
    print("[%d]=>[%d]"%(i, lista[i]))
print(dato(7))
