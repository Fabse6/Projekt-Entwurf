#Authors: Moritz Mezler, Fabian Wiedemann
#Matrikelnummer von Moritz Mezler:
#Matrikelnummer von Fabian Wiedemann: 6415375
#date: 2025-03-01
#brief:

'Programm to learn basic skills in Python'


### Values ###

### Functions ###

def check_answer (response):       
    #checks, if user`s awnser is correct or not. If not it shows
    #remaining tries and if no tries left the user has to restart
    #the programm                             
    user_response = input("Deine Lösung: ")                     
    response_tries = 4                                          
    for i in range(4, 0, -1):
        if user_response != response and response_tries > 0:
            print("Falsche Lösung!")
            print(f"du hast noch {i} Versuche!")
            user_response = input("Deine Lösung: ")
            response_tries -= 1
        elif response_tries > 0:
            print("Super! Das ist richtig!")
            response_tries = 0
        if response_tries == 0 and user_response != response:
            print("Du hast deine Versuche aufgebraucht! Starte das Programm erneut!")
            exit()
            




### Input ###

user_skill_level = input("Was ist dein Skillevel in Python? (Anfänger, Fortgeschritten, Profi): ")

### Calculations ###


### Output ###

 

