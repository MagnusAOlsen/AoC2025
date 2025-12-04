with open("input.txt", "r") as f:
    data = f.read().split(",")
totalSum = 0
for id_range in data:
    endpoints = id_range.split("-")
    secondary_range = [x for x in range(int(endpoints[0]), int(endpoints[1]) + 1)]
    for number in secondary_range:
        totalSum += number if str(number)[:int(len(str(number))/2)] == str(number)[int(len(str(number))/2):] and str(number)[0] != 0 else 0

print(totalSum)