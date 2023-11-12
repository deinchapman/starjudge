good_ending = "Definitivamente, volverán a verse otro día"
neutral_ending = "No siempre se puede conseguir el resultado que uno quiere, pero al menos puedes seguir intenando"
bad_ending = "Sientes cómo este dia ha sido un desprecio e irrespeto a tu tiempo, no volverás a cometer el mismo error"
Just_failure = "Algo nos dice que deberías replantearte tus habilidades para socializar"



        
POINTS = 50
GOOD_CHOICE = 20
MEH_CHOICE = 15
BAD_CHOICE = -10


    
def start():
    NAME = input("¿Podrías recordarme tu nombre por favor?: ")
    FRIEND = input(f"""
Bonito nombre, {NAME};
jeje, se me olvidan las cosas con facilidad, pido disculpas;
para que sea justo, ¿cómo te gustaría que me llame?: """)
    
    print(f"{FRIEND}? jiji, me gusta :3")

    input("press enter to continue")
    
    return NAME, FRIEND

def roots(text1, textC1, textC2, textC3):    
    conclusion = POINTS
    print(text1)
    while True:
        choice = input("¿A donde quieres que vayamos el día de hoy?(A/B/C)")
        if choice.upper() == "A":
           conclusion = cine(textC1, textC2, textC3, conclusion)
           path = 1
           break
        
        elif choice.upper() == "B":
            print("Tuiveron una linda tarde con helados")
            conclusion
            path = 2
            break
            
        elif choice.upper() == "C":
            print("Pasaron un buen rato en el parque")
            conclusion
            path = 3
            break
        
        else:
            print("Invalid input")
            continue
            
    return path, conclusion
    
        

def cine(textC1, textC2, textC3, conclusion):
    print(textC1)
    input("\npresiona <enter> para continuar\n")
    #Opción de mejor a peor C1: A, B, C
    choice = input("""
¿Como vas a actuar durante este evento?

A- Divertido
B- Coqueto
C- Edgy
D- ...
          """)
    while True:     
        if choice.upper() == "A":
            conclusion += GOOD_CHOICE 
            print("Decidiste no tomarte la situación tan a pecho e hiciste que ambos se rieran de la situación")
            break     
        
        elif choice.upper() == "B":
            conclusion += MEH_CHOICE 
            print("Pusiste una voz seductora y dijiste una frase picardía; \nUn comentario así te hizo ver cómo un payaso, pero la risas no faltaron...")
            break
            
        elif choice.upper() == "C":
            conclusion += BAD_CHOICE  
            print("Sin duda alguna, actuar cómo si fueras el cabellero de la venganza te hace ver cool;\n ojalá se pueda decir lo mismo al interactuar directamente contigo...")
            break
        
        elif choice.upper() == "D":
            conclusion += 0 
            print("no hiciste ni nada en especial *aplausos \n(FELICIDADES No hay chiste)")
            break
        
        else:
            print("invalid input")
    
            continue
    
    print(textC2)
    input("\npress enter continue\n")
    #Opción de mejor a peor C2: A, C, B 
    choice = input("""
¿Como vas a actuar durante este evento?

A- Divertido
B- Coqueto
C- Edgy
D- ...
          """)
    while True:     
        if choice.upper() == "A":
            conclusion += GOOD_CHOICE  
            print("Decidiste no tomarte la situación tan a pecho e hiciste que ambos se rieran de la situación")
            break     
        
        elif choice.upper() == "B":
            conclusion += BAD_CHOICE  
            print("Pusiste una voz seductora y dijiste una frase picardía; \nUn comentario así te hizo ver cómo un payaso, pero la risas no faltaron...")
            break
            
        elif choice.upper() == "C":
            conclusion += MEH_CHOICE  
            print("Sin duda alguna, actuar cómo si fueras el cabellero de la venganza te hace ver cool;\n ojalá se pueda decir lo mismo al interactuar directamente contigo...")
            break
        
        elif choice.upper() == "D":
            conclusion += 0 
            print("no hiciste ni nada en especial *aplausos \n(FELICIDADES No hay chiste)")
            break
        
        else:
            print("invalid input")
    
            continue

    print(textC3)
    input("\npress enter continue\n")
