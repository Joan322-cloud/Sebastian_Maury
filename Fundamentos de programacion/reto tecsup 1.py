horas = int(input("introduzca las horas: "))
tarifa = float(input("introduzca la tarifa por hora: "))
if horas>40:
    salario_normal=40*tarifa
    horas_extras=(horas-40)*(tarifa*1.5)
    salario=salario_normal+horas_extras
else:
    salario=horas*tarifa
print(f"salario:{salario}")