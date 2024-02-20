# Quadratic Equation Solver with Imaginary Numbers

import math
import cmath

# This programme calculates the resolving formula with imaginary numbers.
if __name__=='__main__':

    print("***FACTORING a * x^2 + b * x + c WITH IMAGINARY NUMBERS***")

    # 1. Input coefficients a:
    a=0
    while(a==0):
        a=float(input("Enter the coefficient a: "))
        if(a==0):
            print("Value of a can't be zero.")
    
    # 2. Input coefficients b and c:
    b=float(input("Enter the coefficient b: "))
    c=float(input("Enter the coefficient c: "))
    
    # 3. Calculate the discriminant:
    d=(b**2 - 4*a*c)

    # 4. Check the discriminant and compute solutions:
    if (d<0):
        x1 = (-b + cmath.sqrt(d)) / (2 * a)
        x2 = (-b - cmath.sqrt(d)) / (2 * a)
        print(f"This equation has two solutions: {x1:6.2f} and {x2:6.2f}")
    elif (d==0):
        x = (-b + math.sqrt(d)) / (2 * a)
        print(f"This equation has one solution: {x:6.2f}")
    else:
        x1 = (-b + math.sqrt(d)) / (2 * a)
        x2 = (-b - math.sqrt(d)) / (2 * a)
        print(f"This equation has two solutions: {x1:6.2f} and {x2:6.2f}")