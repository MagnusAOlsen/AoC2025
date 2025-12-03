with open("input.txt", "r") as f:
    data = f.readlines()
    totalSum = 0
    for line in data:
        line = line.strip()
        biggest = max(line[:-1])
        next_biggest = max(line[line.index(biggest) + 1:])
        totalSum += int(biggest + next_biggest)

print(totalSum)


