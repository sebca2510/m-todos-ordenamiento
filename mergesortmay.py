def mergesortmay(arr):
    if len(arr) <= 1:
        return arr
    
    mitad = len(arr) // 2
    izmid = arr[:mitad]
    demid = arr[mitad:]

    
    izmid = mergesortmay(izmid)
    demid = mergesortmay(demid)

    
    return merge(izmid, demid)

def merge(iz, de):
    result = []
    izdex, dedex = 0, 0

    
    while izdex < len(iz) and dedex < len(de):
        if iz[izdex] > de[dedex]:
            result.append(iz[izdex])
            izdex += 1
        else:
            result.append(de[dedex])
            dedex += 1

    result.extend(iz[izdex:])
    result.extend(de[dedex:])
    return result

# Ejemplo de uso:
lista_desordenada = [38, 27, 43, 3, 9, 82, 10]
lista_ordenada = mergesortmay(lista_desordenada)
print(lista_ordenada)