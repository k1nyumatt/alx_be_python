task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ")
time_bound = input("Is it time-bound? (yes/no): ")

# Process the Task Based on Priority
match priority:
    case "high":
        reminder = f"'{task}' is a high priority task"
    case "medium":
        reminder = f"'{task}' is a medium priority task"
    case "low":
        reminder = f"'{task}' is a low priority task"
    case _:
        reminder = f"'{task}' has an unknown priority"

# Modify reminder based on time sensitivity
if time_bound == "yes":
    reminder += " that requires immediate attention today!"

# Print the customized reminder
print(f"Reminder: {reminder}")