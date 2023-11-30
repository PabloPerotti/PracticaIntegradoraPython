import tkinter as tk
import random

opciones = ["piedra", "papel", "tijera"]

def jugar(opcion_usuario):
    opcion_computadora = random.choice(opciones)

    if opcion_usuario == opcion_computadora:
        resultado = "Empate"
    elif (
        (opcion_usuario == "Piedra" and opcion_computadora == "Tijera") or
        (opcion_usuario == "Papel" and opcion_computadora == "Piedra") or
        (opcion_usuario == "Tijera" and opcion_computadora == "Papel")
    ):
        resultado = "¡Ganaste!"
    else:
        resultado = "¡Perdiste!"

    result.config(text=f"Computadora eligió {opcion_computadora}. {resultado}")

ventana = tk.Tk()
ventana.title("Piedra, Papel, Tijera")
ventana.geometry("400x200+400+100")

instrucciones = tk.Label(ventana, text="Elige una opción:")
instrucciones.pack()

piedra_boton = tk.Button(ventana, text="Piedra", command=lambda: jugar("Piedra"))
papel_boton = tk.Button(ventana, text="Papel", command=lambda: jugar("Papel"))
tijera_boton = tk.Button(ventana, text="Tijera", command=lambda: jugar("Tijera"))


piedra_boton.pack()
papel_boton.pack()
tijera_boton.pack() 

result = tk.Label(ventana, text="")
result.pack()
ventana.mainloop()
