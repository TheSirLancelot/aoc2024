from itertools import product


def find_cheapest(buttons, prize, max_presses=100):
    # they hinted that you don't have to press more than 100 so we're using that for now
    a_x, a_y, a_cost = buttons[0]  # Button A configuration
    b_x, b_y, b_cost = buttons[1]  # Button B configuration
    target_x, target_y = prize

    min_cost = float("inf")  # infinity

    for a_presses, b_presses in product(range(max_presses + 1), repeat=2):
        # calculate the final position after pressing buttons
        total_x = a_presses * a_x + b_presses * b_x
        total_y = a_presses * a_y + b_presses * b_y

        # see if it matches our prize location
        if total_x == target_x and total_y == target_y:
            # figure out how much it costs
            cost = a_presses * a_cost + b_presses * b_cost
            min_cost = min(min_cost, cost)

    return min_cost if min_cost != float("inf") else None


def calculate_min_tokens(claw_machines):
    total_tokens = 0
    for buttons, prize in claw_machines:
        cost = find_cheapest(buttons, prize)
        if cost is not None:
            total_tokens += cost

    return total_tokens


# read the input and grab the machine info
with open(r".\13\1\input.txt", "r", encoding="utf-8") as file:
    lines = [line.strip() for line in file if line.strip()]

    claw_machines = []

    for i in range(0, len(lines), 3):
        button_a = tuple(
            map(
                int,
                lines[i]
                .split(": ")[1]
                .replace("X+", "")
                .replace("Y+", "")
                .replace(",", "")
                .split(),
            )
        ) + (3,)
        button_b = tuple(
            map(
                int,
                lines[i + 1]
                .split(": ")[1]
                .replace("X+", "")
                .replace("Y+", "")
                .replace(",", "")
                .split(),
            )
        ) + (1,)
        prize = tuple(
            map(
                int,
                lines[i + 2]
                .split(": ")[1]
                .replace("X=", "")
                .replace("Y=", "")
                .split(", "),
            )
        )
        claw_machines.append(([button_a, button_b], prize))

# calculate the minimum tokens required
result = calculate_min_tokens(claw_machines)

# print the result
print(result)
