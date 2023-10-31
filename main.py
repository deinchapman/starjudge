
def main():
    name = input("Muchas gracias venir, ¿Me puedes dar tu Nombre por favor?: ")
    lover = input(f"Hola, {name}. Me puedes llamar lo más te guste, ¿Cómo te gustaría llamarme?: ")
    answer = input(f"{lover}: ¿Te puedo hacer una pregunta? Solo dime que si o no por favor: ")

    if answer == "no":
        print(f"{lover}: Lo siento mucho, no te volvere a molestar.\nFinal neutral 1: No volveras a ser molestado.")
        return
    elif answer != "si":
        print(f"{lover}: Mejor olvidalo, no es nada.\nFinal neutral 2: Al final no era nada.")
        return

    answer = input(f"{lover}: Me da pena pero... ¿podemos ir a comer un helado juntos? *Puedes escuchar entre murmuros como solo espera que le responde o que ¨si¨ o que ¨no¨: ")

    if answer == "no":
        print(f"{lover}: Ou... esta bien, siento mucho las molestias.\nFinal malo: Te terminaste quedando solo e insatisfecho.")
        return
    elif answer != "si":
        print(f"{lover}: Uhm... pensandolo mejor, creo que no tengo ganas... mejor otro dia")
        print("Final indeciso: No eres tu, tampoco es la otra persona, algunas veces simplemente no sentimos la confianza de dar ese proximo paso en la relacion.")
        return

    print(f"{lover}: Oh ¿En serio? ¡Entonces no hay tiempo que perder!")
    answer = input("Las estrellas del destino te juzgan ¿Genuinamente quieres pasar tiempo con esta persona? *Sientes que solo puedes responder ¨si¨ o ¨no¨ a esta pregunta: ")

    if answer == "no":
        print("Final hipócrita: A pesar de que en un principio respondiste que si; era evidente para la otra persona que realmente no querias estar con ella, y antes de que te dieras cuenta, simplemente se despidieron para nunca volverse a ver.")
        return
    elif answer != "si":
        print("Final del mas allá: Independientemente de tu respuesta, te distrajiste demasiado hablando con seres que van mas allá de tu comprensión, y terminaste siendo atropellado por un camión, justo en frente de los ojos de la otra persona.")

    print("Final bueno: La mejor tarde de tu vida.")
    return

while True:
    main()
    input("\nPresiona enter para volver a empezar...")