#Opción de mejor a peor C3: B, A, C
    choice = input("""
¿Como vas a actuar durante este evento?

A- Divertido
B- Coqueto
C- Edgy
D- ...
          """)
    while True:     
        if choice.upper() == "A":
            conclusion += MEH_CHOICE  
            print("Decidiste no tomarte la situación tan a pecho e hiciste que ambos se rieran de la situación")
            break     
        
        elif choice.upper() == "B":
            conclusion += GOOD_CHOICE  
            print("Pusiste una voz seductora y dijiste una frase picardía; \nUn comentario así te hizo ver cómo un payaso, pero la risas no faltaron...")
            break
            
        elif choice.upper() == "C":
            conclusion += BAD_CHOICE  
            print("Sin duda alguna, actuar cómo si fueras el cabellero de la venganza te hace ver cool;\n ojalá se pueda decir lo mismo al interactuar directamente contigo...")
            break
        
        elif choice.upper() == "D":
            conclusion += 0 
            print("no hiciste ni nada en especial *aplausos \n(FELICIDADES No hay chiste)")
            break
        
        else:
            print("invalid input")
    
            continue     
        
    return conclusion
        
        
def cine_endings(NAME, FRIEND, result):
    print(result)
    print(f"\nFelicidad por llegar hasta este punto {NAME}... Las estrellas juzgan tus acciones con {FRIEND}:\n")
    if result >= 99:
        print("El cine fue el lugar perfecto para compartir cartas pokemon sin que te llamen otaku, \nhablar de yugi oh sin que digan que te gusta el yaoi, \ny dar cringe... ¡JUNTOS!")

    elif 75 <= result <= 99:
                print("Se divirtieron mucho... nada mas")

    elif 50 <= result <= 74:
                print("¿Es en serio? ¡¿EN QUÉ ESTABAS PENSANDO?!")
     
    input("\npress enter to continue\n")
    
    return result
    

def endings(result):
    if result >= 100:
        print(good_ending)

    elif 75 <= result <= 99:
        print(neutral_ending)

    elif 50 <= result <= 74:
        print(bad_ending)
        
def restart():
    input("""
          
Gracias por jugar

press enter para volver a empezar

""")
    main()
            
    
def main():

    [NAME, FRIEND] = start()
    
    text1 = f"""
{FRIEND}:   ¿Que quieres que hagamos {NAME}? Podemos ir a difeferentes lugares y hacer diferentes cosas...

    A- Podemos ir al cine ¡Y podremos ver esa película que tanto quiero ver!
    
    B- Podemos ir a la heladería, hace tiempo que deseo comer helados de aquel lugar
    
    C- Podemos ir al parque, es secillamente caminar y hablar, pero no hay pérdida    
    
        """
        
    textC1 = f"""
{FRIEND}:   Waos, la fila para las boletas está muy larga, 

            Por favor ve comprando la comida mientras yo la fila para las boletas 

            ¿Okey?
"""
    textC2 = f""" 
{FRIEND}:   Jiji, se que no deberiamos hablar en medio de la película pero es que está increíble ¿A ti qué te parece?
"""

    textC3 = f""" 
{FRIEND}:   La película tuvo unas escenas tan épicas, pero ya es hora de irme, cuidate mucho ¿Si? 
"""
    textH1 = f""" 
{FRIEND}:   
    
"""
    textH2 = f""" 
{FRIEND}:
    
"""
    textH3 = f""" 
{FRIEND}:
    
"""
    textP1 = f""" 
{FRIEND}:
    
"""
    textP2 = f""" 
{FRIEND}:
    
"""
    textP3 = f""" 
{FRIEND}:
    
"""
    
    [path, conclusion] = roots(text1, textC1, textC2, textC3)
    
    result = conclusion
    
    print(f"\nTienes {result} puntos\n")
    
    input("Press enter to continue")
    if path == 1:
        cine_endings(NAME, FRIEND, result)
    
    
    endings(result)




main()

    
    





    
