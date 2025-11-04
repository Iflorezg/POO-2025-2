# -*- coding: utf-8 -*-
"""
Created on Tue Nov  4 17:27:54 2025

@author: ivans
"""

import tkinter as tk
from tkinter import messagebox



class Programador:
   
    def __init__(self, nombre: str, apellidos: str):
        self.nombre = nombre
        self.apellidos = apellidos


class EquipoMaratonProgramacion:
   
    def __init__(self, nombre_equipo: str, universidad: str, lenguaje_programacion: str):
        self.nombre_equipo = nombre_equipo
        self.universidad = universidad
        self.lenguaje_programacion = lenguaje_programacion
        self.programadores = []
        self.tamano_equipo = 0

    def esta_lleno(self) -> bool:
        return self.tamano_equipo == 3  # como en el libro: mínimo 2, máximo 3

    @staticmethod
    def validar_campo(campo: str):
      
        for c in campo:
            if c.isdigit():
                raise ValueError("El nombre no puede tener dígitos.")
        if len(campo) > 20:
            raise ValueError("La longitud no debe ser superior a 20 caracteres.")

    def anadir(self, programador: Programador):
      
        if self.esta_lleno():
            raise ValueError("El equipo está completo. No se pudo agregar programador.")
        self.programadores.append(programador)
        self.tamano_equipo += 1



class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Equipo Maratón de Programación")
        self.root.geometry("460x420")
        self.root.resizable(False, False)

       
        frame_equipo = tk.LabelFrame(root, text="Datos del equipo", padx=10, pady=10)
        frame_equipo.pack(fill="x", padx=10, pady=10)

        tk.Label(frame_equipo, text="Nombre del equipo:").grid(row=0, column=0, sticky="w")
        tk.Label(frame_equipo, text="Universidad:").grid(row=1, column=0, sticky="w")
        tk.Label(frame_equipo, text="Lenguaje:").grid(row=2, column=0, sticky="w")

        self.ent_nombre_equipo = tk.Entry(frame_equipo, width=30)
        self.ent_universidad = tk.Entry(frame_equipo, width=30)
        self.ent_lenguaje = tk.Entry(frame_equipo, width=30)

        self.ent_nombre_equipo.grid(row=0, column=1, padx=5, pady=3)
        self.ent_universidad.grid(row=1, column=1, padx=5, pady=3)
        self.ent_lenguaje.grid(row=2, column=1, padx=5, pady=3)

        btn_crear = tk.Button(frame_equipo, text="Crear equipo", command=self.crear_equipo)
        btn_crear.grid(row=3, column=0, columnspan=2, pady=5)

        
        frame_prog = tk.LabelFrame(root, text="Agregar programadores", padx=10, pady=10)
        frame_prog.pack(fill="x", padx=10, pady=10)

        tk.Label(frame_prog, text="Nombre:").grid(row=0, column=0, sticky="w")
        tk.Label(frame_prog, text="Apellidos:").grid(row=1, column=0, sticky="w")

        self.ent_nombre_prog = tk.Entry(frame_prog, width=25)
        self.ent_apellidos_prog = tk.Entry(frame_prog, width=25)

        self.ent_nombre_prog.grid(row=0, column=1, padx=5, pady=3)
        self.ent_apellidos_prog.grid(row=1, column=1, padx=5, pady=3)

        btn_agregar = tk.Button(frame_prog, text="Añadir programador", command=self.agregar_programador)
        btn_agregar.grid(row=2, column=0, columnspan=2, pady=5)

       
        frame_lista = tk.LabelFrame(root, text="Programadores del equipo", padx=10, pady=10)
        frame_lista.pack(fill="both", expand=True, padx=10, pady=10)

        self.lista_prog = tk.Listbox(frame_lista, width=50, height=6)
        self.lista_prog.pack(side="left", fill="both", expand=True)

        self.lbl_estado = tk.Label(root, text="", fg="blue")
        self.lbl_estado.pack(pady=5)

      
        self.equipo = None

    def crear_equipo(self):
        nombre = self.ent_nombre_equipo.get().strip()
        uni = self.ent_universidad.get().strip()
        leng = self.ent_lenguaje.get().strip()

        if not nombre or not uni or not leng:
            messagebox.showerror("Error", "Debe llenar todos los datos del equipo.")
            return

        
        self.equipo = EquipoMaratonProgramacion(nombre, uni, leng)
        self.lista_prog.delete(0, tk.END)
        self.lbl_estado.config(text="Equipo creado. Ahora agregue los 3 programadores.")
        messagebox.showinfo("Equipo", "Equipo creado correctamente.")

    def agregar_programador(self):
        if self.equipo is None:
            messagebox.showwarning("Sin equipo", "Primero cree el equipo.")
            return

        nombre = self.ent_nombre_prog.get().strip()
        apellidos = self.ent_apellidos_prog.get().strip()

        try:
         
            EquipoMaratonProgramacion.validar_campo(nombre)
            EquipoMaratonProgramacion.validar_campo(apellidos)

            prog = Programador(nombre, apellidos)
            self.equipo.anadir(prog)

           
            self.lista_prog.insert(tk.END, f"{nombre} {apellidos}")
            self.ent_nombre_prog.delete(0, tk.END)
            self.ent_apellidos_prog.delete(0, tk.END)

            if self.equipo.esta_lleno():
                self.lbl_estado.config(text="El equipo está completo.", fg="green")
                messagebox.showinfo("Equipo completo", "El equipo está completo (3 programadores).")
            else:
                faltan = 3 - self.equipo.tamano_equipo
                self.lbl_estado.config(text=f"Programador agregado. Faltan {faltan}.", fg="blue")

        except ValueError as e:
            messagebox.showerror("Validación", str(e))


if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
