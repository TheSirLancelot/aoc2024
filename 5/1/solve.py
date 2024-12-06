def is_update_correct(order_rules, update):
    """Check if an update follows the given order rules."""
    # Create a mapping of page positions for quick comparison
    page_positions = {page: idx for idx, page in enumerate(update)}

    for before, after in order_rules:
        # If both pages are in the update, ensure the order is correct
        if before in page_positions and after in page_positions:
            if page_positions[before] > page_positions[after]:
                return False

    return True


def calculate_middle_pages_sum(order_rules, updates):
    """Calculate the sum of middle pages for correctly ordered updates."""
    total_sum = 0

    for update in updates:
        if is_update_correct(order_rules, update):
            middle_index = len(update) // 2
            total_sum += update[middle_index]

    return total_sum


# Read the input file
with open(r".\5\1\input.txt", "r", encoding="utf-8") as file:
    lines = [line.strip() for line in file]

# Separate the rules and updates
rules_section, updates_section = "\n".join(lines).split("\n\n")

# Parse the rules
order_rules = []
for line in rules_section.split("\n"):
    before, after = map(int, line.split("|"))
    order_rules.append((before, after))

# Parse the updates
updates = []
for line in updates_section.split("\n"):
    updates.append(list(map(int, line.split(","))))

# Calculate the sum of middle pages for correctly ordered updates
result = calculate_middle_pages_sum(order_rules, updates)

# Print the result
print(f"Sum of middle pages from correctly-ordered updates: {result}")
