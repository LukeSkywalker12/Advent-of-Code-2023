input = open("Day-1/input.txt", "r")

gesamt = 0

numbers = ("1", "2", "3", "4", "5", "6", "7", "8", "9", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine")

def findZahl1(line):
    index = len(line)
    returnNumber = "0"

    for number in numbers:                                          # Einmal für jede Nummer in der Liste durchgehen
        indexOfNumber = line.find(number)                           # 'find' gibt den Index des ersten Punktes des Gefundenen Wertes zurück

        if indexOfNumber != -1 and indexOfNumber < index:
            index = indexOfNumber
            if numbers.index(number) < 9 :
                returnNumber = number
            else:
                returnNumber = str(numbers.index(number)-8)         # Beispiel: "two" hat index 10 -> 10-8 = 2  es wird "2" für zurückgegeben
    
    return returnNumber

def findZahl2(line):
    index = -1
    returnNumber = "0"

    for number in numbers:
        indexOfNumber = line.rfind(number)                          # 'rfind' gibt index von dem hintersten gefunden Punkt des eingegebenen Wertes

        if indexOfNumber != -1 and indexOfNumber > index:
            index = indexOfNumber
            if numbers.index(number) < 9 :
                returnNumber = number
            else:
                returnNumber = str(numbers.index(number)-8)         # Beispiel: "two" hat index 10 -> 10-8 = 2  es wird "2" für zurückgegeben
    
    return returnNumber
    

for line in input:
    zahl = findZahl1(line) + findZahl2(line)
    gesamt += int(zahl)


print(gesamt)
