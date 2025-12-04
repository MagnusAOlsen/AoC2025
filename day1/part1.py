with open("input.txt", "r") as f:
    data = f.readlines()
startNumber = 50
currentNumber = startNumber
differentNumbers = 100
totalScore = 0
for line in data:
    line = line.strip()
    currentNumber = (currentNumber + int(line[1:])) % differentNumbers if (line[0] == "R") else (currentNumber - int(line[1:])) % differentNumbers
    if currentNumber == 0: totalScore +=1

print(totalScore)
