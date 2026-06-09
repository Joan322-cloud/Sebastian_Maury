print ("hola programador" \
"")
print("como se llama?")
nombre=input()
print(f"me alegro de conocerle, {nombre}")
print("me alegro de conocerlo", nombre)
print("******************************")
print("******************************")
cantidad=float(input("digame una cantidad en euros(hasta con decimales):"))
print(f"{cantidad} euros son {cantidad*3.97} soles")
8
print("******************************")
print("******************************")
edad=int(input("cuantos años tiene?"))
if edad < 18:
    print("Acceso denegado: es usted menor de edad")
else:
    print("Acceso permitido: usted es mayor de edad")
print("hasta la proxima! :V")
print("******************************")
print("******************************")
print("******************************")

edad = int(input("¿Cuántos años tiene?: "))


if edad < 0:
    print("No se puede tener una edad negativa")
elif edad < 15:
    print("Es usted menor de edad y tiene edad menor a 15")
elif edad < 18:
    print("Es usted menor de edad y tiene edad menor a 18")
else:
    print("Es usted mayor de edad")
    
print('********************************************')
print('********************************************')

nota = float(input("Ingrese la nota final (0 - 20): "))


if nota >= 17:
    print("Rendimiento: Excelente")
elif nota >= 13:
    print("Rendimiento: Aprobado")
elif nota >= 10:
    print("Rendimiento: Sustitutorio pendiente")
else:
    print("Rendimiento: Desaprobado")
print('********************************************')
print('********************************************')

### Declaración IF-ANIDADO
password = input ("Ingrese la contraseña: ")


if (len(password) >= 8):
    print('Tu contraseña es suficientemente larga.')
    if(password == 'miClaveSegura'):
        print("Además es la contraseña correcta.")
    else:
        print("Pero es incorrecta.")


else:
    print('Tu contraseña es muy corta e insegura.')
    if(password != 'miClaveSegura'):
        print("Además, es incorrecta (por supuesto).")
print('********************************************')
print('********************************************')

### INGRESO MENSUAL
ingresos = float(input("Ingrese sus ingresos mensuales: "))


if ingresos >= 2500:
    print("Cumple con el ingreso mínimo.")
    historial = input("¿Tiene buen historial crediticio? (si/no): ").lower()
    
    # Condicional Anidado
    if historial == "si":
        print("¡Crédito APROBADO inmediatamente!")
    else:
        print("Crédito RECHAZADO por riesgo crediticio.")
else:
    print("Crédito RECHAZADO: Ingresos insuficientes.")
print('********************************************')
print('********************************************')

# 1. Solicitamos la respuesta al usuario
respuesta = input("¿Cuál es la capital de Francia?: ")


# 2. Aplicamos .lower() para asegurar que todo esté en minúsculas
respuesta_limpia = respuesta.lower()


# 3. Evaluamos la respuesta estandarizada
if respuesta_limpia == "parís" or respuesta_limpia == "paris":
    print("¡Correcto! Has ganado 10 puntos.")
else:
    print("Incorrecto. La respuesta era París.")


karboncito = input("que dijo el pollo?")
print("no joroben")