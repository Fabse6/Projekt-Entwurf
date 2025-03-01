#Authors: Moritz Mezler, Fabian Wiedemann
#Matrikelnummer von Moritz Mezler:
#Matrikelnummer von Fabian Wiedemann:
#date: 2025-03-01

'Programm to learn basic skills in Python'


### Values ###

### Functions ###
def check_answer (response):
    user_response = input("Deine Lösung: ")
    response_tries = 5
    while user_response != response:
        if response_tries > 0:
            response_tries -= 1 
            print("Falsche Antwort!")
            print(f"du hast noch {response_tries} Versuche!")
            user_response = input("Deine Lösung: ")
        else:
            print("Starte das Programm erneut!")
    else:
        print("richtige Antwort! Super!")

### Input ###
response_task1 = "PI = 3.14"

### Calculations ###

### Output ###
check_answer(response_task1)
 

