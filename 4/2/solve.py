def count_x_mas_occurrences(grid):
    rows = len(grid)
    cols = len(grid[0])

    # Define the specific X-MAS patterns for forward and backward MAS
    patterns = [
        [
            (-1, -1),
            (0, 0),
            (1, 1),
            (-1, 1),
            (1, -1),
        ],  # Diagonal top-left to bottom-right
        [
            (-1, 1),
            (0, 0),
            (1, -1),
            (-1, -1),
            (1, 1),
        ],  # Diagonal top-right to bottom-left
        [
            (-1, -1),
            (0, 0),
            (1, 1),
            (1, -1),
            (-1, 1),
        ],  # Reverse diagonal bottom-right to top-left
        [
            (-1, 1),
            (0, 0),
            (1, -1),
            (1, 1),
            (-1, -1),
        ],  # Reverse diagonal bottom-left to top-right
    ]

    def is_valid(x, y):
        return 0 <= x < rows and 0 <= y < cols

    def matches_x_mas(x, y, pattern):
        # Check for two MAS patterns forming an X
        required_forward = ["M", "A", "S"]
        required_backward = ["S", "A", "M"]
        indices = [0, 0]  # Track progress for forward and backward

        for dx, dy in pattern:
            nx, ny = x + dx, y + dy
            if not is_valid(nx, ny):
                return False

            # Match forward or backward patterns
            if grid[nx][ny] == required_forward[indices[0]]:
                indices[0] += 1
                if indices[0] == len(required_forward):
                    indices[0] = 0  # Reset for overlap
            elif grid[nx][ny] == required_backward[indices[1]]:
                indices[1] += 1
                if indices[1] == len(required_backward):
                    indices[1] = 0  # Reset for overlap
            else:
                return False

        # Ensure both diagonals are valid
        return indices[0] == 0 or indices[1] == 0

    count = 0

    for i in range(rows):
        for j in range(cols):
            for pattern in patterns:
                if matches_x_mas(i, j, pattern):
                    count += 1

    return count


# Read the word search grid from the input file
with open(r".\4\2\input.txt", "r", encoding="utf-8") as file:
    grid = [list(line.strip()) for line in file]

# Count the occurrences of "X-MAS"
occurrences = count_x_mas_occurrences(grid)

# Print the result
print(f"Total occurrences of X-MAS: {occurrences}")
