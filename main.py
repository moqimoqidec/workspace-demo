import math

def calculate_hypotenuse(a, b):
    """
    Calculate the hypotenuse of a right triangle given the lengths of the other two sides.

    Parameters:
    a (float): The length of one of the shorter sides of the triangle.
    b (float): The length of the other shorter side of the triangle.

    Returns:
    float: The length of the hypotenuse of the triangle.
    """
    if a < 0 or b < 0:
        raise ValueError("The lengths of the sides must be non-negative.")
    return math.sqrt(a**2 + b**2)

def main():
    inputs = [
        (3, 4),
        (5, 12),
        (8, 15),
        (-3, 4),
    ]
    
    for a, b in inputs:
        try:
            hypotenuse = calculate_hypotenuse(a, b)
            print(f"The hypotenuse of a right triangle with sides {a} and {b} is {hypotenuse}")
        except ValueError as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    main()
