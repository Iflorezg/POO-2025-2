import tkinter as tk
import math

def calcular():
 
    numero_str = txt_numero.get()
    try:
        valor = float(numero_str)
        if valor < 0:
            
            lbl_mensaje.config(text="El número debe ser positivo.", fg="red")
            txt_log.delete(0, tk.END)
            txt_raiz.delete(0, tk.END)
            return

   
        log_n = math.log(valor)
        raiz = math.sqrt(valor)

      
        txt_log.delete(0, tk.END)
        txt_log.insert(0, f"{log_n:.6f}")

        txt_raiz.delete(0, tk.END)
        txt_raiz.insert(0, f"{raiz:.6f}")

        lbl_mensaje.config(text="Cálculos realizados.", fg="green")

    except ValueError:
        lbl_mensaje.config(text="Ingrese un número válido.", fg="red")
        txt_log.delete(0, tk.END)
        txt_raiz.delete(0, tk.END)

def limpiar():
    txt_numero.delete(0, tk.END)
    txt_log.delete(0, tk.END)
    txt_raiz.delete(0, tk.END)
    lbl_mensaje.config(text="")


ventana = tk.Tk()
ventana.title("Cálculos Numéricos")


ventana.configure(bg="#d9d9d9")   
ventana.geometry("330x200")

lbl_numero = tk.Label(ventana, text="Numero", bg="#d9d9d9")
lbl_numero.grid(row=0, column=0, padx=10, pady=5, sticky="w")
txt_numero = tk.Entry(ventana, width=22)
txt_numero.grid(row=0, column=1, padx=10, pady=5)

lbl_log = tk.Label(ventana, text="Logaritmo Neperiano", bg="#d9d9d9")
lbl_log.grid(row=1, column=0, padx=10, pady=5, sticky="w")
txt_log = tk.Entry(ventana, width=22)
txt_log.grid(row=1, column=1, padx=10, pady=5)


lbl_raiz = tk.Label(ventana, text="Raiz Cuadrada", bg="#d9d9d9")
lbl_raiz.grid(row=2, column=0, padx=10, pady=5, sticky="w")
txt_raiz = tk.Entry(ventana, width=22)
txt_raiz.grid(row=2, column=1, padx=10, pady=5)


btn_calcular = tk.Button(ventana, text="Calcular", command=calcular, width=10)
btn_calcular.grid(row=3, column=0, padx=10, pady=10)

btn_limpiar = tk.Button(ventana, text="Limpiar", command=limpiar, width=10)
btn_limpiar.grid(row=3, column=1, padx=10, pady=10, sticky="w")


lbl_mensaje = tk.Label(ventana, text="", bg="#d9d9d9")
lbl_mensaje.grid(row=4, column=0, columnspan=2, padx=10, pady=5, sticky="w")


ventana.mainloop()
