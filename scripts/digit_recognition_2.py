from PIL import Image
import numpy as np

# Abrir la imagen
imagen = Image.open("data/digits/1_1.png")  # Reemplaza "tu_imagen.jpg" con la ruta de tu imagen
array_imagen = np.array(imagen)

# Redimensionar la imagen a 64x64 píxeles
imagen_redimensionada = imagen.resize((64, 64))



print("Dimensiones de la imagen:", array_imagen.shape)

# Mostrar el array
print("Array de la imagen:\n", array_imagen)

# Mostrar la imagen
imagen_redimensionada.show()