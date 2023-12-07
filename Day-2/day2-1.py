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



addedIDs = 0

countID = 1


for line in document:
    maxRed = findMaxValue(line, "red")
    maxGreen = findMaxValue(line, "green")
    maxBlue = findMaxValue(line, "blue")

    if maxRed <= 12 and maxGreen <= 13 and maxBlue <= 14:
        addedIDs += countID
    
    countID+=1

print(addedIDs)
