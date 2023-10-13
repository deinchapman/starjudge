invalid_input = True
def start():
        name = input("Nombre: ")
        print("Hola", name)
        print("¿Te puedo hacer una pregunta? Solo dime que si o no por favor")
        answer = input
        if answer == ("no", "No", "NO"):
            print()
            print("Lo siento mucho, no te volvere a molestar")
            print()
            print("Final neutral 1: No volveras a ser molestado")  
        elif answer == ("si", "Si", "SI"):
            invalid_input == False
            print("Me da pena pero... ¿podemos ir a comer un helado juntos? *Puedes escuchar entre murmuros como solo espera que le responde o que ¨si¨ o que ¨no¨ ")
            answer = input()
        else:
            print() 
            print("Mejor olvidalo, no es nada")
            print ()   
            print ("Final neutral 2: Al final no era nada")
        if answer == ("no"): 
            print()
            print("Lo siento mucho, no te volvere a molestar")
            print()
            print("Final neutral 1: No volveras a ser molestado") 
        elif answer == ("si"):
            invalid_input == False
            print("Me da pena pero... ¿podemos ir a comer un helado juntos? *Puedes escuchar entre murmuros como solo espera que le responde o que ¨si¨ o que ¨no¨ ")
            answer = input()
        else: 
            print() 
            print("Mejor olvidalo, no es nada")
            print ()   
            print ("Final neutral 2: Al final no era nada")
        if answer == ("no"):
            print("Ou... esta bien, siento mucho las molestias")
            print()
            print("Final malo: Te terminaste quedando solo e insatisfecho")
        elif answer == ("si"):
            invalid_input == False
            print("Oh ¿En serio? ¡Entonces no hay tiempo que perder!")
            print()
            print("Las estrellas del destino te juzgan ¿Genuinamente quieres pasar tiempo con esta persona? *Sientes que solo puedes responder ¨si¨ o ¨no¨ a esta pregunta")
            answer = input()
        else:
            print()
            print("Uhm... pensandolo mejor, creo que no tengo ganas... mejor otro dia")
            print()
            print("Final indeciso: No eres tu, tampoco es la otra persona, algunas veces simplemente no sentimos la confianza de dar ese proximo paso en la relacion")            
        if answer == ("si"):
            print("Final bueno: La mejor tarde de tu vida")
        elif answer == ("no"):
            print("Final hipócrita: A pesar de que en un principio respondiste que si; era evidente para la otra persona que realmente no querias estar con ella, y antes de que te dieras cuenta, simplemente se despidieron para nunca volverse a ver")
        else: 
            print()
            print("Final del mas allá: Independientemente de tu respuesta, te distrajiste demasiado hablando con seres que van mas allá de tu comprensión, y terminaste siendo atropellado por un camión, justo en frente de los ojos de la otra persona.")

while invalid_input:
    start()