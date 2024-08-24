from art import logo
print(logo)
def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

# Dictionary to map operators to their corresponding functions
operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

def calculator():
    # Start with no previous result
    previous_result = None
    memory = []  # List to store previous results

    while True:
        # Use previous result if the user wants to continue, otherwise ask for a new first number
        if previous_result is None:
            num1 = float(input("Enter the first number: "))
        else:
            num1 = previous_result

        operator = input("Enter an operator (+, -, *, /): ")

        # Ask for the second number
        num2 = float(input("Enter the second number: "))

        # Perform the operation based on user input
        if operator in operations:
            result = operations[operator](num1, num2)
            print(f"Result: {result}")
        else:
            print("Invalid operator, please try again.")
            continue

        # Store the result in memory
        memory.append(result)

        # Ask the user if they want to continue with the current result
        continue_with_result = input("Do you want to continue with this result? (yes/no): ").strip().lower()

        if continue_with_result == "yes":
            previous_result = result
        elif continue_with_result == "no":
            # Reset the previous result but keep the memory
            previous_result = None
            print("Restarting calculator...")
        else:
            print("Invalid input, starting over.")
            previous_result = None

        # Ask the user if they want to view all previous results
        view_memory = input("Do you want to view all previous results? (yes/no): ").strip().lower()
        if view_memory == "yes":
            print("Previous Results:", memory)
        elif view_memory != "no":
            print("Invalid input, continuing...")

# Start the calculator
calculator()
