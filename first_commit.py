# Sample Python Code

def greet(name):
    """A simple greeting function"""
    return f"Hello, {name}!"

def add(a, b):
    """Add two numbers"""
    return a + b

def factorial(n):
    """Calculate factorial of n"""
    if n <= 1:
        return 1
    return n * factorial(n - 1)

if __name__ == "__main__":
    # Test the functions
    print(greet("World"))
    print(f"5 + 3 = {add(5, 3)}")
    print(f"Factorial of 5 = {factorial(5)}")
