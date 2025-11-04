# -*- coding: utf-8 -*-
"""
Created on Tue Nov  4 18:08:05 2025

@author: ivans
"""

import tkinter as tk
from tkinter import messagebox, filedialog


class LeerArchivo:
   

    @staticmethod
    def leer(ruta_archivo: str) -> str:
       
        with open(ruta_archivo, "r", encoding="utf-8") as f:
            contenido = f.read()
        return contenido



class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Lectura de archivos")
        self.root.geometry("550x400")
        self.root.resizable(False, False)

      
        frame_sup = tk.LabelFrame(root, text="Archivo a leer", padx=10, pady=10)
        frame_sup.pack(fill="x", padx=10, pady=10)

        tk.Label(frame_sup, text="Ruta del archivo:").grid(row=0, column=0, sticky="w")
        self.ent_ruta = tk.Entry(frame_sup, width=45)
        self.ent_ruta.grid(row=0, column=1, padx=5, pady=3)

       
        self.ent_ruta.insert(0, "C:/prueba.txt")

        btn_explorar = tk.Button(frame_sup, text="...", width=3, command=self.explorar)
        btn_explorar.grid(row=0, column=2, padx=3)

        btn_leer = tk.Button(frame_sup, text="Leer archivo", command=self.leer_archivo)
        btn_leer.grid(row=1, column=0, columnspan=3, pady=5)

      
        frame_texto = tk.LabelFrame(root, text="Contenido", padx=5, pady=5)
        frame_texto.pack(fill="both", expand=True, padx=10, pady=5)

        self.txt_contenido = tk.Text(frame_texto, wrap="word")
        self.txt_contenido.pack(fill="both", expand=True)

      
        self.lbl_estado = tk.Label(root, text="", fg="blue")
        self.lbl_estado.pack(pady=5)

    def explorar(self):
        ruta = filedialog.askopenfilename(
            title="Seleccionar archivo de texto",
            filetypes=[("Archivos de texto", "*.txt"), ("Todos los archivos", "*.*")]
        )
        if ruta:
            self.ent_ruta.delete(0, tk.END)
            self.ent_ruta.insert(0, ruta)

    def leer_archivo(self):
        ruta = self.ent_ruta.get().strip()
        if not ruta:
            messagebox.showerror("Error", "Debe indicar la ruta del archivo.")
            return

        try:
            contenido = LeerArchivo.leer(ruta)
          
            self.txt_contenido.delete("1.0", tk.END)
            self.txt_contenido.insert(tk.END, contenido)
            self.lbl_estado.config(text="Archivo leído correctamente.", fg="green")
        except FileNotFoundError:
            messagebox.showerror("Error", "No se pudo leer el archivo.\n(Archivo no encontrado)")
            self.lbl_estado.config(text="No se pudo leer el archivo.", fg="red")
        except OSError:
            messagebox.showerror("Error", "No se pudo leer el archivo.")
            self.lbl_estado.config(text="No se pudo leer el archivo.", fg="red")


if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
