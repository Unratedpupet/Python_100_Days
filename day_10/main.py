from art import logo

print(logo)

# What is the first number
# Pick an operation
# What is the next number
# Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation


# Create functions for each +, -, *, /.


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
    
    
    
