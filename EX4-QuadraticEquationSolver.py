# Quadratic Equation Solver

import math

# This programme calculates the resolving formula.
if __name__=='__main__':

    # 1. Input coefficients a, b and c:
    a=float(input("Enter the coefficient a: "))
    b=float(input("Enter the coefficient b: "))
    c=float(input("Enter the coefficient c: "))
    
    # 2. Calculate the discriminant:
    d=(b**2 - 4*a*c)

    # 3. Check the discriminant and compute solutions:
    if (d<0):
        print("This equation has no real solution.")
    elif (d==0):
        x = (-b + math.sqrt(d)) / (2 * a)
        print(f"This equation has one solution: {x:6.2f}")
    else:
        x1 = (-b + math.sqrt(d)) / (2 * a)
        x2 = (-b - math.sqrt(d)) / (2 * a)
        print(f"This equation has two solutions: {x1:6.2f} and {x2:6.2f}")

