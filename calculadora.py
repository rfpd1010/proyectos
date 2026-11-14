ganancia = int(input("¿cuanto ganaste hoy?"))
perdida = int(input("¿cuanto gastaste en publicidad?"))
anterior = int(input("¿cuanto ganaste ayer?"))
ganancia_neta = ganancia - perdida
diferencia = ganancia_neta - anterior
porcentaje = (diferencia / anterior) * 100
print("tu ganancia neta de hoy fue de", ganancia_neta)
if ganancia_neta > anterior:print("tu ganancia fue mayor que ayer")
elif ganancia_neta < anterior:
    print("Tu ganancia fue menor a la de ayer")
else: print("tu ganancia fue igual que ayer")
print("el cambio fue del", porcentaje, "%")
