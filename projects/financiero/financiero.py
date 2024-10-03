import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def interes_compuesto(Ci, tasa_interes, t):
    """
    Interés compuesto anual.

    Parámetros:
    Ci (float): La cantidad inicial de dinero.
    tasa_interes (float): La tasa de interés anual (en porcentaje).
    t (int): El número de años.

    Retorna:
    float: El valor total después del interés compuesto.
    """
    t = np.linspace(0, t, 100)
    return t, Ci * (1 + tasa_interes / 100) ** t

def interes_compuesto_con_aportes(Ci, tasa_interes, t, aporte_anual):
    """
    Calcula el interés compuesto anual con aportes anuales.

    Parámetros:
    Ci (float): La cantidad inicial de dinero.
    tasa_interes (float): La tasa de interés anual (en porcentaje).
    t (int): El número de años.
    aporte_anual (float): La cantidad de dinero que se agrega al final de cada año.

    Retorna:
    float: El valor total después del interés compuesto con aportes.
    """
    t = np.arange(0, t+1, 1)
    monto_total_list = []
    monto_total = Ci
    aportación_acumulada = 0
    aportaciones = []
    for _ in t:
        aportaciones.append(aportación_acumulada)
        monto_total_list.append(monto_total)
        monto_total = monto_total * (1 + tasa_interes / 100)
        monto_total += aporte_anual
        aportación_acumulada += aporte_anual
        
    return t, np.array(monto_total_list), np.array(aportaciones)

t, dinero = interes_compuesto(10000, 5, 10)

f, ax = plt.subplots(figsize=(8, 8))
ax.plot(t, dinero)
# ax.set_ylim(0, dinero.max()*1.05)
print(dinero.max())

t, dinero, aportaciones = interes_compuesto_con_aportes(10000, 5, 10, 1000)

# f, ax = plt.subplots(figsize=(8, 8))
ax.plot(t, dinero)
ax.bar(t, aportaciones)
ax.set_ylim(0, dinero.max()*1.05)
print(dinero.max())
plt.show()
