import random

def jugar_adivina_el_numero():
    numero_secreto = random.randint(1, 100)
    intentos = 0

    print("¡Bienvenido a Adivina el Número!")
    print("Estoy pensando en un número entre 1 y 100.")

    while True:
        intentos += 1
        intento = int(input("Introduce tu adivinanza: "))

        if intento < numero_secreto:
            print("Mi número es mayor. ¡Inténtalo de nuevo!")
        elif intento > numero_secreto:
            print("Mi número es menor. ¡Inténtalo de nuevo!")
        else:
            print(f"¡Felicidades! Adivinaste el número en {intentos} intentos.")
            break


jugar_adivina_el_numero()
