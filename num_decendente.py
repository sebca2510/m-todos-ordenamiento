numeros = []
while len(numeros) <10:
    try:
        numero = float(input("Indruzca un numero: "))
        numeros.append(numero)
    except ValueError:
        print("numero no valido, introduzca otro")

acendente = sorted(numeros)
decendente = sorted(numeros, reverse=True)

print("Nuemeros ordenados de forma acendente: ")
print("\n", acendente)
print("\n", "Numeros ordenados de forma decendente:  ")
print("\n", decendente)

buscar = float(input("¿Qué numero desea buscar?"))
if buscar in numeros:
    print(f"{buscar} esta en la lista ")
else:
    print(f"{buscar} no esta en la lista")
