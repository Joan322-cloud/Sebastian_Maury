impar = 0;par = 0;numero=5
while numero != 0:
    numero = int(input("Ingresa un número o escriba 0 para finalizar:"))
 
    if numero % 2 == 1: # Verificar si el número es impar
        impar += 1 # Incrementar en 1 el contador
    else:
        par += 1 # Incrementar en 1 el contador
# Al finalizar bucle imprimir resultados.
print("Conteo de números impares:", impar)
print("Conteo de números pares:", par)