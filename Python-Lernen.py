#Authors: Moritz Mezler, Fabian Wiedemann
#Matrikelnummer von Moritz Mezler:
#Matrikelnummer von Fabian Wiedemann: 6415375
#date: 2025-03-01
#brief:

'Programm to learn basic skills in Python'

# Introduction for the user
print("""
********************************************
        Starte deine Python-Reise
********************************************

Mit PyLearn kannst du Python Schritt für Schritt erlernen – von den Grundlagen bis zu fortgeschrittenen Themen!

Wähle deine Lernstufe:
[1] Anfänger – Grundlagen wie Variablen, Schleifen und Funktionen
[2] Mittelstufe – Listen, Dictionaries, Fehlerbehandlung
[3] Fortgeschritten – OOP, Datenstrukturen, Algorithmen

************************************
""")

# Input of User-Informations

while True: # repeats the query for the user input until a correct input is made

    learning_level = input("Gib die Nummer deiner Lernstufe ein (1-3): ") # query of the user for the respective learning level

    
    if learning_level == "1":
        print("\nDu hast Anfänger gewählt. Hier lernst du die Basics von Python!")
        break # interrupts the while loop when the numbers 1-3 are entered
    elif learning_level == "2":
        print("\nDu hast die Mittelstufe gewählt. Du vertiefst dein Wissen mit komplexeren Konzepten!")
        break
    elif learning_level == "3":
        print("\nDu hast Fortgeschritten gewählt. Jetzt wird es anspruchsvoll mit OOP und Algorithmen!")
        break
    
    # if no correct input was made, output this text
    else:
        print("\nUngültige Eingabe. Bitte starte das Programm neu und wähle eine Zahl zwischen 1 und 3.")





### Values ###

### Functions ###
def check_answer (response):                                    #überprüft, ob die Eingabe der jeweiligen Aufgabe richtig ist.
    user_response = input("Deine Lösung: ")                     #Wenn Eingabe nicht richtig ist, wird die Anzahl der Versuche angezeigt
    response_tries = 4                                          #und solange ein neuer Versuch angeboten, bis die Versuche aufgebraucht sind
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

### Calculations ###

### Output ###

 

