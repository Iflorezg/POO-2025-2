# -*- coding: utf-8 -*-
import tkinter as tk
from tkinter import messagebox, filedialog, ttk


class TipoCargo:
    DIRECTIVO = "DIRECTIVO"
    ESTRATÉGICO = "ESTRATÉGICO"
    OPERATIVO = "OPERATIVO"


class TipoGénero:
    MASCULINO = "MASCULINO"
    FEMENINO = "FEMENINO"


class Empleado:
    def __init__(self, nombre, apellidos, cargo, género, salarioDía, díasTrabajados,
                 otrosIngresos, pagosSalud, aportePensiones):
        self.nombre = nombre
        self.apellidos = apellidos
        self.salarioDía = salarioDía
        self.otrosIngresos = otrosIngresos
        self.pagosSalud = pagosSalud
        self.aportePensiones = aportePensiones
        self.díasTrabajados = díasTrabajados
        self.cargo = cargo
        self.género = género

    def getNombre(self):
        return self.nombre

    def getApellidos(self):
        return self.apellidos

    def getCargo(self):
        return self.cargo

    def getGénero(self):
        return self.género

    def getSalarioDía(self):
        return self.salarioDía

    def getDíasTrabajados(self):
        return self.díasTrabajados

    def getOtrosIngresos(self):
        return self.otrosIngresos

    def getPagosSalud(self):
        return self.pagosSalud

    def getAportePensiones(self):
        return self.aportePensiones

    def calcularNómina(self):
        return (self.salarioDía * self.díasTrabajados) + self.otrosIngresos - self.pagosSalud - self.aportePensiones


class ListaEmpleados:
    def __init__(self):
        self.lista = []
        self.totalNómina = 0.0

    def agregarEmpleado(self, a):
        self.lista.append(a)

    def calcularTotalNómina(self):
        for i in range(len(self.lista)):
            e = self.lista[i]
            self.totalNómina = self.totalNómina + e.calcularNómina()
        return self.totalNómina

    def obtenerMatriz(self):
        datos = [["", "", ""] for _ in range(len(self.lista))]
        for i in range(len(self.lista)):
            e = self.lista[i]
            datos[i][0] = e.getNombre()
            datos[i][1] = e.getApellidos()
            datos[i][2] = str(e.calcularNómina())
            self.totalNómina = self.totalNómina + e.calcularNómina()
        return datos

    def convertirTexto(self):
        texto = ""
        for i in range(len(self.lista)):
            e = self.lista[i]
            texto = (
                texto
                + "Nombre = " + e.getNombre() + "\n"
                + "Apellidos = " + e.getApellidos() + "\n"
                + "Cargo = " + str(e.getCargo()) + "\n"
                + "Género = " + str(e.getGénero()) + "\n"
                + "Salario = $" + str(e.getSalarioDía()) + "\n"
                + "Días trabajados = " + str(e.getDíasTrabajados()) + "\n"
                + "Otros ingresos = $" + str(e.getOtrosIngresos()) + "\n"
                + "Pagos saludo = $" + str(e.getPagosSalud()) + "\n"
                + "Aportes pensiones = $" + str(e.getAportePensiones()) + "\n"
                + "---------\n"
            )
        texto = texto + "Total nómina = $" + "{:.2f}".format(self.calcularTotalNómina())
        return texto


