# -*- coding: utf-8 -*-
import tkinter as tk
from tkinter import messagebox, simpledialog
from datetime import datetime


class Huesped:
    def __init__(self, nombres, apellidos, documentoIdentidad):
        self.nombres = nombres
        self.apellidos = apellidos
        self.documentoIdentidad = documentoIdentidad
        self.fechaIngreso = None
        self.fechaSalida = None

    def setFechaIngreso(self, fecha):
        self.fechaIngreso = fecha

    def setFechaSalida(self, fecha):
        self.fechaSalida = fecha

    def getFechaIngreso(self):
        return self.fechaIngreso

    def obtenerDiasAlojamiento(self):
        dias = (self.fechaSalida - self.fechaIngreso).days
        return dias


class Habitacion:
    def __init__(self, numeroHabitacion, disponible, precioDia):
        self.numeroHabitacion = numeroHabitacion
        self.disponible = disponible
        self.precioDia = precioDia
        self.huesped = None

    def getNumeroHabitacion(self):
        return self.numeroHabitacion

    def getDisponible(self):
        return self.disponible

    def getPrecioDia(self):
        return self.precioDia

    def getHuesped(self):
        return self.huesped

    def setHuesped(self, huesped):
        self.huesped = huesped

    def setDisponible(self, disponible):
        self.disponible = disponible


class Hotel:
    def __init__(self):
        self.listaHabitaciones = []
        self.listaHabitaciones.append(Habitacion(1, True, 120000))
        self.listaHabitaciones.append(Habitacion(2, True, 120000))
        self.listaHabitaciones.append(Habitacion(3, True, 120000))
        self.listaHabitaciones.append(Habitacion(4, True, 120000))
        self.listaHabitaciones.append(Habitacion(5, True, 120000))
        self.listaHabitaciones.append(Habitacion(6, True, 160000))
        self.listaHabitaciones.append(Habitacion(7, True, 160000))
        self.listaHabitaciones.append(Habitacion(8, True, 160000))
        self.listaHabitaciones.append(Habitacion(9, True, 160000))
        self.listaHabitaciones.append(Habitacion(10, True, 160000))

    def buscarFechaIngresoHabitacion(self, numero):
        for hab in self.listaHabitaciones:
            if hab.getNumeroHabitacion() == numero and hab.getHuesped() is not None:
                fecha = hab.getHuesped().getFechaIngreso()
                if fecha is None:
                    return ""
                return fecha.strftime("%Y/%m/%d")
        return ""

    def buscarHabitacionOcupada(self, numero):
        for hab in self.listaHabitaciones:
            if hab.getNumeroHabitacion() == numero and not hab.getDisponible():
                return True
        return False


class VentanaHabitaciones(tk.Toplevel):
    def __init__(self, hotel, master=None):
        super().__init__(master)
        self.hotel = hotel
        self.title("Habitaciones")
        self.geometry("760x260")
        self.resizable(False, False)
        self.contenedor = tk.Frame(self)
        self.contenedor.place(x=0, y=0, relwidth=1, relheight=1)
        self.crearComponentes()

    def crearComponentes(self):
        etiquetas_hab = []
        etiquetas_disp = []
        posiciones = [
            (20, 30), (160, 30), (300, 30), (440, 30), (580, 30),
            (20, 120), (160, 120), (300, 120), (440, 120), (580, 120)
        ]
        pos_disp = [
            (20, 50), (160, 50), (300, 50), (440, 50), (580, 50),
            (20, 140), (160, 140), (300, 140), (440, 140), (580, 140)
        ]
        for i, hab in enumerate(self.hotel.listaHabitaciones):
            l = tk.Label(self.contenedor, text=f"Habitación {hab.getNumeroHabitacion()}")
            l.place(x=posiciones[i][0], y=posiciones[i][1], width=130, height=23)
            etiquetas_hab.append(l)
            ld = tk.Label(self.contenedor, text="Disponible" if hab.getDisponible() else "No disponible")
            ld.place(x=pos_disp[i][0], y=pos_disp[i][1], width=100, height=23)
            etiquetas_disp.append(ld)

        self.habitacionSeleccionada = tk.Label(self.contenedor, text="Habitación a reservar:")
        self.habitacionSeleccionada.place(x=250, y=180, width=135, height=23)

        self.campoHabitacionSeleccionada = tk.Spinbox(self.contenedor, from_=1, to=10)
        self.campoHabitacionSeleccionada.place(x=380, y=180, width=40, height=23)

        self.botonAceptar = tk.Button(self.contenedor, text="Aceptar", command=self.aceptar)
        self.botonAceptar.place(x=500, y=180, width=100, height=23)

    def aceptar(self):
        numero = int(self.campoHabitacionSeleccionada.get())
        if not self.hotel.buscarHabitacionOcupada(numero):
            ventanaIngreso = VentanaIngreso(self.hotel, numero, self.master)
            self.destroy()
        else:
            messagebox.showinfo("Mensaje", "La habitación está ocupada", parent=self)


