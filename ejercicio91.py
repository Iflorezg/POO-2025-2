import tkinter as tk
from tkinter import messagebox
from datetime import date

class Contacto:
    def __init__(self, nombres, apellidos, fechaNacimiento, direccion, telefono, correo):
        self.nombres = nombres
        self.apellidos = apellidos
        self.fechaNacimiento = fechaNacimiento
        self.direccion = direccion
        self.telefono = telefono
        self.correo = correo


class ListaContactos:
    def __init__(self):
        self.lista = []

    def agregarContacto(self, contacto):
        self.lista.append(contacto)


class VentanaContacto(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Detalles del contacto")
        self.geometry("600x300")

        self.listaContactos = ListaContactos()

        # --- Creamos el contenedor ---
        self.grid_frame = tk.Frame(self)
        self.grid_frame.pack(fill="both", expand=True)

        # --- Labels ---
        self.lbl_nombres = tk.Label(self.grid_frame, text="Nombres:")
        self.lbl_apellidos = tk.Label(self.grid_frame, text="Apellidos:")
        self.lbl_fecha = tk.Label(self.grid_frame, text="Fecha nacimiento:")
        self.lbl_direccion = tk.Label(self.grid_frame, text="Dirección:")
        self.lbl_telefono = tk.Label(self.grid_frame, text="Teléfono:")
        self.lbl_correo = tk.Label(self.grid_frame, text="Correo:")

        # --- Entry ---
        self.campoNombres = tk.Entry(self.grid_frame)
        self.campoApellidos = tk.Entry(self.grid_frame)
        self.campoFecha = tk.Entry(self.grid_frame)
        self.campoDireccion = tk.Entry(self.grid_frame)
        self.campoTelefono = tk.Entry(self.grid_frame)
        self.campoCorreo = tk.Entry(self.grid_frame)

        # --- Lista ---
        self.lista = tk.Listbox(self.grid_frame)

        # --- Botón ---
        self.btn_agregar = tk.Button(self.grid_frame, text="Agregar", command=self.mostrarDatos)

        self.start()


    def start(self):
        g = self.grid_frame

        g.columnconfigure(0, weight=1)
        g.columnconfigure(1, weight=1)

        # Fila 0
        self.lbl_nombres.grid(row=0, column=0, sticky="w", padx=5, pady=5)
        self.campoNombres.grid(row=0, column=1, sticky="ew", padx=5, pady=5)

        # Fila 1
        self.lbl_apellidos.grid(row=1, column=0, sticky="w", padx=5, pady=5)
        self.campoApellidos.grid(row=1, column=1, sticky="ew", padx=5, pady=5)

        # Fila 2
        self.lbl_fecha.grid(row=2, column=0, sticky="w", padx=5, pady=5)
        self.campoFecha.grid(row=2, column=1, sticky="ew", padx=5, pady=5)

        # Fila 3
        self.lbl_direccion.grid(row=3, column=0, sticky="w", padx=5, pady=5)
        self.campoDireccion.grid(row=3, column=1, sticky="ew", padx=5, pady=5)

        # Fila 4
        self.lbl_telefono.grid(row=4, column=0, sticky="w", padx=5, pady=5)
        self.campoTelefono.grid(row=4, column=1, sticky="ew", padx=5, pady=5)

        # Fila 5
        self.lbl_correo.grid(row=5, column=0, sticky="w", padx=5, pady=5)
        self.campoCorreo.grid(row=5, column=1, sticky="ew", padx=5, pady=5)

        # Lista de contactos (columna 2, ocupa 7 filas)
        self.lista.grid(row=0, column=2, rowspan=7, sticky="ns", padx=10, pady=5)

        # Botón
        self.btn_agregar.grid(row=6, column=0, columnspan=2, sticky="ew", padx=5, pady=10)


    def mostrarDatos(self):
        a = self.campoNombres.get()
        b = self.campoApellidos.get()
        c = self.campoFecha.get()
        d = self.campoDireccion.get()
        e = self.campoTelefono.get()
        f = self.campoCorreo.get()

        if a == "" or b == "" or c == "" or d == "" or e == "" or f == "":
            messagebox.showerror("Error", "No se permiten campos vacíos")
            return

        contacto = Contacto(a, b, c, d, e, f)
        self.listaContactos.agregarContacto(contacto)

        self.lista.insert(tk.END, f"{a} - {b} - {c} - {d} - {e} - {f}")

        # Limpiar campos
        self.campoNombres.delete(0, tk.END)
        self.campoApellidos.delete(0, tk.END)
        self.campoFecha.delete(0, tk.END)
        self.campoDireccion.delete(0, tk.END)
        self.campoTelefono.delete(0, tk.END)
        self.campoCorreo.delete(0, tk.END)


if __name__ == "__main__":
    app = VentanaContacto()
    app.mainloop()
