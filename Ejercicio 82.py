import tkinter as tk
from tkinter import messagebox

class Notas:
    def __init__(self):
        self.lista_notas = [0.0] * 5

    def calcular_promedio(self):
        return sum(self.lista_notas) / len(self.lista_notas)

    def calcular_desviacion(self):
        prom = self.calcular_promedio()
        suma = sum((x - prom) ** 2 for x in self.lista_notas)
        return (suma / len(self.lista_notas)) ** 0.5

    def calcular_menor(self):
        return min(self.lista_notas)

    def calcular_mayor(self):
        return max(self.lista_notas)


class VentanaPrincipal(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Notas")
        self.geometry("320x360")
        self.resizable(False, False)
        self._crear_componentes()

    def _crear_componentes(self):
        self.labels_notas = []
        self.entradas = []

        for i in range(5):
            lbl = tk.Label(self, text=f"Nota {i+1}:")
            lbl.place(x=20, y=20 + i*30, width=100, height=23)
            self.labels_notas.append(lbl)

            ent = tk.Entry(self)
            ent.place(x=140, y=20 + i*30, width=140, height=23)
            self.entradas.append(ent)

        self.btn_calcular = tk.Button(self, text="Calcular", command=self._calcular)
        self.btn_calcular.place(x=20, y=175, width=110, height=27)

        self.btn_limpiar = tk.Button(self, text="Limpiar", command=self._limpiar)
        self.btn_limpiar.place(x=170, y=175, width=110, height=27)

        self.lbl_promedio = tk.Label(self, text="Promedio = ")
        self.lbl_promedio.place(x=20, y=215, width=260, height=23)

        self.lbl_desviacion = tk.Label(self, text="Desviación = ")
        self.lbl_desviacion.place(x=20, y=240, width=260, height=23)

        self.lbl_mayor = tk.Label(self, text="Nota mayor = ")
        self.lbl_mayor.place(x=20, y=265, width=260, height=23)

        self.lbl_menor = tk.Label(self, text="Nota menor = ")
        self.lbl_menor.place(x=20, y=290, width=260, height=23)

    def _calcular(self):
        try:
            notas = Notas()
            for i in range(5):
                notas.lista_notas[i] = float(self.entradas[i].get().strip())

            prom = notas.calcular_promedio()
            desv = notas.calcular_desviacion()
            mayor = notas.calcular_mayor()
            menor = notas.calcular_menor()

            self.lbl_promedio.config(text=f"Promedio = {prom:.2f}")
            self.lbl_desviacion.config(text=f"Desviación = {desv:.2f}")
            self.lbl_mayor.config(text=f"Valor mayor = {mayor:.2f}")
            self.lbl_menor.config(text=f"Valor menor = {menor:.2f}")

        except ValueError:
            messagebox.showerror("Entrada inválida", "Por favor ingresa 5 números válidos (usa punto decimal).")

    def _limpiar(self):
        for ent in self.entradas:
            ent.delete(0, tk.END)
        self.lbl_promedio.config(text="Promedio = ")
        self.lbl_desviacion.config(text="Desviación = ")
        self.lbl_mayor.config(text="Nota mayor = ")
        self.lbl_menor.config(text="Nota menor = ")


if __name__ == "__main__":
    app = VentanaPrincipal()
    app.mainloop()
