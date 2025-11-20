import numpy as np
import matplotlib.pyplot as plt

f = lambda x: x**x - 100
f_deriv = lambda x: x**x * (np.log(x)+1)

x = np.linspace(0.1,5,101)
y = f(x)

it = 0
xn = 5
umbral = 0.0001

iteraciones = [xn]
residuos = [f(xn)]

while True:
    residuo = f(xn)
    it += 1
    print(f'Iteracion: {it}')
    print(f'Residuo: {residuo:.4f}')
    print(f'Solucion: {xn:.4f}')
    print('----')
   
    if abs(residuo) < umbral:
        break   

    xn = xn - residuo / f_deriv(xn)
    iteraciones.append(xn)
    residuos.append(f(xn))

fig, ax = plt.subplots(figsize=(6, 6))

ax.plot(x, y)
ax.axhline(0, color='gray', alpha=.2)  # Línea y=0 para referencia
ax.scatter(iteraciones, [f(xi) for xi in iteraciones], color='red', zorder=5, label='Iteraciones')

for i in range(len(iteraciones)-1):
    ax.plot([iteraciones[i], iteraciones[i+1]], [f(iteraciones[i]), 0], 'r--', alpha=0.5, lw=1)

for xi in iteraciones:
    ax.plot([xi, xi], [0, f(xi)], color='blue', alpha=0.5, lw=1)

plt.show()