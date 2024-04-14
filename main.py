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
    # aus diesem Grund sollte sich immer eine gerade Anzahl an Einträgen in der Liste befinden
    for i in range(int(len(lines)/2)): 
        hybris_set = random.sample(lines, 2) #Ein zufälliges sample aus zwei sich nicht doppelnden Einträgen wird gewählt
        lines.remove(hybris_set[0]) #die Einträge werden aus der Liste des .txt-Dokuments entfernt, 
        lines.remove(hybris_set[1]) #damit es in nicht zu Dopplungen kommt

        # 
        phrase = "Menschen " + hybris_set[0].strip("\n") + " aber " + hybris_set[1].strip("\n") + "."

        print(phrase)