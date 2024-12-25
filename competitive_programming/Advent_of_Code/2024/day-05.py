from collections import defaultdict

def top_sort(l, edge_list):
    # find a valid topological sort of l, given directed edge list
    nodes = set(l)
    result = []
    unvisited = set(l)
    def visit(n):
        if n not in unvisited:
            return
        for nbr in edge_list[n]:
            if nbr not in nodes:
                continue
            visit(nbr)
        unvisited.remove(n)
        result.append(n)
    while unvisited:
        for x in unvisited:
            break
        visit(x)
    return result[::-1]

result1, result2 = 0, 0
edge_list = defaultdict(set)
with open('input.txt', 'r') as f:
    is_section_one = True
    for line in f.readlines():
        if not line.strip():
            is_section_one = False
            continue
        if is_section_one:
            # section 1
            x, y = (int(z) for z in line.split('|'))
            edge_list[x].add(y)
        else:
            # section 2
            l = [int(z) for z in line.strip().split(',')]
            valid = True
            # check for violations
            for i in range(len(l)):
                for j in range(i+1, len(l)):
                    if l[i] in edge_list[l[j]]:
                        valid = False
                        break
                if not valid:
                    break
            if valid:
                result1 += l[len(l)//2]
            else:
                top_sorted_list = top_sort(l, edge_list)
                result2 += top_sorted_list[len(top_sorted_list) // 2]



# Result
print(f"Part One : {result1}")
print(f"Part Tow : {result2}")
