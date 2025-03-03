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



"""
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
"""

def check_answer(response):  # Überprüft, ob die Eingabe richtig ist
    user_response = input("Deine Lösung: ")
    response_tries = 4  # Maximale Anzahl der Versuche

    for i in range(4, 0, -1):
        if user_response != response and response_tries > 0:
            print("Falsche Lösung!")
            print(f"Du hast noch {i} Versuche!")
            user_response = input("Deine Lösung: ")
        elif response_tries > 0:
                print("Super! Das ist richtig!")
                response_tries = 0
        if response_tries == 0 and user_response != response:
            print("Du hast deine Versuche aufgebraucht! Starte das Programm erneut!")
            exit()


def beginner_unit():
    print("""
    Lerneinheit für Anfänger:
    - Was sind Variablen und wie verwendest du sie?
    - Wie erstellst du Schleifen in Python?
    - Funktionen definieren und anwenden

    Drücke eine beliebige Taste, um mit der Lerneinheit zu beginnen...
    """)
    input()

    print("\nFrage 1: Was ist eine Variable in Python?")
    print("1) Eine Funktion")
    print("2) Ein Datentyp")
    print("3) Ein Speicherort für Daten")
    print("4) Ein Schleifen-Konstrukt")
    check_answer("3")  # Die richtige Antwort ist "3"

    print("\nFrage 2: Wie erstelle ich eine Schleife in Python?")
    print("1) Mit einer Funktion")
    print("2) Mit einer Bedingung")
    print("3) Mit 'for' oder 'while'")
    print("4) Mit 'if' und 'else'")
    check_answer("3")  # Die richtige Antwort ist "3"

    print("\nFrage 3: Wie definierst du eine Funktion in Python?")
    print("1) Mit 'function'")
    print("2) Mit 'def'")
    print("3) Mit 'lambda'")
    print("4) Mit 'func'")
    check_answer("2")  # Die richtige Antwort ist "2"

    print("\nGlückwunsch! Du hast die Lerneinheit abgeschlossen!")

def intermediate_unit():
    print("""
    Lerneinheit für Mittelstufe:
    - Listen und Dictionaries verstehen und verwenden
    - Fehlerbehandlung mit try-except
    - Funktionen mit mehreren Parametern und Rückgabewerten

    Drücke eine beliebige Taste, um mit der Lerneinheit zu beginnen...
    """)
    input()

def advenced_unit():
    print("""
    Lerneinheit für Fortgeschrittene:
    - Objektorientierte Programmierung (OOP) in Python
    - Arbeiten mit Datenstrukturen wie Bäumen und Graphen
    - Implementierung und Analyse von Algorithmen

    Drücke eine beliebige Taste, um mit der Lerneinheit zu beginnen...
    """)
    input()



if learning_level == "1":
    beginner_unit()
elif learning_level == "2":
    intermediate_unit()
elif learning_level == "3":
    advanced_unit()


