import math

side_a = input("Please enter the first side of a triangle.")    # Input three sides of a triangle 
side_b = input("Please enter the second side of a triangle.")   # Store three sides of a triangle in variables: side_a, side_b and side_c
side_c = input("Please enter the third side of a triangle.")

sideA = float(side_a)   # Convert side_a, side_b and side_c to float and Store them in variables sideA, sideB and sideC
sideB = float(side_b)   
sideC = float(side_c)

s = ((sideA+sideB+sideC)/2)     # Divide the sum of the sides by 2 and Store it in variable s

value = s*(s-sideA)*(s-sideB)*(s-sideC)   # Multiply s by the result of the subtraction of each side from s and Store it in variable value

area = math.sqrt(value)     # Calculate the square root of the value and Store it in variable area
print (area)        # Print area

