def simulate_guard_patrol(grid):
    rows = len(grid)
    cols = len(grid[0])

    # Directions and how they move
    directions = {
        "^": (-1, 0),  # up
        ">": (0, 1),  # right
        "v": (1, 0),  # down
        "<": (0, -1),  # left
    }

    direction_order = ["^", ">", "v", "<"]

    # find the initial position
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] in directions:
                guard_pos = (r, c)
                guard_dir = grid[r][c]
                break

    visited = set()
    visited.add(guard_pos)

    while True:
        # figure out the guard's direction
        dr, dc = directions[guard_dir]
        next_pos = (guard_pos[0] + dr, guard_pos[1] + dc)

        # check if the guard will leave
        if not (0 <= next_pos[0] < rows and 0 <= next_pos[1] < cols):
            break

        # check if the next step is an obstacle
        if grid[next_pos[0]][next_pos[1]] == "#":
            # turn right
            current_index = direction_order.index(guard_dir)
            # increment current index but rollover to the beginning if we overflow
            guard_dir = direction_order[(current_index + 1) % len(direction_order)]
        else:
            # keep walking
            guard_pos = next_pos
            visited.add(guard_pos)

    return len(visited)


# read the input:
with open(r".\6\1\input.txt", "r", encoding="utf-8") as file:
    grid = [list(line.strip()) for line in file]

result = simulate_guard_patrol(grid)

print(result)
