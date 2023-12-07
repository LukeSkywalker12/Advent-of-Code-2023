document = open("Day-2/input.txt")

def findMaxValue(line, type):
    maxValue = 0
    index = line.find(type)

    while index != -1:

        if line[index-3].isdigit():
            value = int(line[index-3:index-1])
        else:
            value = int(line[index-2])

        if value > maxValue:
            maxValue = value
        line = line[:index-2] + line[index+len(type):]
        index = line.find(type)
    
    return maxValue



gesamt = 0


for line in document:
    maxRed = findMaxValue(line, "red")
    maxGreen = findMaxValue(line, "green")
    maxBlue = findMaxValue(line, "blue")

    gesamt += maxRed*maxGreen*maxBlue

print(gesamt)