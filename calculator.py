def add(a, b):
    """Returns the sum of a and b."""
    return a + b

if __name__ == "__main__":
    import sys
    if len(sys.argv) == 3:
        try:
            num1 = float(sys.argv[1])
            num2 = float(sys.argv[2])
            print(f"{num1} + {num2} = {add(num1, num2)}")
        except ValueError:
            print("Please provide two numbers as arguments.")
    else:
        print("Usage: python calculator.py <num1> <num2>")
