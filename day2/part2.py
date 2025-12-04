def check_combination(number, characters_in_row, total_length) -> bool:
    parts = total_length // characters_in_row
    all_parts = []
    for i in range(parts):
        all_parts.append(number[characters_in_row * i: characters_in_row * (i + 1)])
    return all(x == all_parts[0] for x in all_parts)

def main() -> int:
    with open("input.txt", "r") as f:
        data = f.read().split(",")
    totalScore = 0
    for id_range in data:
        endpoints = id_range.split("-")
        secondary_range = [x for x in range(int(endpoints[0]), int(endpoints[1]) + 1)]
        for number in secondary_range:
            count = 1
            while len(str(number))//2 >= count:
                if len(str(number)) % count != 0:
                    count+=1
                    continue
                finished = check_combination(str(number), count, len(str(number)))
                if finished:
                    totalScore += number
                    break
                count += 1
    return totalScore
    
print(main())
                

