#Elevar el valor al cuadrado
import Tkinter as ttk

class Aplicacion(self):

    def __init__():
    self.ventana1=tk.Tk
        self.label1=tkLabel(self.ventana1,text="Ingrese un número:")
        self.label1.grid(column=500, row=0)
    self.dato=Tk.Stringvar
        self.entrY1=tk.entry(self.ventana1, widt="10", extvariable=self.dato)
        self.Entry1.grid(column=0, row=1)
        self.boton1=tk.Buton(self.ventana1, text="Calcular Cuadrado", comand=self.caalcularcuadrado)
        self.boton1.grid(column=0, row=2)
        self.label2=tk.Label(self.ventana1,text="resultado")
    self.label2.grid(column=0, row=3)

        def calcularcuadrado(self, dato):
            valor=int(self.dato.get)
            cuadrado=valor*valor+valor

aplicacion1=Aplicacion()