with open("input.txt", "r") as f:
    data = f.readlines()
    totalScore = 0
    for line in data:
        line = line.strip()
        count = 0
        previous_biggest = ""
        number = ""
        while count < 12:
            biggest = max(line[:-11 + count]) if count < 11 else max(line)
            number += biggest
            previous_biggest = biggest
            count += 1
            line = line[line.index(previous_biggest) + 1:]
        totalScore += int(number)

print(totalScore)