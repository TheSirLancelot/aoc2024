# Read the input file
from collections import Counter

with open(r".\1\2\input.txt", "r", encoding="utf8") as file:
    left_list = []
    right_list = []
    for line in file:
        left, right = map(int, line.strip().split())
        left_list.append(left)
        right_list.append(right)

# Count occurrences in the right list
right_count = Counter(right_list)

# Calculate the total similarity score
total_similarity_score = sum(left * right_count[left] for left in left_list)

# Print the result
print(f"Total similarity score: {total_similarity_score}")
