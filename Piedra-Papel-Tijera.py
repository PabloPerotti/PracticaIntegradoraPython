import random

opciones = ["piedra", "papel", "tijera"]

def jugar_piedra_papel_tijera():
    eleccion_usuario = input("Elige una opción: piedra, papel o tijera: ").lower()
    eleccion_computadora = random.choice(opciones)

    print(f"Elegiste: {eleccion_usuario}")
    print(f"Yo elegi: {eleccion_computadora}")

    if eleccion_usuario in opciones:
        if eleccion_usuario == eleccion_computadora:
            print("¡Empatamos!")
        elif (eleccion_usuario == "piedra" and eleccion_computadora == "tijera") or \
            (eleccion_usuario == "papel" and eleccion_computadora == "piedra") or \
            (eleccion_usuario == "tijera" and eleccion_computadora == "papel"):
            print("¡Ganaste!")
        else:
            print("Te gane!!!")
    else:
        print("Opción no válida. Por favor, elige piedra, papel o tijera.")

while True:
    jugar_piedra_papel_tijera()
    otro_juego = input("¿Jugamos de nuevo? (s/n): ")
    if otro_juego.lower() != "s":
        break
