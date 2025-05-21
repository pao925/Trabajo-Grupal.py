import random

def juego_adivinar_palabra():
    palabras = ["python", "programacion", "juego", "codigo"]
    palabra_secreta = random.choice(palabras)
    letras_adivinadas = []
    intentos = 6

    print("¡Bienvenido al juego de Adivina la palabra secreta!")

    while intentos > 0:
        mostrar = [letra if letra in letras_adivinadas else "_" for letra in palabra_secreta]
        print("Palabra:", " ".join(mostrar))

        if "_" not in mostrar:
            print("🎉 ¡Felicidades! Adivinaste la palabra:", palabra_secreta)
            break

        intento = input("Adivina una letra: ").lower()

        if intento in letras_adivinadas:
            print("Ya adivinaste esa letra.")
            continue

        if intento in palabra_secreta:
            letras_adivinadas.append(intento)
            print("¡Bien! La letra está en la palabra.")
        else:
            intentos -= 1
            print("❌ Incorrecto. Intentos restantes:", intentos)

    else:
        print("😢 Has perdido. La palabra era:", palabra_secreta)

juego_adivinar_palabra()
