#se creará un juego, donde el usuario tiene que adivinar ciertas palabras colocando letras al azar. Se usará el modulo random.
import random

def juego_adivinar_palabra():
    palabras = ["python", "programacion", "juego", "codigo"] #listas de palabras para el juego
    palabra_secreta = random.choice(palabras)
    letras_adivinadas = []
    intentos = 6 #números de intentos permitidos

    print("¡Bienvenido al juego de Adivina la palabra secreta!")

    #bucle principal del juego
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
            #dismuir el número de intentos con el mensaje de "incorecto"
            intentos -= 1
            print("❌ Incorrecto. Intentos restantes:", intentos)

    else:
        print("😢 Has perdido. La palabra era:", palabra_secreta)

juego_adivinar_palabra()
