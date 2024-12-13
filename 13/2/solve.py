def solve_claw_machine(buttons, prize, offset=10**13):
    """
    Solve the claw machine problem using direct calculation.
    """
    a_x, a_y, a_cost = buttons[0]
    b_x, b_y, b_cost = buttons[1]

    # Adjust the prize coordinates by the offset
    target_x, target_y = prize[0] + offset, prize[1] + offset

    # Calculate determinant
    det = a_x * b_y - a_y * b_x
    if det == 0:
        return None  # No solution if determinant is zero

    # Solve for the number of presses
    a_presses = (target_x * b_y - target_y * b_x) // det
    b_presses = (a_x * target_y - a_y * target_x) // det

    # Verify the solution
    if (a_x * a_presses + b_x * b_presses, a_y * a_presses + b_y * b_presses) == (
        target_x,
        target_y,
    ):
        return a_presses * a_cost + b_presses * b_cost

    return None


def calculate_minimum_tokens(claw_machines):
    """
    Calculate the minimum tokens required to win all possible prizes.
    """
    total_tokens = 0
    for index, (buttons, prize) in enumerate(claw_machines):
        print(f"Processing claw machine {index + 1}/{len(claw_machines)}...")
        cost = solve_claw_machine(buttons, prize)
        if cost is not None:
            print(f"Claw machine {index + 1}: Cost to win prize = {cost}")
            total_tokens += cost
        else:
            print(f"Claw machine {index + 1}: Prize cannot be won.")
    return total_tokens


# Read the input file
with open(r".\13\2\input.txt", "r", encoding="utf-8") as file:
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
            lines[i + 2].split(": ")[1].replace("X=", "").replace("Y=", "").split(", "),
        )
    )

    claw_machines.append(([button_a, button_b], prize))

# Calculate the minimum tokens required
result = calculate_minimum_tokens(claw_machines)

# Print the result
print(f"Minimum tokens required to win all possible prizes: {result}")
