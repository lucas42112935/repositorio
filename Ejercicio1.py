#Incrementar y decrementar
import tkinter as tk

class Aplicacion():
    def __init__(self):
        self.valor="1"
        self.ventana1=tk.Tk()
        self.ventana1.title=("Controles Button y Label")
        self.label1=tk.Label(self.ventana1, text="self.valor")
        self.label1.grid(column=0, row=0)
        #self.label1.configure(forground="red")


        self.boton2=tk.Button(self.ventana1, text="Decrementar", command=self.decrementar)
        self.boton2.grid(column=0, row=2)

        self.ventana1.mainloop()


    def decrementar(self):
        self.valor=self.valor+1
        self.label1.config(text=self.valor)
     


Aplicacion = Aplicacion()