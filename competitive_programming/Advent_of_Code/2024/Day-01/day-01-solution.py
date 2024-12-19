import re

# --- Part One ---
def part1():
    lines = []

    with open("input.txt") as file:
        lines = file.readlines()

    first_list = []
    second_list = []

    for line in lines:
        line = line.strip()  # Enlever les espaces et les retours à la ligne
        if line:  # Si la ligne n'est pas vide
            parts = line.split(' ')
            first_list.append(int(re.sub(r'\D', '', parts[0])))  # Garder uniquement les chiffres
            second_list.append(int(re.sub(r'\D', '', parts[-1])))  # Garder uniquement les chiffres

    first_list.sort()
    second_list.sort()

    total = 0
    for i in range(len(first_list)):
        total += abs(first_list[i] - second_list[i])

    print(total)


# --- Part Two ---
def part2():
    lines = []

    with open("input.txt") as file:
        lines = file.readlines()

    location_list = []
    frequency_map = {}

    for line in lines:
        line = line.strip()  # Enlever les espaces et les retours à la ligne
        if line:  # Si la ligne n'est pas vide
            parts = line.split(' ')
            location_list.append(int(re.sub(r'\D', '', parts[0])))  # Garder uniquement les chiffres

            frequency_key = int(re.sub(r'\D', '', parts[-1]))
            frequency_map[frequency_key] = frequency_map.get(frequency_key, 0) + 1


    similarity_score = 0
    for i in range(len(location_list)):
        if frequency_map.get(location_list[i], 0) != 0:
            similarity_score += location_list[i] * frequency_map[location_list[i]]

    print(similarity_score)


if __name__ == "__main__":

    part1() 
    part2()
