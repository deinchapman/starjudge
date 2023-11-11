good_ending = "Definitivamente, volverán a verse otro día"
neutral_ending = "No siempre se puede conseguir el resultado que uno quiere, pero al menos puedes seguir intenando"
bad_ending = "Sientes cómo este dia ha sido un desprecio e irrespeto a tu tiempo, no volverás a cometer el mismo error"
Just_failure = "Algo nos dice que deberías replantearte tus habilidades para socializar"



        
POINTS = 50
A = 25
B = 50
C = -abs(25)


    
def start():
    NAME = input("¿Podrías recordarme tu nombre por favor?: ")
    FRIEND = input(f"""
Bonito nombre, {NAME};
jeje, se me olvidan las cosas con facilidad, pido disculpas;
para que sea justo, ¿cómo te gustaría que me llame?: """)
    
    print(f"{FRIEND}? jiji, me gusta :3")

    input("press enter to continue")
    
    return NAME, FRIEND

def roots(NAME, FRIEND):    
    text1 = f"""
{FRIEND}: ¿Que quieres que hagamos {NAME}? Podemos ir a difeferentes lugares y hacer diferentes cosas...

    A- Podemos ir al cine ¡Y podremos ver esa película que tanto quiero ver!
    
    B- Podemos ir a la heladería, hace tiempo que deseo comer helados de aquel lugar
    
    C- Podemos ir al parque, es secillamente caminar y hablar, pero no hay pérdida    
    
        """
    print(text1)
    while True:
        choice = input("¿A donde quieres que vayamos el día de hoy?(A/B/C)")
        if choice.upper() == "A":
           conclusion = cine()
           break
        
        elif choice.upper() == "B":
            print("Tuiveron una linda tarde con helados")
            conclusion
            break
            
        elif choice.upper() == "C":
            print("Pasaron un buen rato en el parque")
            conclusion
            break
        
        else:
            print("Invalid input")
            continue
            
    return conclusion
    
        

def cine():
    
    choice = input("""
¿Como vas a actuar durante este evento?

A- Divertido
B- Coqueto
C- Edgy
D- ...
          """)
    while True:     
        if choice.upper() == "A":
            conclusion = A + POINTS
            
        
        elif choice.upper() == "B":
            conclusion = B + POINTS
            
            
        elif choice.upper() == "C":
            conclusion = C + POINTS
            
        else:
            print("invalid input")
            continue
        
        
        return conclusion
        
        
def end(NAME, FRIEND, result):
    print(result)
    print(f"\nFelicidad por llegar hasta este punto {NAME}... Las estrellas juzgan tus acciones con {FRIEND}\n")
    if result >= 99:
        print("El cine fue un buen lugar para hacer tu movimiento")

    elif 74 <= result <= 98:
                print("Se divirtieron mucho... nada mas")

    elif 50 <= result <= 73:
                print("¿Es en serio? ¡¿EN QUÉ ESTABAS PENSANDO?!")
     
    input("\npress enter to continue\n")
    endings(result)
    

def endings(result):
    if result >= 100:
        print(good_ending)

    elif 75 <= result <= 99:
        print(neutral_ending)

    elif 50 <= result <= 74:
        print(bad_ending)
        
def restart():
    print("Gracias por jugar")
            
    
def main():
    [NAME, FRIEND] = start()
    
    print(NAME, FRIEND)
    
    result = conclusion = roots(NAME, FRIEND)
    
    print(f"Tienes {result} puntos")
    
    input("Press enter to continue")
    end(NAME, FRIEND, result)
    



main()

    
    





    