class VentanaIngreso(tk.Toplevel):
    def __init__(self, hotel, numeroHabitacionReservada, master=None):
        super().__init__(master)
        self.hotel = hotel
        self.numeroHabitacionReservada = numeroHabitacionReservada
        self.title("Ingreso")
        self.geometry("290x250")
        self.resizable(False, False)
        self.contenedor = tk.Frame(self)
        self.contenedor.pack(fill="both", expand=True)
        self.crearComponentes()

    def crearComponentes(self):
        c = tk.GridBagConstraints if False else None
        self.contenedor.grid_columnconfigure(0, weight=1)
        self.contenedor.grid_columnconfigure(1, weight=1)

        self.lblHabitacion = tk.Label(self.contenedor, text=f"Habitación: {self.numeroHabitacionReservada}")
        self.lblHabitacion.grid(row=0, column=0, padx=3, pady=3, sticky="w")

        self.lblFechaIngreso = tk.Label(self.contenedor, text="Fecha (aaaa-mm-dd):")
        self.lblFechaIngreso.grid(row=1, column=0, padx=3, pady=3, sticky="w")
        self.campoFechaIngreso = tk.Entry(self.contenedor)
        self.campoFechaIngreso.grid(row=1, column=1, padx=3, pady=3, sticky="we")

        self.lblHuesped = tk.Label(self.contenedor, text="Huésped")
        self.lblHuesped.grid(row=2, column=0, padx=3, pady=3, sticky="w")

        self.lblNombre = tk.Label(self.contenedor, text="Nombre:")
        self.lblNombre.grid(row=3, column=0, padx=3, pady=3, sticky="w")
        self.campoNombre = tk.Entry(self.contenedor)
        self.campoNombre.grid(row=3, column=1, padx=3, pady=3, sticky="we")

        self.lblApellidos = tk.Label(self.contenedor, text="Apellidos:")
        self.lblApellidos.grid(row=4, column=0, padx=3, pady=3, sticky="w")
        self.campoApellidos = tk.Entry(self.contenedor)
        self.campoApellidos.grid(row=4, column=1, padx=3, pady=3, sticky="we")

        self.lblDoc = tk.Label(self.contenedor, text="Doc. Identidad:")
        self.lblDoc.grid(row=5, column=0, padx=3, pady=3, sticky="w")
        self.campoDocumento = tk.Entry(self.contenedor)
        self.campoDocumento.grid(row=5, column=1, padx=3, pady=3, sticky="we")

        self.botonAceptar = tk.Button(self.contenedor, text="Aceptar", command=self.aceptar)
        self.botonAceptar.grid(row=6, column=0, padx=3, pady=3, sticky="we")

        self.botonCancelar = tk.Button(self.contenedor, text="Cancelar", command=self.destroy)
        self.botonCancelar.grid(row=6, column=1, padx=3, pady=3, sticky="we")

    def aceptar(self):
        for hab in self.hotel.listaHabitaciones:
            if hab.getNumeroHabitacion() == self.numeroHabitacionReservada:
                try:
                    fechaIngresada = self.campoFechaIngreso.get()
                    fecha = datetime.strptime(fechaIngresada, "%Y-%m-%d").date()
                    nombres = self.campoNombre.get()
                    apellidos = self.campoApellidos.get()
                    documento = int(self.campoDocumento.get())
                    huesped = Huesped(nombres, apellidos, documento)
                    huesped.setFechaIngreso(fecha)
                    hab.setHuesped(huesped)
                    hab.setDisponible(False)
                    messagebox.showinfo("Mensaje", "El huésped ha sido registrado", parent=self)
                    self.destroy()
                    return
                except ValueError:
                    messagebox.showerror("Mensaje", "La fecha no está en el formato solicitado o datos inválidos",
                                         parent=self)
                    return
                except Exception:
                    messagebox.showerror("Error", "Campo nulo o error en formato de numero", parent=self)
                    return


