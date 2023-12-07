input = open("Day-1/input.txt", "r")         # Liest die Liste ein

gesamt = 0

for line in input:                          # geht einmal durch die Liste durch
    zahl = 0

    for __ in line:                         # geht einmal von vorne durch die Zeile durch
        if __.isdigit():                    # falls der Teil vom String (nur ein Buchstabe oder eine Zahl) eine Zahl ist
            zahl = __                       # setzt er die Variable auf diese Zahl
            break                           # und beendet die for-Schleife
    
    index = -1

    while index >= len(line)*-1:            # geht einmal von hinten durch die Zeile durch
        if line[index].isdigit():           # hier auch falls es eine Zahl ist
            zahl += line[index]             # wird die Zahl dann der Variable hinzugefügt
            break                           # und die Schleife beendet
        index-=1
    
    gesamt += int(zahl)                     # dann wird die Zahl noch der Gesamtzahl hinzuaddiert

print(gesamt)
