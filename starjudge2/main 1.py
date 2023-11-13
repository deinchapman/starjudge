import sys

good_ending = """
    Final [D]

[D]efinitivamente, volverán a verse otro día ;)

"""
neutral_ending = """
    Final [N]

Uno [N]o siempre se puede conseguir el resultado que uno quiere, 
pero al menos puedes seguir intenando

"""
bad_ending = """
    Final [S]   

[S]ientes cómo este dia ha sido un desprecio e irrespeto a tu tiempo, 
pero en este punto ya no volverás a cometer el mismo error...

"""

def failure(FRIEND):
    Just_failure = f"""
Simplemente Fracaso.

    {FRIEND} decidió que lo mejor era irse, y simplemente no volverte a hablar
    
    en este punto las razones ya no importan;

    Algo nos dice que deberías replantearte tus habilidades para socializar.

"""
    print(Just_failure)
    input("Presiona <enter> para continuar", restart())
        
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

def roots(text1, textC1, textC2, textC3, textH1, textH2, textH3, textP1, textP2, textP3, FRIEND):    
    conclusion = POINTS
    print(text1)
    while True:
        choice = input("¿A donde quieres que vayamos el día de hoy?(A/B/C)")
        if choice.upper() == "A":
           conclusion = cine(textC1, textC2, textC3, FRIEND, conclusion)
           path = 1
           break
        
        elif choice.upper() == "B":
            conclusion = helados(textH1, textH2, textH3, FRIEND, conclusion)
            path = 2
            break
            
        elif choice.upper() == "C":
            conclusion = parque(textP1, textP2, textP3, FRIEND, conclusion)
            path = 3
            break
        
        else:
            print("Invalid input")
            continue
            
    return path, conclusion
    
        

def cine(textC1, textC2, textC3,FRIEND, conclusion):
    print(textC1)
    input("\npresiona <enter> para continuar\n")
    #Opción de mejor a peor C1: A, B, C
    while True:
        choice = input(f"""
    Ahora mismo están en frente de la fila para comprar las entradas a la película, {FRIEND} está de pie al lado tuyo, 
    esperando tu respuesta.                                              
    ¿Como vas a actuar durante este evento?

    A- Divertido
    B- Coqueto
    C- Edgy
    D- ...
            """)
            
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
        
        elif conclusion < 50:
            failure(FRIEND)    
        
        else:
                print("invalid input")
        
                continue
    
    print(textC2)
    input("\npress enter continue\n")
    #Opción de mejor a peor C2: A, C, B 
    while True:
        choice = input(f"""
Después de comprar las entradas, comida, y lograr acomodarse en la sala de le película;
{FRIEND} parece buscar una corta retroalimentación de tu parte sobre lo que están viendo ahora mismo en la pelicula.
¿Como vas a actuar durante este evento?

A- Divertido
B- Coqueto
C- Edgy
D- ...
          """)
     
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
    while True:    
        choice = input("""
Ambos pasaron una noche majistral con aquella película independientemente de sus interacciones personales; 
pero ya llegó la hora de despedirse.                
¿Como vas a actuar durante este evento?

A- Divertido
B- Coqueto
C- Edgy
D- ...
          """)     
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
    print(f"\nFelicidades por llegar hasta este punto {NAME}... Las estrellas juzgan tus acciones con {FRIEND}:\n")
    if result >= 99:
        print("El cine fue el lugar perfecto para compartir cartas pokemon sin que te llamen otaku, \nhablar de yugi oh sin que digan que te gusta el yaoi, \ny dar cringe... ¡JUNTOS!")

    elif 75 <= result <= 99:
                print("Se divirtieron mucho... nada mas")

    elif 50 <= result <= 74:
                print("¿Es en serio? ¡¿EN QUÉ ESTABAS PENSANDO?!")
     
    input("\npress enter to continue\n")
    
    return result