class VentanaAgregarEmpleado(tk.Toplevel):
    def __init__(self, lista, master=None):
        super().__init__(master)
        self.lista = lista
        self.contenedor = None
        self.nombre = None
        self.apellidos = None
        self.cargo = None
        self.salarioDía = None
        self.númeroDías = None
        self.género = None
        self.otrosIngresos = None
        self.aportesSalud = None
        self.pensiones = None
        self.campoNombre = None
        self.campoApellidos = None
        self.campoSalarioDía = None
        self.campoOtrosIngresos = None
        self.campoAportesSalud = None
        self.campoPensiones = None
        self.grupoGénero = None
        self.masculino = None
        self.femenino = None
        self.campoCargo = None
        self.campoNúmeroDías = None
        self.agregar = None
        self.limpiar = None
        self.inicio()
        self.title("Agregar Empleado")
        self.geometry("300x400")
        self.resizable(False, False)

    def inicio(self):
        self.contenedor = tk.Frame(self)
        self.contenedor.place(x=0, y=0, relwidth=1, relheight=1)

        self.nombre = tk.Label(self.contenedor, text="Nombre:")
        self.nombre.place(x=20, y=20, width=135, height=23)
        self.campoNombre = tk.Entry(self.contenedor)
        self.campoNombre.place(x=160, y=20, width=100, height=23)

        self.apellidos = tk.Label(self.contenedor, text="Apellidos:")
        self.apellidos.place(x=20, y=50, width=135, height=23)
        self.campoApellidos = tk.Entry(self.contenedor)
        self.campoApellidos.place(x=160, y=50, width=100, height=23)

        self.cargo = tk.Label(self.contenedor, text="Cargo:")
        self.cargo.place(x=20, y=80, width=135, height=23)
        self.campoCargo = ttk.Combobox(self.contenedor, state="readonly",
                                       values=["Directivo", "Estratégico", "Operativo"])
        self.campoCargo.place(x=160, y=80, width=100, height=23)
        self.campoCargo.current(0)

        self.género = tk.Label(self.contenedor, text="Género:")
        self.género.place(x=20, y=110, width=100, height=30)
        self.grupoGénero = tk.StringVar(value="Masculino")
        self.masculino = tk.Radiobutton(self.contenedor, text="Masculino",
                                        variable=self.grupoGénero, value="Masculino")
        self.masculino.place(x=160, y=110, width=100, height=30)
        self.femenino = tk.Radiobutton(self.contenedor, text="Femenino",
                                       variable=self.grupoGénero, value="Femenino")
        self.femenino.place(x=160, y=140, width=100, height=30)

        self.salarioDía = tk.Label(self.contenedor, text="Salario por día:")
        self.salarioDía.place(x=20, y=170, width=135, height=23)
        self.campoSalarioDía = tk.Entry(self.contenedor)
        self.campoSalarioDía.place(x=160, y=170, width=100, height=23)

        self.númeroDías = tk.Label(self.contenedor, text="Días trabajados al mes:")
        self.númeroDías.place(x=20, y=200, width=135, height=23)
        self.campoNúmeroDías = tk.Spinbox(self.contenedor, from_=1, to=31)
        self.campoNúmeroDías.delete(0, tk.END)
        self.campoNúmeroDías.insert(0, "30")
        self.campoNúmeroDías.place(x=160, y=200, width=40, height=23)

        self.otrosIngresos = tk.Label(self.contenedor, text="Otros ingresos:")
        self.otrosIngresos.place(x=20, y=230, width=135, height=23)
        self.campoOtrosIngresos = tk.Entry(self.contenedor)
        self.campoOtrosIngresos.place(x=160, y=230, width=100, height=23)

        self.aportesSalud = tk.Label(self.contenedor, text="Pagos por salud:")
        self.aportesSalud.place(x=20, y=260, width=135, height=23)
        self.campoAportesSalud = tk.Entry(self.contenedor)
        self.campoAportesSalud.place(x=160, y=260, width=100, height=23)

        self.pensiones = tk.Label(self.contenedor, text="Aportes pensiones:")
        self.pensiones.place(x=20, y=290, width=135, height=23)
        self.campoPensiones = tk.Entry(self.contenedor)
        self.campoPensiones.place(x=160, y=290, width=100, height=23)

        self.agregar = tk.Button(self.contenedor, text="Agregar",
                                 command=self._agregar_action)
        self.agregar.place(x=20, y=320, width=100, height=23)

        self.limpiar = tk.Button(self.contenedor, text="Borrar",
                                 command=self._limpiar_action)
        self.limpiar.place(x=160, y=320, width=80, height=23)

    def limpiarCampos(self):
        self.campoNombre.delete(0, tk.END)
        self.campoApellidos.delete(0, tk.END)
        self.campoSalarioDía.delete(0, tk.END)
        self.campoNúmeroDías.delete(0, tk.END)
        self.campoNúmeroDías.insert(0, "0")
        self.campoOtrosIngresos.delete(0, tk.END)
        self.campoAportesSalud.delete(0, tk.END)
        self.campoPensiones.delete(0, tk.END)

    def _agregar_action(self):
        self.añadirEmpleado()

    def _limpiar_action(self):
        self.limpiarCampos()

    def añadirEmpleado(self):
        if self.campoCargo.get() == "Directivo":
            tipoC = TipoCargo.DIRECTIVO
        elif self.campoCargo.get() == "Estratégico":
            tipoC = TipoCargo.ESTRATÉGICO
        else:
            tipoC = TipoCargo.OPERATIVO

        if self.grupoGénero.get() == "Masculino":
            tipoG = TipoGénero.MASCULINO
        else:
            tipoG = TipoGénero.FEMENINO

        try:
            valor1 = self.campoNombre.get()
            valor2 = self.campoApellidos.get()
            valor3 = float(self.campoSalarioDía.get())
            valor4 = int(self.campoNúmeroDías.get())
            valor5 = float(self.campoOtrosIngresos.get())
            valor6 = float(self.campoAportesSalud.get())
            valor7 = float(self.campoPensiones.get())
            e = Empleado(valor1, valor2, tipoC, tipoG,
                         valor3, valor4, valor5, valor6, valor7)
            self.lista.agregarEmpleado(e)
            messagebox.showinfo("Mensaje", "El empleado ha sido agregado", parent=self)
            self.limpiarCampos()
        except Exception:
            messagebox.showerror("Error", "Campo nulo o error en formato de numero", parent=self)


