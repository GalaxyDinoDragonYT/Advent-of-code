import copy

inputFile = open('2023/Day2/Part1/test.txt', 'r')
lines = [line.strip() for line in inputFile.readlines()]
example_game_data = {
    'red': 0,
    'green': 0,
    'blue': 0
}

def readyInput():
    cleanInput = []

    for line in lines:
        gameData = line.split(':')[1]
        rounds = gameData.split(';')
        
        for round in rounds:
            specificColors = round.split(',')
            machineData = {
                'red': 0,
                'green': 0,
                'blue': 0
            }

            for colorData in specificColors:
                diffColors = ['red', 'green', 'blue']

                for color in diffColors:
                    if colorData.find(color):
                        no = colorData.replace(color, '').strip()
                        print(color)
                        machineData[color] = int(no)
                
            print(machineData)




    
    return cleanInput


cleanInput = readyInput()
