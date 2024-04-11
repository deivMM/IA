import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

imagen = Image.open("../data/digits/0_1.png")
array_imagen = np.array(imagen)

imagen_redimensionada = imagen.resize((30, 30))

print("Dimensiones de la imagen:", array_imagen.shape)
print("Array de la imagen:\n", array_imagen)

f, ax = plt.subplots(figsize=(6, 6))
ax.imshow(imagen_redimensionada, cmap='gray')
ax.axis('off')
plt.show()

print('terminado')