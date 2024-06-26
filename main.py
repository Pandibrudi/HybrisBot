#mit dem random modul lassen sich Zufalls- bzw. Pseudozufallsoperationen durchführen
import random

# Das Skript öffnet die Liste der vermeitlich widersprüchlichen Taten und Aussagen
# Das Programm hat ausschließlich eine Leseberechtigung ("r") für das .txt file
# Das Encoding in utf-8 ermöglicht u.a. die Darstellung von Umlauten
# Die Datei wird in der Variable "file" gespeichert

with open("C:/Users/Fabia/Documents/Coding/Hybris Bot/deeds.txt", "r", encoding="utf-8") as file:

    lines = file.readlines() #gibt alle zeilen des Textdokuments als Liste aus

    # Es erfolgen i Iterationen, wobei i die Länge der Liste geteilt durch 2 ist
    # da immer exakt 2 Einträge verwendet werden
    for i in range(int(len(lines)/2)): 
        hybris_set = random.sample(lines, 2) #Ein zufälliges sample aus zwei sich nicht doppelnden Einträgen wird gewählt
        lines.remove(hybris_set[0]) #die Einträge werden aus der Liste des .txt-Dokuments entfernt, 
        lines.remove(hybris_set[1]) #damit es in nicht zu Dopplungen kommt

        # Nun werden die beiden Teile des Sets zu einer Phrase verbunden
        # Die Phrase beginnt zunächst mit dem Wort "Menschen", 
        # gefolgt vom ersten Teil des Hybris-Sets, einem " aber ", dem zweiten Teil des Sets und einem Punkt.
        # der .strip("\n") entfernt den Zeilenumbruch, sodass am Ende alles in einer Zeile steht
        phrase = "Menschen " + hybris_set[0].strip("\n") + " aber " + hybris_set[1].strip("\n") + "."

        #die Phrase wird in der Konsole ausgegeben
        print(phrase)