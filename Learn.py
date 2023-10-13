import sys
sys.tracebacklimit=0


Ch_n = input("Nombre: ")

print("Hola", Ch_n)
print("¿Te puedo hacer una pregunta? Solo dime que si o no por favor")
Task_1 = input()

if Task_1 == ("no"): 
    print()
    print("Lo siento mucho, no te volvere a molestar")
    print()
    print("Final neutral 1: No volveras a ser molestado") 
    

elif Task_1 == ("si"):
    print("Me da pena pero... ¿podemos ir a comer un helado juntos? *Puedes escuchar entre murmuros como solo espera que le responde o que ¨si¨ o que ¨no¨ ")
    
    Task_2 = input()
    
else: 
    print() 
    print("Mejor olvidalo, no es nada")
print ()   
print ("Final neutral 2: Al final no era nada")
    
if Task_2 == ("no"):
        print("Ou... esta bien, siento mucho las molestias")
        print()
        print("Final malo: Te terminaste quedando solo e insatisfecho")
    
elif Task_2 == ("si"):
        print("Oh ¿En serio? ¡Entonces no hay tiempo que perder!")
        print()
        print("Las estrellas del destino te juzgan ¿Genuinamente quieres pasar tiempo con esta persona? *Sientes que solo puedes responder ¨si¨ o ¨no¨ a esta pregunta")
        
        Task_3 = input()
else:
 print()
 print("Uhm... pensandolo mejor, creo que no tengo ganas... mejor otro dia")
 print()
 print("Final indeciso: No eres tu, tampoco es la otra persona, algunas veces simplemente no sentimos la confianza de dar ese proximo paso en la relacion")
                  
if Task_3 == ("si"):
            print("Final bueno: La mejor tarde de tu vida")
            
elif Task_3 == ("no"):
            print("Final hipócrita: A pesar de que en un principio respondiste que si; era evidente para la otra persona que realmente no querias estar con ella, y antes de que te dieras cuenta, simplemente se despidieron para nunca volverse a ver")
        
else: 
    print()
    print("Final del mas allá: Independientemente de tu respuesta, te distrajiste demasiado hablando con seres que van mas allá de tu comprensión, y terminaste siendo atropellado por un camión, justo en frente de los ojos de la otra persona.")

        
try:
    Task_1 = input
    Task_2 = input
    Task_3 = input
except NameError: 
    print()
    print("El Fin")

