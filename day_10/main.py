from art import logo


def add(n1, n2):
    """Adds two numbers together

    Args:
        n1 (float): First number to be added
        n2 (float): Second number to be added

    Returns:
        float: The sum of n1 and n2
    """
    return n1 + n2


def subtract(n1, n2):
    """Subtracts n2 from n1

    Args:
        n1 (float): The number to be subtracted from
        n2 (float): The number being subtracted

    Returns:
        float: The difference between n1 and n2
    """
    return n1 - n2


def multiply(n1, n2):
    """Produces the product of n1 and n2

    Args:
        n1 (float): First number being multiplied
        n2 (float): Second number being multiplied

    Returns:
        float: Product of n1 and n2
    """
    return n1 * n2


def divide(n1, n2):
    """Division of n1 by n2

    Args:
        n1 (float): Number being divided
        n2 (float): Number doing division

    Returns:
        float: Quotient of n1 and n2
    """
    if n2 != 0:
        return n1 / n2
    else:
        return "Cannot divide by zero."


operations = {"+": add, "-": subtract, "*": multiply, "/": divide}


def calculator():
    should_continue = True
    num1 = float(input("What is the first number? "))

    # Prints out the operation list
    for key in operations.keys():
        print(key)

    while should_continue:

        operation_symbol = input("Pick an operation: ")

        num2 = float(input("What is the second number? "))

        # Calculates the answer by finding the value from the operation_symbol function to call the appropriate function
        answer = operations[operation_symbol](num1, num2)

        print(f"{num1} {operation_symbol} {num2} = {answer}.")

        question = input(
            f"Type 'y' to continue calculating with {answer} or type 'n' to start a new calculation or type 'q' to quit: "
        )
        if question == "y":
            num1 = answer
        elif question == "n":
            should_continue = False
            calculator()
        else:
            exit()


print(logo)


calculator()
