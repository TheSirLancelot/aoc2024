import re

# Read the input file
with open(r".\3\2\input.txt", "r", encoding="utf-8") as file:
    memory = file.read()

# Regular expression to find valid "mul(X,Y)" patterns and control instructions
mul_pattern = r"mul\(\s*(\d{1,3})\s*,\s*(\d{1,3})\s*\)"
do_pattern = r"do\(\)"
dont_pattern = r"don't\(\)"

# Split memory into tokens to process in order
tokens = re.split(f"({mul_pattern}|{do_pattern}|{dont_pattern})", memory)

# Initialize state
enabled = True
result_sum = 0

# Process each token
for token in tokens:
    if not token or token.isspace():
        continue

    # Check for control instructions
    if re.match(do_pattern, token):
        enabled = True
    elif re.match(dont_pattern, token):
        enabled = False

    # Check for mul instructions
    match = re.match(mul_pattern, token)
    if match and enabled:
        x, y = map(int, match.groups())
        result_sum += x * y

# Print the result
print(f"Sum of all enabled multiplications: {result_sum}")
