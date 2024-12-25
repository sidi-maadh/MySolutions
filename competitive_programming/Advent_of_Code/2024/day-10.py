from dataclasses import dataclass

grid = []
with open('input.txt', 'r') as f:
    for i, line in enumerate(f.readlines()):
        grid.append([int(x) for x in line.strip()])
n = len(grid)
m = len(grid[0])

@dataclass(frozen=True)
class Pos:
    i: int
    j: int
    def __add__(self, other):
        return Pos(self.i + other.i, self.j + other.j)
    def __eq__(self, other):
        return isinstance(other, Pos) and (self.i, self.j) == (other.i, other.j)
    def __hash__(self):
        return hash((self.i, self.j))
    def is_inbounds(self):
        return 0 <= self.i < n and 0 <= self.j < m
    def get_nbrs(self):
        for delta in (Pos(0, 1), Pos(0, -1), Pos(1, 0), Pos(-1, 0)):
            if (self+delta).is_inbounds():
                yield self + delta

def dfs(start):
    peaks = set()
    rating = 0
    q = [start]
    while q:
        current = q.pop()
        if grid[current.i][current.j] == 9:
            rating += 1
            peaks.add(current)
        for nbr in current.get_nbrs():
            if grid[nbr.i][nbr.j] == 1 + grid[current.i][current.j]:
                q.append(nbr)
    return len(peaks), rating

score, rating = 0, 0
for i in range(n):
    for j in range(m):
        if grid[i][j] == 0:
            s, r = dfs(Pos(i, j))
            score += s
            rating += r
            
            
print(f"Part One : {score}")
print(f"Part Two : {rating}")
