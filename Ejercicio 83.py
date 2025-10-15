import tkinter as tk
from tkinter import messagebox
import math

class FiguraGeometrica:
    def __init__(self):
        self._volumen = 0.0
        self._superficie = 0.0
    def set_volumen(self, v):
        self._volumen = v
    def set_superficie(self, s):
        self._superficie = s
    def get_volumen(self):
        return self._volumen
    def get_superficie(self):
        return self._superficie

class Cilindro(FiguraGeometrica):
    def __init__(self, radio, altura):
        super().__init__()
        self.radio = radio
        self.altura = altura
        self.set_volumen(self.calcular_volumen())
        self.set_superficie(self.calcular_superficie())
    def calcular_volumen(self):
        return math.pi * self.altura * (self.radio ** 2)
    def calcular_superficie(self):
        return 2.0 * math.pi * self.radio * self.altura + 2.0 * math.pi * (self.radio ** 2)

class Esfera(FiguraGeometrica):
    def __init__(self, radio):
        super().__init__()
        self.radio = radio
        self.set_volumen(self.calcular_volumen())
        self.set_superficie(self.calcular_superficie())
    def calcular_volumen(self):
        return (4.0 / 3.0) * math.pi * (self.radio ** 3)
    def calcular_superficie(self):
        return 4.0 * math.pi * (self.radio ** 2)

class Piramide(FiguraGeometrica):
    def __init__(self, base, altura, apotema):
        super().__init__()
        self.base = base
        self.altura = altura
        self.apotema = apotema
        self.set_volumen(self.calcular_volumen())
        self.set_superficie(self.calcular_superficie())
    def calcular_volumen(self):
        return (self.base ** 2) * self.altura / 3.0
    def calcular_superficie(self):
        return (self.base ** 2) + 2.0 * self.base * self.apotema

class VentanaCilindro(tk.Toplevel):
    def __init__(self, master=None):
        super().__init__(master)
        self.title("Cilindro")
        self.geometry("300x190")
        self.resizable(False, False)
        tk.Label(self, text="Radio (cm):").place(x=20, y=20, width=110, height=23)
        tk.Label(self, text="Altura (cm):").place(x=20, y=50, width=110, height=23)
        self.e_radio = tk.Entry(self)
        self.e_altura = tk.Entry(self)
        self.e_radio.place(x=140, y=20, width=130, height=23)
        self.e_altura.place(x=140, y=50, width=130, height=23)
        self.btn = tk.Button(self, text="Calcular", command=self.calcular)
        self.btn.place(x=140, y=80, width=130, height=25)
        self.l_vol = tk.Label(self, text="Volumen (cm³):")
        self.l_sup = tk.Label(self, text="Superficie (cm²):")
        self.l_vol.place(x=20, y=115, width=250, height=23)
        self.l_sup.place(x=20, y=140, width=250, height=23)
    def calcular(self):
        try:
            r = float(self.e_radio.get().strip())
            h = float(self.e_altura.get().strip())
            c = Cilindro(r, h)
            self.l_vol.config(text=f"Volumen (cm³): {c.calcular_volumen():.2f}")
            self.l_sup.config(text=f"Superficie (cm²): {c.calcular_superficie():.2f}")
        except Exception:
            messagebox.showerror("Error", "Campo nulo o error en formato de número")

class VentanaEsfera(tk.Toplevel):
    def __init__(self, master=None):
        super().__init__(master)
        self.title("Esfera")
        self.geometry("300x170")
        self.resizable(False, False)
        tk.Label(self, text="Radio (cm):").place(x=20, y=20, width=110, height=23)
        self.e_radio = tk.Entry(self)
        self.e_radio.place(x=140, y=20, width=130, height=23)
        self.btn = tk.Button(self, text="Calcular", command=self.calcular)
        self.btn.place(x=140, y=50, width=130, height=25)
        self.l_vol = tk.Label(self, text="Volumen (cm³):")
        self.l_sup = tk.Label(self, text="Superficie (cm²):")
        self.l_vol.place(x=20, y=85, width=250, height=23)
        self.l_sup.place(x=20, y=110, width=250, height=23)
    def calcular(self):
        try:
            r = float(self.e_radio.get().strip())
            e = Esfera(r)
            self.l_vol.config(text=f"Volumen (cm³): {e.calcular_volumen():.2f}")
            self.l_sup.config(text=f"Superficie (cm²): {e.calcular_superficie():.2f}")
        except Exception:
            messagebox.showerror("Error", "Campo nulo o error en formato de número")

class VentanaPiramide(tk.Toplevel):
    def __init__(self, master=None):
        super().__init__(master)
        self.title("Pirámide")
        self.geometry("320x230")
        self.resizable(False, False)
        tk.Label(self, text="Base (cm):").place(x=20, y=20, width=110, height=23)
        tk.Label(self, text="Altura (cm):").place(x=20, y=50, width=110, height=23)
        tk.Label(self, text="Apotema (cm):").place(x=20, y=80, width=110, height=23)
        self.e_base = tk.Entry(self)
        self.e_altura = tk.Entry(self)
        self.e_apotema = tk.Entry(self)
        self.e_base.place(x=140, y=20, width=150, height=23)
        self.e_altura.place(x=140, y=50, width=150, height=23)
        self.e_apotema.place(x=140, y=80, width=150, height=23)
        self.btn = tk.Button(self, text="Calcular", command=self.calcular)
        self.btn.place(x=140, y=110, width=150, height=25)
        self.l_vol = tk.Label(self, text="Volumen (cm³):")
        self.l_sup = tk.Label(self, text="Superficie (cm²):")
        self.l_vol.place(x=20, y=150, width=270, height=23)
        self.l_sup.place(x=20, y=175, width=270, height=23)
    def calcular(self):
        try:
            b = float(self.e_base.get().strip())
            h = float(self.e_altura.get().strip())
            a = float(self.e_apotema.get().strip())
            p = Piramide(b, h, a)
            self.l_vol.config(text=f"Volumen (cm³): {p.calcular_volumen():.2f}")
            self.l_sup.config(text=f"Superficie (cm²): {p.calcular_superficie():.2f}")
        except Exception:
            messagebox.showerror("Error", "Campo nulo o error en formato de número")

class VentanaPrincipal(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Figuras")
        self.geometry("340x150")
        self.resizable(False, False)
        self._crear_componentes()
    def _crear_componentes(self):
        btn_cil = tk.Button(self, text="Cilindro", command=lambda: VentanaCilindro(self))
        btn_esp = tk.Button(self, text="Esfera", command=lambda: VentanaEsfera(self))
        btn_pir = tk.Button(self, text="Pirámide", command=lambda: VentanaPiramide(self))
        btn_cil.place(x=25, y=50, width=90, height=28)
        btn_esp.place(x=125, y=50, width=90, height=28)
        btn_pir.place(x=225, y=50, width=90, height=28)

if __name__ == "__main__":
    app = VentanaPrincipal()
    app.mainloop()

