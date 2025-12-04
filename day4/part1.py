with open("input.txt", "r") as f:
    data = f.readlines()
    
totalRolls = 0
my_dict = {x: {y: 0 for y in range(len(data) + 2)} for x in range(len(data)+2)}
for line in range(len(data)):
    for character in range(len(data[line].strip())):
        if data[line][character] == "@":
            my_dict[line][character] += 1
            my_dict[line][character + 1] += 1
            my_dict[line][character + 2] += 1
            my_dict[line + 1][character] += 1
            my_dict[line + 1][character + 2] += 1
            my_dict[line + 2][character] += 1
            my_dict[line + 2][character + 1] += 1
            my_dict[line + 2][character + 2] += 1

my_dict.pop(0)
my_dict.pop(len(data) + 1)
for lineNr, characters in my_dict.items():
    for characterNr, score in characters.items():
        requirements = score < 4 and characterNr < 136 and characterNr > 0 and data[lineNr-1][characterNr-1] == "@" 
        totalRolls += 1 if requirements else 0

print(totalRolls)
