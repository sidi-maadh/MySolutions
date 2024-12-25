from dataclasses import dataclass
from collections import defaultdict
import math

grid = []
with open('input.txt', 'r') as f:
    for i, line in enumerate(f.readlines()):
        grid.append(line.strip())
n = len(grid)
m = len(grid[0])

@dataclass(frozen=True)
class Pos:
    i: int
    j: int
    def __add__(self, other):
        return Pos(self.i + other.i, self.j + other.j)
    def __sub__(self, other):
        return Pos(self.i - other.i, self.j - other.j)
    def __eq__(self, other):
        return isinstance(other, Pos) and (self.i, self.j) == (other.i, other.j)
    def __hash__(self):
        return hash((self.i, self.j))
    def is_inbounds(self):
        return 0 <= self.i < n and 0 <= self.j < m
    def get_gcd_vec(self):
        gcd = math.gcd(self.i, self.j)
        return Pos(self.i // gcd, self.j // gcd)

# populate dict of frequency -> [antenna positions]
antennae = defaultdict(list)
for i in range(n):
    for j in range(m):
        if grid[i][j] != '.':
            antennae[grid[i][j]].append(Pos(i, j))
print(antennae)

antinodes_p1 = set()
antinodes_p2 = set()
for antenna_group in antennae.values():
    for i, a1 in enumerate(antenna_group):
        for j in range(i+1, len(antenna_group)):
            a2 = antenna_group[j]
            vec = a2-a1
            # part 1
            anti1 = vec + a2
            anti2 = a1 - vec
            if anti1.is_inbounds():
                antinodes_p1.add(anti1)
            if anti2.is_inbounds():
                antinodes_p1.add(anti2)
            # part 2
            gcd_vec = vec.get_gcd_vec()
            temp = a1
            while temp.is_inbounds():
                antinodes_p2.add(temp)
                temp += gcd_vec
            temp = a1
            while temp.is_inbounds():
                antinodes_p2.add(temp)
                temp -= gcd_vec


print(f"Part One : {len(antinodes_p1)}")
print(f"Part Two : {len(antinodes_p2)}")
