montoAcumulado=0
monto=-1
while monto !=0:
    monto= int(input("Introduzca monto: "))
    if monto < 0:
        print("Introduzca monto positivo, por favor ")
    elif monto > 0:
        montoAcumulado = montoAcumulado + monto
    else: break
if montoAcumulado >= 1000:
    montoAcumulado = montoAcumulado *0.9
print("El total de la factura es: ", montoAcumulado)
