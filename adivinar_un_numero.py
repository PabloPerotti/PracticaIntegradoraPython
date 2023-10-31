import random

def jugar_adivina_el_numero():
    numero_secreto = random.randint(1, 10)
    intentos = 0

    print("¡Bienvenido a Adivina el Numero!")
    print("Trata de adivinar el numero que estoy pensando entre 1 y 10.")

    while True:
        intentos += 1
        intento = int(input("A ver si adivinas? tira tu adivinanza: "))

        if intento < numero_secreto:
            print("FRIO FRIO!!! Mi número es mayor. Proba de vuelta!")
        elif intento > numero_secreto:
            print("FRIO FRIO!!! Mi número es menor. ¡Proba de vuelta!")
        else:
            print(f"¡UUhhh me ganaste! Adivinaste el número en {intentos} intentos.")
            break


jugar_adivina_el_numero()
