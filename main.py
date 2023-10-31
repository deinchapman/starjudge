def restart():
    answer = input("\nPresiona enter para volver a empezar.\n")
    if answer == 0:
        main()

    else:
        main()


def main():
        name = input("Muchas gracias venir, ¿Me puedes dar tu Nombre por favor?: ")
        print("\nHola", name)
        
        lover = input("Me puedes llamar lo más te guste, ¿Cómo te gustaría llamarme?\n")
        
        print("\n",lover + ":","¿Te puedo hacer una pregunta? Solo dime que si o no por favor\n")
        answer = input()

        if answer == ("no"): 
            print("\n",lover + ":","Lo siento mucho, no te volvere a molestar\n")
            print("\nFinal neutral 1: No volveras a ser molestado\n") 
            restart()
            
        elif answer == ("si"):
            print("\n",lover + ":","Me da pena pero... ¿podemos ir a comer un helado juntos? *Puedes escuchar entre murmuros como solo espera que le responde o que ¨si¨ o que ¨no¨\n")
            answer = input()
        else:  
            print("\n",lover + ":","Mejor olvidalo, no es nada\n")
            print ("\nFinal neutral 2: Al final no era nada\n")
            restart()
        
        if answer == ("no"):
            print("\n",lover + ":","Ou... esta bien, siento mucho las molestias\n")
            print("\nFinal malo: Te terminaste quedando solo e insatisfecho\n")
            restart()
        elif answer == ("si"):
            print("\n",lover + ":","Oh ¿En serio? ¡Entonces no hay tiempo que perder!\n")
            print("\nLas estrellas del destino te juzgan ¿Genuinamente quieres pasar tiempo con esta persona? *Sientes que solo puedes responder ¨si¨ o ¨no¨ a esta pregunta\n")
            answer = input()
            if answer == ("si"):
                print("\nFinal bueno: La mejor tarde de tu vida\n")
            elif answer == ("no"):
                print("\nFinal hipócrita: A pesar de que en un principio respondiste que si; era evidente para la otra persona que realmente no querias estar con ella, y antes de que te dieras cuenta, simplemente se despidieron para nunca volverse a ver\n")
                restart()
            else: 
                print("\nFinal del mas allá: Independientemente de tu respuesta, te distrajiste demasiado hablando con seres que van mas allá de tu comprensión, y terminaste siendo atropellado por un camión, justo en frente de los ojos de la otra persona.\n")
                restart()

        else:
            print("\nUhm... pensandolo mejor, creo que no tengo ganas... mejor otro dia\n")
            print("\nFinal indeciso: No eres tu, tampoco es la otra persona, algunas veces simplemente no sentimos la confianza de dar ese proximo paso en la relacion\n")
        restart()

main()


    