def helados(textH1, textH2, textH3, FRIEND, conclusion):
    print(textH1)
    input("\npresiona <enter> para continuar\n")
    #Opción de mejor a peor H1: C, A, B
    while True:
        choice = input(f"""
{FRIEND} parece estar disgutado con esta escena llena de personas y ni un espacio para respirar.
¿Como vas a actuar durante este evento?

A- Divertido
B- Coqueto
C- Edgy
D- ...
          """)     
        if choice.upper() == "A":
            conclusion += MEH_CHOICE  
            print("Decidiste no tomarte la situación tan a pecho e hiciste que ambos se rieran de la situación")
            break     
        
        elif choice.upper() == "B":
            conclusion += BAD_CHOICE  
            print("Pusiste una voz seductora y dijiste una frase picardía; \nUn comentario así te hizo ver cómo un payaso, pero la risas no faltaron...")
            break
            
        elif choice.upper() == "C":
            conclusion += GOOD_CHOICE   
            print("Sin duda alguna, actuar cómo si fueras el cabellero de la venganza te hace ver cool;\n ojalá se pueda decir lo mismo al interactuar directamente contigo...")
            break
        
        elif choice.upper() == "D":
            conclusion += 0 
            print("no hiciste ni nada en especial *aplausos \n(FELICIDADES No hay chiste)")
            break

        elif conclusion < 50:
            failure(FRIEND) 
 
        else:
            print("invalid input")
    
            continue

    print(textH2)
    input("\npresiona <enter> para continuar\n")
    #Opción de mejor a peor H2: B, A, C
    while True:
        choice = input(f"""
De alguna forma te las ingeniaste para comprarle un helado a {FRIEND};   
Pero este parece sentirse culpable por hacer que sacaras tu cartera.                
¿Como vas a actuar durante este evento?

A- Divertido
B- Coqueto
C- Edgy
D- ...
          """)     
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

    print(textH3)
    input("\npresiona <enter> para continuar\n")
    #Opción de mejor a peor H3: B, A, C
    while True:
        choice = input(f"""
Pasaron una bonita tarde con helados independientemente de sus interacciones personales, pero ya deben despedirse.                   
¿Como vas a actuar durante este evento?

A- Divertido
B- Coqueto
C- Edgy
D- ...
          """)     
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


def helados_endings(NAME, FRIEND, result):
    print(result)
    print(f"\nFelicidades por llegar hasta este punto {NAME}... Las estrellas juzgan tus acciones con {FRIEND}:\n")
    if result >= 99:
        print("Nada cómo un postre frío para entrar en calor ;)")

    elif 75 <= result <= 99:
                print("Se divirtieron mucho... nada mas")

    elif 50 <= result <= 74:
                print("¿Es en serio? ¡¿EN QUÉ ESTABAS PENSANDO?!")
     
    input("\npress enter to continue\n")
        
    return result


def parque(textP1, textP2, textP3, FRIEND, conclusion):
    print(textP1)
    input("\npresiona <enter> para continuar\n")
    #Opción de mejor a peor P1: B, A, C
    while True:
        choice = input(f"""
Tú y {FRIEND} caminan sobre el camino pavimentado del parque sin estar haciendo nada en especial;
Puedes intentar hacer algún comentario u observación sobre los alrededores o lo que sea que pase por tu mente;
quién sabe y da paso a una conversación.
¿Como vas a actuar durante este evento?

A- Divertido
B- Coqueto
C- Edgy
D- ...
          """)     
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
        
        elif conclusion < 50:
            failure(FRIEND) 
        
        else:
            print("invalid input")
    
            continue

    print(textP2)
    input("\npresiona <enter> para continuar\n")
    #Opción de mejor a peor P2: D?, B, A 
    while True:
        choice = input(f"""
Después de caminar por un rato, {FRIEND} propone que se tomen un descanso y que escuchen música.
¿Como vas a actuar durante este evento?

A- Divertido
B- Coqueto
C- Edgy
D- ...
          """)     
        if choice.upper() == "A":
            conclusion += MEH_CHOICE  
            print("Decidiste no tomarte la situación tan a pecho e hiciste que ambos se rieran de la situación")
            break     
        
        elif choice.upper() == "B":
            conclusion += MEH_CHOICE  
            print("Pusiste una voz seductora y dijiste una frase picardía; \nUn comentario así te hizo ver cómo un payaso, pero la risas no faltaron...")
            break
            
        elif choice.upper() == "C":
            conclusion += 0  
            print("Sin duda alguna, actuar cómo si fueras el cabellero de la venganza te hace ver cool;\n ojalá se pueda decir lo mismo al interactuar directamente contigo...")
            break
        
        elif choice.upper() == "D":
            conclusion += GOOD_CHOICE  
            print("no hiciste ni nada en especial *aplausos \n(FELICIDADES No hay chiste)")
            break
        
        else:
            print("invalid input")
    
            continue

    print(textP3)
    input("\npresiona <enter> para continuar\n")
    #Opción de mejor a peor P3: B, A, C
    while True:
        choice = input("""
    Independientemente de sus interacciones personales, 
    se puede decir que pasaron un rato agradable caminando y escuchando música;
    pero finalmente llegó la hora de decir adiós.                   
    ¿Como vas a actuar durante este evento?

    A- Divertido
    B- Coqueto
    C- Edgy
    D- ...
            """)     
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

