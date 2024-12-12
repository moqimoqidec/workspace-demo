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
    return math.sqrt(a**2 + b**2)

def main():
    inputs = [
        (3, 4),
        (5, 12),
        (8, 15),
    ]
    
    for a, b in inputs:
        hypotenuse = calculate_hypotenuse(a, b)
        print(f"The hypotenuse of a right triangle with sides {a} and {b} is {hypotenuse}")

if __name__ == "__main__":
    main()
