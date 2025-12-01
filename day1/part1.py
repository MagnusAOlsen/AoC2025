with open("input.txt", "r") as f:
    startNumber = 50
    currentNumber = startNumber
    differentNumbers = 100
    totalScore = 0
    data = f.readlines()
    for line in data:
        line = line.strip()
        currentNumber = (currentNumber + int(line[1:])) % differentNumbers if (line[0] == "R") else (currentNumber - int(line[1:])) % differentNumbers
        if currentNumber == 0: totalScore +=1

        """ print("CURRENT: " + str(currentNumber))
        print("TOTAL: " + str(totalScore)) """


print(totalScore)
