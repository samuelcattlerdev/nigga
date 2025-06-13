import json
import tkinter as tk
from tkinter import messagebox

def procesar_datos():
    try:
        LUZ = int(entry_luz.get())
        HUMEDAD = int(entry_humedad.get())
        TEMPERATURA = int(entry_temperatura.get())

        # Determine statuses
        ESTADO_LUZ = 'iluminado' if LUZ > 40 else 'oscuro'
        ESTADO_HUMEDAD = 'húmedo' if HUMEDAD > 37 else 'seco'
        if TEMPERATURA >= 30:
            TEMPERATURA_ESTADO = 'caliente'
        elif 20 <= TEMPERATURA < 30:
            TEMPERATURA_ESTADO = 'normal'
        else:
            TEMPERATURA_ESTADO = 'frío'

        # Format into a JSON object
        status = {
            'ESTADO_LUZ': ESTADO_LUZ,
            'ESTADO_HUMEDAD': ESTADO_HUMEDAD,
            'TEMPERATURA_ESTADO': TEMPERATURA_ESTADO,
        }

        # Output the JSON object
        resultado.set(json.dumps(status, ensure_ascii=False, indent=4))

    except ValueError:
        messagebox.showerror("Entrada no válida", "Por favor ingrese valores numéricos válidos.")

# Crear la ventana principal
root = tk.Tk()
root.title("Interfaz de Parámetros")

# Variables
resultado = tk.StringVar()

# Crear widgets
tk.Label(root, text="LUZ:").grid(row=0, column=0, padx=10, pady=10)
entry_luz = tk.Entry(root)
entry_luz.grid(row=0, column=1, padx=10, pady=10)

tk.Label(root, text="HUMEDAD:").grid(row=1, column=0, padx=10, pady=10)
entry_humedad = tk.Entry(root)
entry_humedad.grid(row=1, column=1, padx=10, pady=10)

tk.Label(root, text="TEMPERATURA:").grid(row=2, column=0, padx=10, pady=10)
entry_temperatura = tk.Entry(root)
entry_temperatura.grid(row=2, column=1, padx=10, pady=10)

tk.Button(root, text="Procesar", command=procesar_datos).grid(row=3, column=0, columnspan=2, pady=10)
tk.Label(root, textvariable=resultado).grid(row=4, column=0, columnspan=2, padx=10, pady=10)

# Ejecutar la aplicación
root.mainloop()
