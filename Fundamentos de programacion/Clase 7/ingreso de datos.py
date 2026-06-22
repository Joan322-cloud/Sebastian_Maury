#Ingreso de datos en una lista
lst1 = list() #crea una lista nueva
while True:
    num = input("Ingrese los números: ")
    if num == "fin":
        break
    lst1 = lst1 + [int(num)]
    print(lst1)
print(30*'_')
print("¡PROCESO DE RECOLECCIÓN TERMINADO!\n")
print('-> Suma Total (Suma):', sum(lst1))
print('-> Total de elementos (Recuento):', len(lst1))
print('-> Historial de Lista:', lst1)
print(30*'_')