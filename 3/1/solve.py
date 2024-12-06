import re

# Read the input file
with open(r".\3\1\input.txt", "r", encoding="utf-8") as file:
    memory = file.read()

# Regular expression to find valid "mul(X,Y)" patterns
pattern = r"mul\(\s*(\d{1,3})\s*,\s*(\d{1,3})\s*\)"

# Find all matches
matches = re.findall(pattern, memory)

# Calculate the sum of all results
result_sum = sum(int(x) * int(y) for x, y in matches)

# Print the result
print(f"Sum of all valid multiplications: {result_sum}")
