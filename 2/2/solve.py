# Read the input file
with open(r".\2\2\input.txt", "r", encoding="utf8") as file:
    reports = [list(map(int, line.strip().split())) for line in file]


# Function to check if a report is safe
def is_safe(report):
    differences = [report[i + 1] - report[i] for i in range(len(report) - 1)]

    # Check if all differences are within [-3, -1] or [1, 3]
    if all(-3 <= diff <= -1 for diff in differences) or all(
        1 <= diff <= 3 for diff in differences
    ):
        return True
    return False


# Function to check if a report can be made safe by removing one level
def can_be_made_safe(report):
    for i in range(len(report)):
        modified_report = report[:i] + report[i + 1 :]  # Remove the i-th level
        if is_safe(modified_report):
            return True
    return False


# Count the number of safe reports, including those made safe by removing one level
safe_count = sum(1 for report in reports if is_safe(report) or can_be_made_safe(report))

# Print the result
print(f"Number of safe reports: {safe_count}")
