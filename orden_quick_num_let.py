
ordenar = {}

def datos():
    dato = input("Ingrese el dato a ordenar: ")
    if eletra == 1 and dato.isnumeric():
        ordenar[dato] = None
    elif eletra == 2 and dato.isalpha():
        ordenar[dato] = None
    else:
        print("El tipo de dato ingresado no coincide con tu selección.")

def quicksortmenor(arr):
    if len(arr) <= 1:
        return arr
    else:
        ref = arr[0]
        men = [x for x in arr[1:] if x <= ref]
        may = [x for x in arr[1:] if x > ref]
        return quicksortmenor(men) + [ref] + quicksortmenor(may)

def quicksortmayor(arr):
    if len(arr) <= 1:
        return arr
    else:
        ref = arr[0]
        men = [x for x in arr[1:] if x <= ref]
        may = [x for x in arr[1:] if x > ref]
        return quicksortmayor(may) + [ref] + quicksortmayor(men)

def mergesortmen(arr):
    if len(arr) <= 1:
        return arr
    
    mitad = len(arr) // 2
    izmid = arr[:mitad]
    demid = arr[mitad:]

    izmid = mergesortmen(izmid)
    demid = mergesortmen(demid)

    return merge(izmid, demid)

def merge(iz, de):
    result = []
    izdex, dedex = 0, 0

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

def mergesortmay(arr):
    if len(arr) <= 1:
        return arr
    
    mitad = len(arr) // 2
    izmid = arr[:mitad]
    demid = arr[mitad:]

    izmid = mergesortmen(izmid)
    demid = mergesortmen(demid)

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

print("¿Qué tipo de dato desea ordenar?")
eletra = int(input("1 = números, 2 = letras: "))

if eletra == 1:
    print("Seleccionaste ordenar números.")
elif eletra == 2:
    print("Seleccionaste ordenar letras.")

print("¿Qué tipo de ordenamiento desea utilizar?")
orden = input("1 = Quicksort, 2 = Mergesort: ")

if orden == "1":
    print("Seleccionaste Quicksort")
elif orden == "2":
    print("Seleccionaste Mergesort")

print("¿Qué tipo de orden desea?")
mezcla = input("1 = menor a mayor, 2 = mayor a menor: ")

if mezcla == "1":
    print("Seleccionaste ordenar de menor a mayor")
elif mezcla == "2":
    print("Seleccionaste ordenar de mayor a menor")

while True:
    datos()
    mas = input("¿Quiere agregar otro dato? (S/N): ")
    if mas.lower() != "s":
        break
print(list(ordenar.keys()))

if orden == "1" and mezcla == "1":
    ordenar = quicksortmenor(list(ordenar.keys()))
    print("los datos ordenados por quicksort y de menor a mayor quedarían:")
    print("\n", ordenar)#

elif orden == "1" and mezcla == "2":
    ordenar = quicksortmayor(list(ordenar.keys()))
    print("los datos ordenados por quicksort y de mayor a menor quedarían:")
    print("\n", ordenar)

elif orden == "2" and mezcla == "1":
    ordenar = mergesortmen(list(ordenar.keys()))
    print("los datos ordenados por mergesort de menor a mayor quedarían:")
    print("\n", ordenar)
    
elif orden == "2" and mezcla == "2":
    ordenar = mergesortmay(list(ordenar.keys()))
    print("los datos ordenados por mergesort de mayor a menor quedarían:")
    print("\n", ordenar)
