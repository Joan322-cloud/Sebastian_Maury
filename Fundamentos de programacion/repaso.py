print("pintado de muros")
print("====================================")
#indicar las variables o constantes al inicio

costo_brocha=15
costo_valde=75

largo=float(input("ingrese largo del muro(en metros) :"))
alto=float(input("ingrese el alto del muro(en metros):"))

#procesos o calculos para obtener resultados
area= largo*alto
cant_brochas=area/30
cant_valdes=area/6.5
costo_brochas=cant_brochas*costo_brocha
costo_valdes=cant_valdes*costo_valde # type: ignore

costo_total=costo_brochas+costo_valdes

#la salida de datos o resultados
print("====================================")
print("el muro tiene :",area, "m2")
print("cantidad de brochas:", round(cant_brochas))
print("cantidad de valdes de pintura :",round(cant_valdes,2))

print("costo de materiales :", round(costo_total,2), "soles")