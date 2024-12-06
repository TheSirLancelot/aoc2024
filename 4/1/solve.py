def count_xmas_occurrences(grid):
    rows = len(grid)
    cols = len(grid[0])
    word = "XMAS"
    word_len = len(word)
    directions = [
        (0, 1),  # Right
        (1, 0),  # Down
        (1, 1),  # Diagonal Down-Right
        (-1, 1),  # Diagonal Up-Right
        (0, -1),  # Left
        (-1, 0),  # Up
        (-1, -1),  # Diagonal Up-Left
        (1, -1),  # Diagonal Down-Left
    ]

    def is_valid(x, y):
        return 0 <= x < rows and 0 <= y < cols

    def search_from(x, y, dx, dy):
        for i in range(word_len):
            nx, ny = x + i * dx, y + i * dy
            if not is_valid(nx, ny) or grid[nx][ny] != word[i]:
                return False
        return True

    count = 0

    for i in range(rows):
        for j in range(cols):
            for dx, dy in directions:
                if search_from(i, j, dx, dy):
                    count += 1

    return count


# Read the word search grid from the input file
with open(r".\4\1\input.txt", "r", encoding="utf-8") as file:
    grid = [list(line.strip()) for line in file]

# Count the occurrences of "XMAS"
occurrences = count_xmas_occurrences(grid)

# Print the result
print(f"Total occurrences of XMAS: {occurrences}")
