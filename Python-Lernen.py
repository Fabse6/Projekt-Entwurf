#Authors: Moritz Mezler, Fabian Wiedemann
#Matrikelnummer von Moritz Mezler:
#Matrikelnummer von Fabian Wiedemann: 6415375
#date: 2025-03-01

'Programm to learn basic skills in Python'


### Values ###

### Functions ###
def check_answer (response):                                    #überprüft, ob die Eingabe der jeweiligen Aufgabe richtig ist.
    user_response = input("Deine Lösung: ")                     #Wenn Eingabe nicht richtig ist, wird die Anzahl der Versuche angezeigt
    response_tries = 5                                          #und solange ein neuer Versuch angeboten, bis die Versuche aufgebraucht sind
    for i in range(5, 0, -1):
        if user_response != response and response_tries > 0:
            print("Falsche Lösung!")
            print(f"du hast noch {i} Versuche!")
            user_response = input("Deine Lösung: ")
            response_tries -= 1
        elif response_tries > 0:
            print("Super! Das ist richtig!")
            response_tries = 1



### Input ###

### Calculations ###

### Output ###
answer_task1 = "PI = 3.14"
check_answer (answer_task1)
 

