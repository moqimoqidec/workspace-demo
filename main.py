import math

def calculate_hypotenuse(a, b):
    return math.sqrt(a**2 + b**2)

def main():
    # 多组输入
    inputs = [
        (3, 4),
        (5, 12),
        (8, 15)
    ]
    
    for a, b in inputs:
        hypotenuse = calculate_hypotenuse(a, b)
        print(f"The hypotenuse of a right triangle with sides {a} and {b} is {hypotenuse}")

if __name__ == "__main__":
    main()
