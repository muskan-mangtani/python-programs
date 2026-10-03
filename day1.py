def add_numbers(num1, num2):
    """Adds two numbers together and returns the total."""
    result = num1 + num2
    return result

def greet_user(name):
    """Greets the user by their name."""
    print(f"Hello, {name}! Welcome to Python functions.")

# Testing the functions
if __name__ == "__main__":
    # 1. Test the greeting function
    greet_user("Developer")
    
    # 2. Test the math function
    total = add_numbers(5, 7)
    print(f"5 + 7 equals {total}")
