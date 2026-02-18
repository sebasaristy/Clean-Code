

def calcular_cuota(compra, tasa, plazo):
    """
    :compra: Valor de la compra con la tarjeta
    :interes: Tasa de interes mensual representada como decimal
    :plazo: Numero de cuoatas a diferir la compra
    """
    if tasa ==0:
        return compra / plazo
    else:
        return (compra*tasa) / (1 - (1+tasa)** (-plazo))

def calcular_abonos(compra, tasa, plazo):
    ...

def calcular_interes():
    ...