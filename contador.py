import tkinter as tk

def incrementar():
    # Leer el valor actual, sumarle 1 y actualizar la etiqueta
    valor_actual = int(label_numero["text"])
    label_numero.config(text=str(valor_actual + 1))

# Crear ventana principal
ventana = tk.Tk()
ventana.title("Contador de visitas")
ventana.geometry("250x120")

# Visor de número (inicia en 0)
label_numero = tk.Label(ventana, text="0", font=("Arial", 32))
label_numero.pack(pady=10)

# Botón que incrementa el número
boton = tk.Button(ventana, text="Sumar 1", font=("Arial", 12), command=incrementar)
boton.pack(pady=5)

# Bucle principal de la interfaz
ventana.mainloop()
