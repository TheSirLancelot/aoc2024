# Read the input file
with open(r".\1\1\input.txt", "r", encoding="utf8") as file:
    left_list = []
    right_list = []
    for line in file:
        left, right = map(int, line.strip().split())
        left_list.append(left)
        right_list.append(right)

# Sort both lists
left_list.sort()
right_list.sort()

# Calculate the total distance
total_distance = sum(abs(l - r) for l, r in zip(left_list, right_list))

# Print the result
print(f"Total distance: {total_distance}")
