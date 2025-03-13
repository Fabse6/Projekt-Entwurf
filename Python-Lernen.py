#Authors: Moritz Mezler, Fabian Wiedemann
#Matrikelnummer von Moritz Mezler: 9582981
#Matrikelnummer von Fabian Wiedemann: 6415375
#date: 2025-03-01
#brief:

'Programm to learn basic skills in Python'

def main():
    
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


        ### Input ### 

    counter = 0
    
    def restart_program():
        main()
        
    def Enter_to_go_on():
        print("\nDrücke 'Enter', um weiterzumachen!")
        input()

    def check_answer(response):
        #checks if user's input is correct or not, if no tries left user has to start again  
        user_response = input("Deine Lösung: ")
        response_tries = 5  
        global score, counter # changes the value of the global variable

        for i in range(5, 0, -1):
            if user_response.strip() != response and response_tries > 1:
                print("\nFalsche Lösung!")
                print(f"Du hast noch {i - 1} Versuche!")
                user_response = input("\nDeine Lösung: ")
                response_tries -= 1
            elif response_tries >= 1 and user_response.strip() == response:
                print("Super! Das ist richtig!")
                counter += 1
                # Calculation of score points depending on the number of attempts required
                if response_tries == 5:
                 score += 4
                if response_tries >= 2 and response_tries <= 4:
                    score += 2
                if response_tries < 2:
                    score += 1
                response_tries -= 6
                Enter_to_go_on()
                break #ends the loop so that the current score is still displayed (unlike return)
            elif response_tries == 1 and user_response.strip() != response:
                response_tries -= 6
                print("\n\nDie richtige Antwort wäre: " + str(response))
                print("\nDu hast deine Versuche aufgebraucht!")
                print("Drücke 'Enter', um das Level nochmal zu versuchen")
                input()
                restart_program()
                counter += 1

        check_next_level()


    def check_code(expected_code):  
        #checks if user's input is correct. If no tries left user has to start again
        user_code = input("Deine Eingabe: ")
        response_tries = 5
        global score, counter # changes the value of the global variable

        for i in range(5, 0, -1):
            if user_code.strip() == expected_code.strip() and response_tries >= 1:
                print("Super! Dein Code ist korrekt.")
                counter += 1
                # Calculation of score points depending on the number of attempts required
                if response_tries >= 5:
                 score += 4
                if response_tries >= 2 and response_tries <= 4:
                    score += 2
                if response_tries < 2:
                    score += 1
                response_tries -= 6
                Enter_to_go_on()
                break #ends the loop so that the current score is still displayed (unlike return)
            elif user_code.strip() != expected_code.strip() and response_tries > 1:
                print("\nFalsch! Versuch es nochmal.")
                print(f"Du hast noch {i - 1} Versuche!")
                response_tries -= 1 
                user_code = input("Deine Eingabe: ")
            elif response_tries == 1 and user_code.strip() != expected_code.strip():
                print("\n\nDer richtige Code wäre: " + expected_code)
                print("\nDu hast deine Versuche aufgebraucht!")
                print("Drücke 'Enter', um das Programm neuzustarten!")
                counter += 1
                response_tries -= 6
                restart_program()

        check_next_level()


    def check_next_level():
        global counter
        if counter >= 4:
            print(f"\nDu hast {score} von {counter * 4} Punkten erreicht!")
            print("möchstest du zur nächten Lerneinheit wechseln, zurück zum Start oder das Programm beenden? (nächste/start/'Enter')")
            choice = input().strip().lower()
            if choice == "nächste":
                second_learning_level()
            elif choice == "start":
                restart_program()
            else:
                print("Programm beendet")
                exit()  



        # definition for the learning level “beginner”
    def beginner_unit(): 
        # description
        print("""
Lerneinheit für Anfänger:
- Was sind Variablen und wie verwendest du sie?
- Wie erstellst du Schleifen in Python?
- Funktionen definieren und anwenden
Drücke eine beliebige Taste, um mit der Lerneinheit zu beginnen...
        """)
        input() # enter any value to start the learning unit/question catalog
        start_learning()

    def start_learning():
        global score, counter # changes the value of the global variable
        score = 0
        counter = 0
        first_learning_level()

    def first_learning_level():
        # first element: answering a question
        print("""######## Variablen ########
              
Eine Variable in Python ist ein Speicherplatz für Daten, dem ein Name zugewiesen wird. Sie ermöglicht es, Werte zu speichern und später im Code wiederzuverwenden.
Eigenschaften von Variablen in Python:
    - Dynamische Typisierung: Du musst den Datentyp (String, Float, Integer, ...)nicht angeben, Python erkennt ihn automatisch.
    - Zuweisung mit =: Eine Variable wird mit = einem Wert zugewiesen.
    - Namen dürfen Buchstaben, Zahlen und _ enthalten (dürfen aber nicht mit einer Zahl beginnen).
    - Zu empfehlen: Leerzeichen zwischen Variable, =, und Wert, der in der Variable gespeichert werden soll""")
        print("\nFrage 1: Was ist eine Variable in Python?")
        print("1) Eine Funktion")
        print("2) Ein Datentyp")
        print("3) Ein Speicherort für Daten")
        print("4) Ein Schleifen-Konstrukt")
        check_answer("3")  # the correct answer is "3"

        # second element: input / creation of a program code
        print("""\n######## print()- Befehl ########

Indem man den Befehl print() eingibt, kann man etwas in der Konsole ausgeben. 
Indem man eine schon zugewiesene Variable zwischen die Klammern schreibt, wird der Wert der Variable in der Konsole ausgegeben.""")
        print("Wenn Du zwischen den Klammern einen Text zwischen Anführungszeichen schreibst, wird dieser Text ausgegeben")
        print("\nFrage 2: Schreibe jetzt selbst einen Code, um 'Hello World!' auszugeben.")
        check_code('print("Hello World!")')

        # third element: answering a question 
        print("""\n######## Mathematische Rechnungen ########
Addition: +
Subtraktion: -
Multiplikation: *
Division: /

Man kann auch 2 Variablen miteinander verrechnen. Erstelle eine neue Variable 'litre',
welche die Variable 'price' durch die Variable 'litre_price' teilt:
price = 72
litre_price = 1,80
""")
        check_code("litre = price / litre_price")

        # fourth element: answering a question
        print("Frage 4: Gib nun den Wert der neuen Variable aus!")
        check_code('print(litre)')

            # fourth element: answering a question

    def second_learning_level():
        global score, counter # changes the value of the global variable
        score = 0
        counter = 0
        
        #first question
        print("""\n\n######## input()-Befehl ########

Der Input-Befehl wird verwendet, wenn man eine Eingabe des Nutzers in einer Variable speichern will.
Die Eingabe des Nutzers wird als sogenannter String gespeichert. 
Wenn man mit der Variable weiter rechnen will, muss man den Input-Befehl in einen int()- (ganze Zahl) oder float()- (Dezimalzahl) Befehl schreiben.
Beispiel: variable = float(input("Zahl: "))
Somit wird eine Zahl in der Variable gespeichert""")
        print('\nFrage 1: Frage den Nutzer nach einer Zahl (input("Zahl: ")und speichere diesehn Ganzzahlenwert (Integer) vom Nutzer in einer Variable "number"')
        check_code('number = int(input("Zahl: "))')
        
        
        #second question
        print("""\n\n######## Variable und String in einem print()-Befehl #########

Indem man in dem print()-Befehl zwei Strings mit einem plus verbindet, werden beide nacheinander ausgegeben.
Genauso läuft es, wenn man einen String durch ein + mit einer Variable verbindet (Leerzeichen zwischen Elementen), 
VORAUSGESETZT ein String ist in der Variable gespeichert.""")
        print('''\nFrage 2: Folgende Variable ist schon im Programmcode:
name = "Max Mustermann"
In der Konsole soll nun folgendes stehen: Dein name ist Max
Schreibe diesen Code!''')
        check_code('print("Dein Name ist " + name)')
        
        #third question

        print("\nFrage 3: Wie erstellt man eine Klasse in Python?")
        print("1) Mit 'def'")
        print("2) Mit 'class'")
        print("3) Mit 'function'")
        print("4) Mit 'type'")
        check_answer("2")

        print("\nFrage 4: Was bedeutet 'self' in Klassenmethoden?")
        print("1) Eine Variable")
        print("2) Ein Parameter")
        print("3) Eine Referenz auf die Instanz")
        print("4) Eine Schleife")
        check_answer("3")


        print("\nGlückwunsch! Du hast die Lerneinheit abgeschlossen!")

    # Definition for the intermediate learning level
    def intermediate_unit():
        # Description
        print("""
        Lerneinheit für Mittelstufe:
        - Listen und Dictionaries verstehen und verwenden
        - Fehlerbehandlung mit try-except
        - Funktionen mit mehreren Parametern und Rückgabewerten
        Drücke eine beliebige Taste, um mit der Lerneinheit zu beginnen...
        """)
        input() # Enter any value to start the learning unit/question catalog

    # definition for the advanced learning level
    def advanced_unit():
        # description
        print("""
        Lerneinheit für Fortgeschrittene:
        - Objektorientierte Programmierung (OOP) in Python
        - Arbeiten mit Datenstrukturen wie Bäumen und Graphen
        - Implementierung und Analyse von Algorithmen
        Drücke eine beliebige Taste, um mit der Lerneinheit zu beginnen...
        """)
        input() # enter any value to start the learning unit/question catalog



                ### Output ### 

        # prints the values ​​of the beginner_unit definition when the number "1" is selected
    if learning_level == "1":
        beginner_unit()
    # prints the values ​​of the intermediate_unit definition when the number "2" is selected
    elif learning_level == "2":
        intermediate_unit()
    # prints the values ​​of the advanced_unit definition when the number "3" is selected
    elif learning_level == "3":
        advanced_unit()

main()




