import numpy as np

with open ("input.txt", "r") as f:
    # lineNr=1
    totalSum = 0
    startNumber = 50
    currentNumber = startNumber
    numbers = [x for x in range(0,100)]
    data = f.readlines()
    for line in data:
        tick = False
        count = 0
        line = line.strip()
        
        if (line[0] == "R"):
            number_before_change = currentNumber
            myNumber = (number_before_change + int(line[1:]))
            currentNumber = myNumber % len(numbers)
            if myNumber > 99:
                count = np.floor(myNumber / len(numbers))
            elif currentNumber == 0:
                tick = True

        else:
            number_before_change = currentNumber
            currentNumber = (number_before_change - int(line[1:])) % len(numbers)
            if currentNumber == 0:
                tick = True

            if (number_before_change - int(line[1:])) < 0:
                myNumber = (number_before_change - int(line[1:])) * (-1)
                count = np.ceil(myNumber / len(numbers))
                count = count - 1 if number_before_change == 0 else count
                
        
        if tick and count > 0:
            totalSum += (count + 1)

        elif currentNumber == 0 and count < 1:
            totalSum+=1

        elif count > 0:
            totalSum += count

        """ print("------------------")
        print("LINEnR: " + str(lineNr))
        print("LINE: " + line)
        print("NUMBER BEFORE CHANGE: " + str(number_before_change))
        print("NUMBER AFTER CHANGE: " + str(currentNumber))
        print("COUNT: " + str(count))
        print("TOTALSUM: " + str(totalSum))
        print("------------------")
        lineNr += 1 """

       

print(totalSum)


    

