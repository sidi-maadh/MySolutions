from dataclasses import dataclass

grid = []
with open('input.txt', 'r') as f:
    for i, line in enumerate(f.readlines()):
        row = line.strip()
        if '^' in row:
            start = (i, row.find('^'))
            row = row.replace('^', '.')
        grid.append(row)
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
    def rotate_right(self):
        return Pos(self.j, -self.i)

def is_inbounds(p):
    return 0 <= p.i < n and 0 <= p.j < m

def get_guard_span(new_obstacle=None):
    # returns a set of visited positions by the guard
    # second value returns bool to indicate success of looping guard
    # option to add additional obstacle position
    pos = Pos(start[0], start[1])
    direction = Pos(-1, 0)  # up
    visited = set()
    states = {(pos, direction)}
    while is_inbounds(pos):
        visited.add(pos)
        # try to take a step
        dest = pos + direction
        if is_inbounds(dest) and (grid[dest.i][dest.j] == '#' or dest == new_obstacle):
            # turn right
            direction = direction.rotate_right()
        else:
            # step forward
            pos = dest
        new_state = (pos, direction)
        if new_state in states:
            # infinite loop detected
            return True, visited
        states.add(new_state)
    return False, visited

# part 1
visited = get_guard_span()[1]
print(f"Part One : {len(visited)}")

# part 2
result = 0
obstacle_candidates = visited - {start}
for obstacle in obstacle_candidates:
    if get_guard_span(obstacle)[0]:
        result += 1
print(f"Part Two : {result}")
