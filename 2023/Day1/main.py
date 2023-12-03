inputFile = open('input.txt', 'r')
lines = inputFile.readlines()
alphabet = ['\n', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def dealWithString(splitString):
    toReturn = ''

    if len(splitString) < 2:
        firstVal = splitString[0]

        splitString.append(firstVal)
        toReturn.join(splitString)
    elif not isinstance(len(splitString)/2, int):
        print(len(splitString)/2)
    else:
        toReturn.join(splitString)

    return toReturn

def setup():
    toReturn = []

    for _, line in enumerate(lines):
        splitString = [char for char in line if not str(char).lower() in alphabet]
        dealtWithString = dealWithString(splitString)

        toReturn.append(dealtWithString)
    
    return toReturn

allValues = setup()

current = 0

for value in allValues:
    current += int(value)

print(f'Final result: ', current)