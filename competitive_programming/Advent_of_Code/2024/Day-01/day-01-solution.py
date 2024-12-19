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

part1()


# --- Part Two ---

