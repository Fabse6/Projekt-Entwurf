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

    def check_answer(response):
        #checks if user's input is correct or not, if no tries left user has to start again  
        user_response = input("Deine Lösung: ")
        response_tries = 5  
        global score, counter # changes the value of the global variable

        for i in range(5, 0, -1):
            if user_response != response and response_tries > 1:
                print("\nFalsche Lösung!")
                print(f"Du hast noch {i - 1} Versuche!")
                user_response = input("\nDeine Lösung: ")
                response_tries -= 1
            elif response_tries >= 1 and user_response == response:
                print("Super! Das ist richtig!")
                counter += 1
                # Calculation of score points depending on the number of attempts required
                if response_tries == 5:
                 score += 4
                if response_tries >= 2 and response_tries <= 4:
                    score += 2
                if response_tries < 2:
                    score += 1
                break #ends the loop so that the current score is still displayed (unlike return)
            elif response_tries == 1 and user_response != response:
                print("\n\nDie richtige Antwort wäre: " + str(response))
                print("\nDu hast deine Versuche aufgebraucht!")
                counter += 1

        check_next_level()

        for i in range(5, 0, -1):
            if user_response != response and response_tries > 1:
                print("Falsche Lösung!")
                print(f"Du hast noch {i - 1} Versuche!")
                user_response = input("Deine Lösung: ")
                response_tries -= 1
            elif response_tries >= 1 and user_response == response:
                    print("Super! Das ist richtig!")
                    response_tries -= 5
            elif response_tries == 1 and user_response != response:
                print("\n\nDie richtige Antwort wäre: " + str(response))
                print("\nDu hast deine Versuche aufgebraucht!")
                print("Drücke 'Enter', um das Programm neuzustarten!")
                input()
                restart_program()




    def check_code(expected_code):  
        #checks if user's input is correct. If no tries left user has to start again
        print("\nSchreibe den folgenden Code:")
        print(f"   {expected_code}")
        user_code = input("Deine Eingabe: ")
        response_tries = 5
        global score, counter # changes the value of the global variable

        for i in range(5, 0, -1):
            if user_code.strip() == expected_code.strip() and response_tries >= 1:
                print("Super! Dein Code ist korrekt.")
                response_tries -= 5
                counter += 1
                # Calculation of score points depending on the number of attempts required
                if response_tries == 5:
                 score += 4
                if response_tries >= 2 and response_tries <= 4:
                    score += 2
                if response_tries < 2:
                    score += 1
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
                restart_program()

        check_next_level()


    def check_next_level():
        global counter
        if counter >= 4:
            print(f"Du hast {score} von 4 Punkten erreicht!")
            print("möchstest du zur nächten Lerneinheit wechseln oder zurück zum Start? (nächste/start)")
            choice = input().strip().lower()
            if choice == "nächste":
                second_learning_level()
            elif choice == "start":
                beginner_unit()
            else:
                print("Programm beendet")   


    def check_code(expected_code):  
        #checks if user's input is correct. If no tries left user has to start again
        print("\nSchreibe den folgenden Code:")
        print(f"   {expected_code}")
        user_code = input("Deine Eingabe: ")
        response_tries = 5
        for i in range(5, 0, -1):
            if user_code.strip() == expected_code.strip() and response_tries >= 1:
                print("Super! Dein Code ist korrekt.")
                response_tries -= 5
            elif user_code.strip() != expected_code.strip() and response_tries > 1:
                print("Falsch! Versuch es nochmal.")
                print(f"du hast noch {i - 1} Versuche!")
                response_tries -= 1 
                user_code = input("Deine Eingabe: ")
            elif response_tries == 1 and user_code.strip() != expected_code.strip():
                print("\n\nDer richtige Code wäre: " + expected_code)
                print("\nDu hast deine Versuche aufgebraucht!")
                print("Drücke 'Enter', um das Programm neuzustarten!")
                restart_program()



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
        print("\nFrage 1: Was ist eine Variable in Python?")
        print("1) Eine Funktion")
        print("2) Ein Datentyp")
        print("3) Ein Speicherort für Daten")
        print("4) Ein Schleifen-Konstrukt")
        check_answer("3")  # the correct answer is "3"

        # second element: input / creation of a program code
        print("\nFrage 2: Schreibe jetzt selbst einen Code, um 'Hello World!' auszugeben.")
        check_code('print(1)')

        # third element: answering a question 
        print("\nFrage 3: Wie erstelle ich eine Schleife in Python?")
        print("1) Mit einer Funktion")
        print("2) Mit einer Bedingung")
        print("3) Mit 'for' oder 'while'")
        print("4) Mit 'if' und 'else'")
        check_answer("3")  # the correct answer is "3"
        print("""Drücke eine beliebige Taste, um mit der Lerneinheit zu beginnen...
            """)
        input() # enter any value to start the learning unit/question catalog
        # first element: answering a question
        print("\nFrage 1: Was ist eine Variable in Python?")
        print("1) Eine Funktion")
        print("2) Ein Datentyp")
        print("3) Ein Speicherort für Daten")
        print("4) Ein Schleifen-Konstrukt")
        check_answer("3")  # the correct answer is "3"
        # second element: input / creation of a program code
        print("\nSchreibe jetzt selbst einen Code, um 'Hello World!' auszugeben.")
        check_code('print("Hello World!")')
        # third element: answering a question 
        print("\nFrage 2: Wie erstelle ich eine Schleife in Python?")
        print("1) Mit einer Funktion")
        print("2) Mit einer Bedingung")
        print("3) Mit 'for' oder 'while'")
        print("4) Mit 'if' und 'else'")
        check_answer("3")  # the correct answer is "3"

        # fourth element: answering a question
        print("\nFrage 4: Wie definierst du eine Funktion in Python?")
        print("1) Mit 'function'")
        print("2) Mit 'def'")
        print("3) Mit 'lambda'")
        print("4) Mit 'func'")
        check_answer("2")  # the correct answer is "2"
            # fourth element: answering a question
        print("\nFrage 3: Wie definierst du eine Funktion in Python?")
        print("1) Mit 'function'")
        print("2) Mit 'def'")
        print("3) Mit 'lambda'")
        print("4) Mit 'func'")
        check_answer("2")  # the correct answer is "2"

    def second_learning_level():
        global score, counter # changes the value of the global variable
        score = 0
        counter = 0
        print("\nFrage 1: Was ist eine Liste in Python?")
        print("1) Eine Variable")
        print("2) Eine Sammlung von Werten")
        print("3) Ein Datentyp")
        print("4) Eine Schleife")
        check_answer("2")

        print("\nFrage 2: Wie iteriert man durch eine Liste in Python?")
        print("1) Mit 'for' oder 'while'")
        print("2) Mit 'if'")
        print("3) Mit einer Funktion")
        print("4) Mit einer Klasse")
        check_answer("1")

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




