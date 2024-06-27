def mergesortmen(arr):
    if len(arr) <= 1:
        return arr
    
    mitad = len(arr) // 2
    izmid = arr[:mitad]
    demid = arr[mitad:]

    # Aplicar Merge Sort de forma recursiva en ambas mitades
    izmid = mergesortmen(izmid)
    demid = mergesortmen(demid)

    # Combinar (merge) las mitades ordenadas
    return merge(izmid, demid)

def merge(iz, de):
    result = []
    izdex, dedex = 0, 0

    #Para cambiar de "menor a mayor" a "mayor a mnenor" camiar el < 
    while izdex < len(iz) and dedex < len(de):
        if iz[izdex] < de[dedex]:
            result.append(iz[izdex])
            izdex += 1
        else:
            result.append(de[dedex])
            dedex += 1

    result.extend(iz[izdex:])
    result.extend(de[dedex:])
    return result

# Ejemplo de uso:
lista_desordenada = [10, 15, 25, 2]
lista_ordenada = mergesortmen(lista_desordenada)
print(lista_ordenada)