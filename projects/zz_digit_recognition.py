import tkinter as tk
from tkinter import messagebox
from PIL import Image
import os
import io

import matplotlib.pyplot as plt
def plotear_nose_k(img):
    imagen_redimensionada = img.resize((20, 20))
    f, ax = plt.subplots(figsize=(6, 6))
    ax.imshow(imagen_redimensionada, cmap='gray')
    ax.axis('off')
    plt.show()

class DrawingApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Drawing App")

        self.canvas = tk.Canvas(self.master, width=300, height=300, bg="white")
        self.canvas.pack()

        self.canvas.bind("<B1-Motion>", self.draw)

        self.selected_number = tk.StringVar(master)
        self.selected_number.set("0")  # Establecer el valor inicial en 0
        numbers = [str(i) for i in range(10)]  # Crear lista de números del 0 al 9
        self.number_dropdown = tk.OptionMenu(self.master, self.selected_number, *numbers)
        self.number_dropdown.pack()

        self.button_send = tk.Button(self.master, text="Comprobar", command=self.comprobar)
        self.button_send.pack(side=tk.LEFT)

        self.button_clear = tk.Button(self.master, text="Borrar", command=self.clear)
        self.button_clear.pack(side=tk.RIGHT)

        self.line_width = 20
        self.line_join_style = tk.ROUND

    def draw(self, event):
        x, y = (event.x), (event.y)
        self.canvas.create_oval(x, y, x + self.line_width, y + self.line_width, fill="black", outline="black")

    def comprobar(self):
        numero = self.selected_number.get()
        # Capturar la imagen del lienzo
        ps = self.canvas.postscript(colormode='color')
        img = Image.open(io.BytesIO(ps.encode('utf-8')))
        plotear_nose_k(img)
        self.canvas.delete("all")
        respuesta = messagebox.askquestion("Confirmación",f"¿El numero escrito es un: {numero}?")

    def clear(self):
        self.canvas.delete("all")
        print('Imagen borrada')

def main():
    print(os.getcwd())
    root = tk.Tk()
    app = DrawingApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()



