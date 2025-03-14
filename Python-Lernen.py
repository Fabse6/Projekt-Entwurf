#Authors: Moritz Mezler, Fabian Wiedemann
#Matrikelnummer von Moritz Mezler: 9582981
#Matrikelnummer von Fabian Wiedemann: 6415375
#date: 2025-03-01
#brief: Programm to learn skills in Python

'Programm to learn skills in Python'

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
            print("\nDu hast die Mittelstufe gewählt und vertiefst dein Wissen mit If-Statements!")
            break
        elif learning_level == "3":
            print("\nDu hast Fortgeschritten gewählt. Jetzt wird es anspruchsvoll! Lerne mehr über Funktionen!")
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
        if counter == 4:
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
         
        elif counter >= 10:
            print(f"\nDu hast {score} von {counter * 4} Punkten erreicht!")
            print("möchstest du zurück zum Start oder das Programm beenden? (start/'Enter')")
            choice = input().strip().lower()
            if choice == "start":
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
        start_learning_1()

    def start_learning_1():
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
        counter = 6
        
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

        print('''
######## print(f"") ######## 
              
Wie gerade schon erwähnt, können nur Strings mit Strings zusammen angezeigt werden,
oder ein Integer mit einem Integer verrechnet und das Ergebnis in der Konsole angezeigt.
Falls eine Variable einen Integer oder Float speichert, kann dieser trotzdem mit einem String ausgegeben werden:
Beispiel:
number = 5
print(f"Deiner Zahl: {number}")''')
        print('''Frage 3: Wie kann man kann man ein String und eine in einer Variable gespeicherte Zahl wie im Beispiel zusammen ausgeben?
1) String + Variable in der print-Funktion
2) durch ein "f" vor dem String und an passender Stelle die Variable in geschweiften Klammern
3) gar nicht
4) durch "f" vor dem String und dahinter die Variable mit + hinzufügen''')
        check_answer("2")
        
        
        #fourth question

        print('''
Eine andere Möglichkeit wäre die Variable durch str() in einen String umzuwandeln.
Dadurch kann man die Variable wie am Anfang durch ein plus zu dem String im print-Befehl hinzufügen.
Beispiel: print("Deine Zahl: " + str(number))''')
        print('''\nFrage 4: Folgender Code ist gegeben:
kilometres = 200
Schreibe einen Code damit folgendes in der Konsole angezeigt wird (mit der gerade beschirebenen Methode!!):
Kilometer zu fahren: 200''')
        check_code('print("Kilometer zu fahren: " + str(kilometres))')


        print("\nGlückwunsch! Du hast die Lerneinheit abgeschlossen!")
 
   
    # Definition for the intermediate learning level
    def intermediate_unit():
        # Description
        print("""
        - If-Statements – Bedingungen in Schleifen für flexible Programme.
        - Mit `if`, `elif` und `else` kannst du unterschiedliche Codeblöcke je nach Bedingung ausführen.
        Drücke eine beliebige Taste, um mit der Lerneinheit zu beginnen...
        """)

        input() # enter any value to start the learning unit/question catalog
        start_learning_2()

    def start_learning_2():
        global score, counter # changes the value of the global variable
        score = 0
        counter = 6
        third_learning_level()

    def third_learning_level():
        # first element: answering a question
        print("""
######## If-Statements ########
              
Ein if-Statement ermöglicht es, Entscheidungen im Code zu treffen. Es überprüft eine Bedingung und 
führt den zugehörigen Codeblock nur aus, wenn diese erfüllt ist.

Eigenschaften von If-Statements in Python:

    - Bedingungsauswertung: Der Ausdruck im if-Statement muss True oder False ergeben.
    - Elif für weitere Bedingungen: Mit elif lassen sich mehrere Bedingungen hintereinander prüfen.
    - Else als Abschluss: else wird ausgeführt, wenn keine der vorherigen Bedingungen zutrifft.
    - Einrückung wichtig: Der Codeblock nach if, elif oder else muss korrekt eingerückt sein.""")
        print("\nFrage 1: Was muss der Ausdruck in einem 'if'-Statement in Python ergeben, damit der zugehörige Code ausgeführt wird?")
        print("1) Der Ausdruck muss eine Zahl sein")
        print("2) Der Ausdruck muss True oder False sein")
        print("3) Der Ausdruck muss ein Textstring sein")
        print("4) Der Ausdruck muss eine Zahl größer als 10 sein")
        check_answer("2")  # the correct answer is "2"


        #second question
        print("""
######## Einführung in die Verwendung von 'if'-Statements ########

Beispiel: Wenn wir überprüfen möchten, ob ein Name ein bestimmter String ist, wie zum Beispiel "Max", könnten wir ein 'If'-Statement verwenden, um dies zu tun.
In dieser Aufgabe wirst du ein 'If'-Statement verwenden, um zu überprüfen, ob der Name 'Max' ist. 

######## Deine Aufgabe ########""")

        print("\nErstelle den Code, um zu überprüfen, ob ein Name 'Max' ist.")
        print("Hier ist der vordefinierte Code:")
        print('name = "Max"')
        print('***Füge die if-Bedingung ein!***')
        check_code("""if name == "Max":""")  
       

        # third question
        print("""
######## else-Statement ########

Das 'else'-Statement wird ausgeführt, wenn keine der vorherigen Bedingungen wahr ist. 
Es stellt eine Art "Fangnetz" dar, um einen Standardcode auszuführen, wenn keine der Bedingungen zutrifft.""")

        print("\nFrage 3: Was passiert, wenn keine der Bedingungen in einem 'if'-Statement zutrifft und kein 'else' angegeben ist?")
        print("1) Der Code gibt einen Fehler aus")
        print("2) Es wird automatisch der Code im 'else'-Block ausgeführt")
        print("3) Der Code nach dem 'if'-Block wird ausgeführt")
        print("4) Der Code wird sofort beendet")
        check_answer("3")  # Die richtige Antwort ist "3"

        # fourth question
        print("""
######## Einrückung in Python ########

In Python ist die Einrückung entscheidend, um zu definieren, welcher Code zu einem 'if', 'elif' oder 'else' gehört. 
Ohne die korrekte Einrückung gibt es einen Syntaxfehler.""")

        print("\nFrage 4: Welche Auswirkung hat es, wenn der Code nach einem 'if', 'elif' oder 'else'-Statement nicht korrekt eingerückt ist?")
        print("1) Der Code wird ignoriert und nicht ausgeführt")
        print("2) Es führt zu einem Syntaxfehler")
        print("3) Der Code wird trotzdem ausgeführt, aber mit Verzögerung")
        print("4) Der Code wird automatisch korrigiert")
        check_answer("2")  # Die richtige Antwort ist "2"
        


    # definition for the advanced learning level
    def advanced_unit():
        # Description
        print("""
        Lerneinheit für Fortgeschrittene:
        - Wie man Funktionen erstellt und aufruft.
        - Wie Funktionen Parameter entgegennehmen, um dynamisch zu arbeiten.
        - Wie man den Rückgabewert einer Funktion nutzt.
        Drücke eine beliebige Taste, um mit der Lerneinheit zu beginnen...
        """)
        input() # enter any value to start the learning unit/question catalog

        start_learning_3()

    def start_learning_3():
        global score, counter # changes the value of the global variable
        score = 0
        counter = 6
        fourth_learning_level()

    def fourth_learning_level():

        # first element: answering a question
        print("""
######## Funktionen in Python ########

In Python verwenden wir den 'def'-Befehl, um eine Funktion zu definieren. Eine Funktion ist ein benannter Codeblock, 
der eine bestimmte Aufgabe ausführt und optional einen Wert zurückgibt. Funktionen ermöglichen es, Code zu modularisieren und wiederzuverwenden.

Eigenschaften von Funktionen in Python:

    - Eine Funktion wird mit dem Schlüsselwort `def` definiert.
    - Funktionen können Parameter entgegennehmen.
    - Eine Funktion kann optional ein Ergebnis mit 'return' zurückgeben.""")

        # first question
        print("\nFrage 1: Wie definierst du eine Funktion in Python?")
        print("1) Mit dem Schlüsselwort 'function'")
        print("2) Mit dem Schlüsselwort 'def'")
        print("3) Mit dem Schlüsselwort 'method'")
        print("4) Mit dem Schlüsselwort 'func'")
        check_answer("2")  

        # second question
        print("""
######## Parameter in Funktionen ########

Eine Funktion kann Parameter entgegennehmen, die es ermöglichen, Daten an die Funktion zu übergeben und deren Verhalten zu steuern. 
In Python werden Parameter in den Klammern nach dem Funktionsnamen angegeben.

######## Deine Aufgabe ########""")

        print("\nErstelle eine Funktion, die überprüft ob eine Zahl gerade oder ungerade ist.")
        print("Die Zahl wird mit Hilfe der variablen 'number' gespeichert")
        check_code("""def check_even_or_odd(number):""")  
        

        # third question
        print("""
######## Funktionsaufruf ########

Nachdem eine Funktion definiert wurde, kann sie durch ihren Namen aufgerufen werden, wobei eventuell benötigte Argumente übergeben werden. 
Der Funktionsaufruf sieht folgendermaßen aus: `funktionsname(argumente)`.""")

        print("\nFrage 3: Wie rufst du eine Funktion in Python auf?")
        print("1) Mit dem Schlüsselwort 'call()'")
        print("2) Mit dem Funktionsnamen und Klammern")
        print("3) Mit dem Befehl 'run()'")
        print("4) Mit dem Schlüsselwort 'invoke()'")
        check_answer("2")  

        # fourth question
        print("""
######## Rückgabewert einer Funktion ########

Eine Funktion kann mit 'return' einen Wert zurückgeben, den man weiterverwenden kann. Ohne 'return' 
gibt eine Funktion automatisch `None` zurück.""")

        print("\nFrage 4: Was gibt eine Funktion zurück, wenn sie keinen 'return'-Befehl enthält?")
        print("1) Einen Fehler")
        print("2) Einen leeren Wert")
        print("3) Die Zahl 0")
        print("4) `None`")
        check_answer("4")  
        


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




