from itertools import product

def is_valid_equation(test_value, equation, operator_symbols):
    for operators in product(operator_symbols, repeat=len(equation)-1):
        p = equation[0]
        for i, o in enumerate(operators):
            if o == '+':
                p += equation[i+1]
            elif o == '*':
                p *= equation[i+1]
            elif o == '|':
                p = int(str(p) + str(equation[i+1]))
            if p > test_value:
                break
        if p == test_value:
            return True
    return False

result1, result2 = 0, 0
with open('input.txt', 'r') as f:
    for i, line in enumerate(f.readlines()):
        ints = line.strip().split()
        test_value = int(ints[0][:-1])
        equation = [int(x) for x in ints[1:]]
        if is_valid_equation(test_value, equation, '+*'):
            result1 += test_value
        if is_valid_equation(test_value, equation, '+*|'):
            result2 += test_value


# Result
print(f"Part One : {result1}")
print(f"Part Two : {result2}")
