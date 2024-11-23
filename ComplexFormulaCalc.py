import math

def main():
    print("Welcome to the Quadratic Equation Solver!")

    # Prompt the user to input the required values
    a = float(input("Enter the coefficient a: "))
    b = float(input("Enter the coefficient b: "))
    c = float(input("Enter the coefficient c: "))

    # Calculate the discriminant
    discriminant = b**2 - 4*a*c

    if discriminant >= 0:
        # Calculate the two solutions
        root1 = (-b + math.sqrt(discriminant)) / (2*a)
        root2 = (-b - math.sqrt(discriminant)) / (2*a)
        print(f"The roots of the equation are: {root1} and {root2}")
    else:
        print("The equation has no real roots.")

    # Display a goodbye message
    print("Thank you for using the Quadratic Equation Solver! Goodbye!")

if __name__ == "__main__":
    main()
