def isNumberValid():
    validNumber = False

    index = indexZahl-len(zahl)


    if line[index] != "." or line[index+len(zahl)+1] != ".":
        validNumber = True
    else:
        while index <= indexZahl+1:
            if input[lineIndex-1][index] != "." or input[lineIndex+1][index] != ".":
                validNumber = True
                break
            index+=1
    
    return validNumber





file = open("Day-3/input.txt")

input = [".............................................................................................................................................."]

for x in file:
    input.append("." + x[:-1] + ".")

input.append("..............................................................................................................................................")

lineIndex = 0

zahl = ""

output = 0


for line in input:
    indexZahl = 0
    
    for character in line:
        if character.isdigit():
            zahl += character

            if not line[indexZahl+1].isdigit():
                if isNumberValid():
                    output += int(zahl)

                zahl = ""
        
        indexZahl+=1

    lineIndex += 1


print(output)