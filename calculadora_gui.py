import tkinter as tk

# Función para agregar números a la pantalla
def presionar(valor):
    entrada.set(entrada.get() + str(valor))

# Función para calcular el resultado
def calcular():
    try:
        resultado = eval(entrada.get())
        entrada.set(resultado)
    except:
        entrada.set("Error")

# Función para limpiar la pantalla
def limpiar():
    entrada.set("")

# Crear ventana
ventana = tk.Tk()
ventana.title("Calculadora")
ventana.geometry("300x400")
ventana.resizable(False, False)

# Variable de entrada
entrada = tk.StringVar()

# Pantalla
pantalla = tk.Entry(ventana, textvariable=entrada, font=("Arial", 20), bd=10, insertwidth=2, width=14, borderwidth=4)
pantalla.grid(row=0, column=0, columnspan=4)

# Botones
botones = [
    ('7',1,0), ('8',1,1), ('9',1,2), ('/',1,3),
    ('4',2,0), ('5',2,1), ('6',2,2), ('*',2,3),
    ('1',3,0), ('2',3,1), ('3',3,2), ('-',3,3),
    ('0',4,0), ('.',4,1), ('=',4,2), ('+',4,3)
]

for (texto, fila, columna) in botones:
    if texto == "=":
        boton = tk.Button(ventana, text=texto, padx=20, pady=20, command=calcular)
    else:
        boton = tk.Button(ventana, text=texto, padx=20, pady=20, command=lambda t=texto: presionar(t))
    
    boton.grid(row=fila, column=columna)

# Botón limpiar
tk.Button(ventana, text="C", padx=20, pady=20, command=limpiar).grid(row=5, column=0, columnspan=4, sticky="we")

ventana.mainloop()