class VentanaSalida(tk.Toplevel):
    def __init__(self, hotel, numero, master=None):
        super().__init__(master)
        self.hotel = hotel
        self.numeroHabitacion = numero
        self.posicionHabitacion = -1
        self.habitacionOcupada = None
        self.title("Salida huéspedes")
        self.geometry("260x260")
        self.resizable(False, False)
        self.contenedor = tk.Frame(self)
        self.contenedor.pack(fill="both", expand=True)
        self.crearComponentes()

    def crearComponentes(self):
        self.contenedor.grid_columnconfigure(0, weight=1)
        self.habitacion = tk.Label(self.contenedor, text=f"Habitación: {self.numeroHabitacion}")
        self.habitacion.grid(row=0, column=0, padx=3, pady=3, sticky="w")

        fecha = self.hotel.buscarFechaIngresoHabitacion(self.numeroHabitacion)
        self.fechaIngreso = tk.Label(self.contenedor, text=f"Fecha de ingreso: {fecha}")
        self.fechaIngreso.grid(row=1, column=0, padx=3, pady=3, sticky="w")

        self.lblFechaSalida = tk.Label(self.contenedor, text="Fecha de salida (aaaa-mm-dd):")
        self.lblFechaSalida.grid(row=2, column=0, padx=3, pady=3, sticky="w")
        self.campoFechaSalida = tk.Entry(self.contenedor)
        self.campoFechaSalida.grid(row=3, column=0, padx=3, pady=3, sticky="we")

        self.botonCalcular = tk.Button(self.contenedor, text="Calcular", command=self.calcular)
        self.botonCalcular.grid(row=4, column=0, padx=3, pady=3, sticky="we")

        self.cantidadDias = tk.Label(self.contenedor, text="Cantidad de días: ")
        self.cantidadDias.grid(row=5, column=0, padx=3, pady=3, sticky="w")

        self.totalPago = tk.Label(self.contenedor, text="Total: $")
        self.totalPago.grid(row=6, column=0, padx=3, pady=3, sticky="w")

        self.botonRegistrar = tk.Button(self.contenedor, text="Registrar salida", command=self.registrarSalida)
        self.botonRegistrar.grid(row=7, column=0, padx=3, pady=3, sticky="we")
        self.botonRegistrar.config(state="disabled")

    def calcular(self):
        fechaS = self.campoFechaSalida.get()
        try:
            fecha2 = datetime.strptime(fechaS, "%Y-%m-%d").date()
        except ValueError:
            messagebox.showerror("Mensaje", "La fecha no está en el formato solicitado", parent=self)
            return

        for i, hab in enumerate(self.hotel.listaHabitaciones):
            if hab.getNumeroHabitacion() == self.numeroHabitacion:
                self.habitacionOcupada = hab
                self.posicionHabitacion = i
                fecha1 = hab.getHuesped().getFechaIngreso()
                if fecha1 is None:
                    messagebox.showerror("Mensaje", "La habitación no tiene fecha de ingreso", parent=self)
                    return
                if fecha1 >= fecha2:
                    messagebox.showerror("Mensaje", "La fecha de salida es menor que la de ingreso", parent=self)
                    return
                hab.getHuesped().setFechaSalida(fecha2)
                cantidad = hab.getHuesped().obtenerDiasAlojamiento()
                self.cantidadDias.config(text=f"Cantidad de días: {cantidad}")
                valor = cantidad * hab.getPrecioDia()
                self.totalPago.config(text=f"Total: ${valor}")
                self.botonRegistrar.config(state="normal")
                return

    def registrarSalida(self):
        self.habitacionOcupada.setHuesped(None)
        self.habitacionOcupada.setDisponible(True)
        self.hotel.listaHabitaciones[self.posicionHabitacion] = self.habitacionOcupada
        messagebox.showinfo("Mensaje", "Se ha registrado la salida del huésped", parent=self)
        self.destroy()


class VentanaPrincipal(tk.Tk):
    def __init__(self, hotel):
        super().__init__()
        self.hotel = hotel
        self.title("Hotel")
        self.geometry("280x380")
        self.resizable(False, False)
        self.contenedor = tk.Frame(self)
        self.contenedor.place(x=0, y=0, relwidth=1, relheight=1)
        self.crearMenu()

    def crearMenu(self):
        self.barraMenu = tk.Menu(self)
        self.menuOpciones = tk.Menu(self.barraMenu, tearoff=0)
        self.menuOpciones.add_command(label="Consultar habitaciones", command=self.abrirHabitaciones)
        self.menuOpciones.add_command(label="Salida de huéspedes", command=self.salidaHuesped)
        self.barraMenu.add_cascade(label="Menú", menu=self.menuOpciones)
        self.config(menu=self.barraMenu)

    def abrirHabitaciones(self):
        VentanaHabitaciones(self.hotel, self)

    def salidaHuesped(self):
        try:
            numero = simpledialog.askinteger("Salida de huéspedes", "Ingrese número de habitación",
                                             parent=self, minvalue=1, maxvalue=10)
            if numero is None:
                return
            if numero < 1 or numero > 10:
                messagebox.showinfo("Mensaje", "El número de habitación debe estar entre 1 y 10", parent=self)
            elif self.hotel.buscarHabitacionOcupada(numero):
                VentanaSalida(self.hotel, numero, self)
            else:
                messagebox.showinfo("Mensaje", "La habitación ingresada no ha sido ocupada", parent=self)
        except Exception:
            messagebox.showerror("Error", "Campo nulo o error en formato de numero", parent=self)


if __name__ == "__main__":
    hotel = Hotel()
    app = VentanaPrincipal(hotel)
    app.mainloop()