def parque_endings(NAME, FRIEND, result):
    print(result)
    print(f"\nFelicidades por llegar hasta este punto {NAME}... Las estrellas juzgan tus acciones con {FRIEND}:\n")
    if result >= 99:
        print("Nada fue forzado.\nSólo fluyeron a través de las palabras que salieron de su corazón;\nY conectaron a través de las ritmicas líricas de las canciones")

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
        
    return
                            
    
def main():

    [NAME, FRIEND] = start()
    
    text1 = f"""
{FRIEND}:   ¿Que quieres que hagamos {NAME}? Podemos ir a difeferentes lugares y hacer diferentes cosas...

    A- Podemos ir al cine ¡Y podremos ver esa película que tanto quiero ver!
    
    B- Podemos ir a la heladería, hace tiempo que deseo comer helados de aquel lugar...
    
    C- Podemos ir al parque, es secillamente caminar y hablar, pero no hay pérdida ;)   
    
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
{FRIEND}:   ¿Pero y que con todo este tumulto de gente?, 
            ¿si quiera encontraremos un lugar para sentarnos?     
    
"""
    textH2 = f""" 
{FRIEND}:   No se ni como pero pudiste conseguirnos una mesa, 
            pero el helado está muy caro ¿No tienes problema con eso?
    
"""
    textH3 = f""" 
{FRIEND}:   Pasamos una bonita tarde n_n 
            pero ya es hora de irme... >_<   
"""
    textP1 = f""" 
{FRIEND}:   Simplemente caminar por el parque mientras hablamos de lo que pasa por nuestras mentes 
            solo contigo puedo disfrutar de algo así
    
"""
    textP2 = f""" 
{FRIEND}:   Me duelen los pies de caminar, quiero descansar 
            ¿Te parece bien si escuchamos música para pasar el rato?    
"""
    textP3 = f""" 
{FRIEND}:   Sin duda alguna... no cambiaría esto por nada del mundo
            Pero es hora de despedirnos, cuidate de camino a casa ¿si?     
"""
    
    [path, conclusion] = roots(text1, textC1, textC2, textC3, textH1, textH2, textH3, textP1, textP2, textP3, FRIEND)
    
    result = conclusion
    if conclusion < 50:
            failure(FRIEND) 
    
    else:
        print(f"\nTienes {result} puntos\n")
    
    input("Press enter to continue")
    if path == 1:
        cine_endings(NAME, FRIEND, result)
    if path == 2:
        helados_endings(NAME, FRIEND, result)
    if path == 3:
        parque_endings(NAME, FRIEND, result)
        
    
    endings(result)
    
    return

def restart():
    while True:
        main()    
        input("\nPreisona <Enter> para continuar.\n")
        choice = input("""
          
             Gracias por jugar.

    Presiona <enter> para volver a empezar.
    
            Para salir presiona "q".

""")
        if choice == "q":
            sys.exit( )
    
        else:
            continue
    

restart()
    



    





    