class VentanaNómina(tk.Toplevel):
    def __init__(self, lista, master=None):
        super().__init__(master)
        self.lista = lista
        self.contenedor = None
        self.empleados = None
        self.nómina = None
        self.tabla = None
        self.inicio()
        self.title("Nómina de Empleados")
        self.geometry("350x250")
        self.resizable(False, False)

    def inicio(self):
        self.contenedor = tk.Frame(self)
        self.contenedor.place(x=0, y=0, relwidth=1, relheight=1)

        self.empleados = tk.Label(self.contenedor, text="Lista de empleados:")
        self.empleados.place(x=20, y=10, width=135, height=23)

        datos = self.lista.obtenerMatriz()
        titulos = ["NOMBRE", "APELLIDOS", "SUELDO"]

        self.tabla = ttk.Treeview(self.contenedor, columns=("c1", "c2", "c3"), show="headings")
        self.tabla.heading("c1", text=titulos[0])
        self.tabla.heading("c2", text=titulos[1])
        self.tabla.heading("c3", text=titulos[2])
        self.tabla.column("c1", width=100)
        self.tabla.column("c2", width=120)
        self.tabla.column("c3", width=80)
        for fila in datos:
            self.tabla.insert("", tk.END, values=fila)
        self.tabla.place(x=20, y=50, width=310, height=100)

        self.nómina = tk.Label(
            self.contenedor,
            text="Total nómina mensual = $ " + "{:.2f}".format(self.lista.totalNómina)
        )
        self.nómina.place(x=20, y=160, width=250, height=23)


class VentanaPrincipal(tk.Tk):
    def __init__(self):
        super().__init__()
        self.contenedor = None
        self.empleados = ListaEmpleados()
        self.barraMenu = None
        self.menuOpciones = None
        self.itemMenu1 = None
        self.itemMenu2 = None
        self.itemMenu3 = None
        self.inicio()
        self.title("Nómina")
        self.geometry("280x380")
        self.resizable(False, False)

    def inicio(self):
        self.contenedor = tk.Frame(self)
        self.contenedor.place(x=0, y=0, relwidth=1, relheight=1)

        self.barraMenu = tk.Menu(self)
        self.menuOpciones = tk.Menu(self.barraMenu, tearoff=0)

        self.menuOpciones.add_command(label="Agregar empleado", command=self._itemMenu1_action)
        self.menuOpciones.add_command(label="Calcular nómina", command=self._itemMenu2_action)
        self.menuOpciones.add_separator()
        self.menuOpciones.add_command(label="Guardar archivo", command=self._itemMenu3_action)

        self.barraMenu.add_cascade(label="Menú", menu=self.menuOpciones)
        self.config(menu=self.barraMenu)

    def _itemMenu1_action(self):
        ventanaAgregar = VentanaAgregarEmpleado(self.empleados, self)
        ventanaAgregar.grab_set()

    def _itemMenu2_action(self):
        ventanaNómina = VentanaNómina(self.empleados, self)
        ventanaNómina.grab_set()

    def _itemMenu3_action(self):
        directorioElegido = filedialog.askdirectory(parent=self)
        if directorioElegido:
            try:
                contenido = self.empleados.convertirTexto()
                import os
                ruta = os.path.join(directorioElegido, "Nómina.txt")
                with open(ruta, "w", encoding="utf-8") as file:
                    file.write(contenido)
                texto = "El archivo de la nómina Nómina.txt se ha creado en " + directorioElegido
                messagebox.showinfo("Mensaje", texto, parent=self)
            except Exception as e:
                print(e)


if __name__ == "__main__":
    miVentanaPrincipal = VentanaPrincipal()
    miVentanaPrincipal.mainloop()
