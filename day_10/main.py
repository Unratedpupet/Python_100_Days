from art import logo

def add(n1, n2):
    """Adds two numbers together

    Args:
        n1 (int or float): First number to be added
        n2 (int or float): Second number to be added

    Returns:
        int or float: The sum of n1 and n2
    """
    return n1 + n2

def subtract(n1, n2):
    """Subtracts n2 from n1

    Args:
        n1 (int or float): The number to be subtracted from
        n2 (int or float): The number being subtracted

    Returns:
        int or float: The difference between n1 and n2
    """
    return n1 - n2

def multiply(n1, n2):
    """Produces the product of n1 and n2

    Args:
        n1 (int or float): First number being multiplied
        n2 (int or float): Second number being multiplied

    Returns:
        int or float: Product of n1 and n2
    """
    return n1 * n2

def divide(n1, n2):
    """Division of n1 by n2

    Args:
        n1 (int or float): Number being divided
        n2 (int or float): Number doing division

    Returns:
        float: Quotient of n1 and n2
    """
    if n2 != 0:
        return n1 / n2
    else:
        return "Cannot divide by zero."
    

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

print(logo)

should_continue = True

num1 = int(input("What is the first number? "))

# Prints out the operation list
for key in operations.keys():
        print(key)



while should_continue:

    operation_symbol = input("Pick an operation: ")

    num2 = int(input("What is the second number? "))

    # Calculates the answer by finding the value from the operation_symbol function to call the appropriate function
    answer = operations[operation_symbol](num1, num2)

    print(f"{num1} {operation_symbol} {num2} = {answer}.")
    num1 = answer
    

    question = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to exit: ")
    if question != 'y':
        should_continue = False
    
