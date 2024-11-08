# Julian Huerta
# UWYO COSC 1010
# Submission Date 11/7/24
# Lab 08
# Lab Section: 14
# Sources, people worked with, help given to:


# Write a function that will properly check strings to see if they are an int or float, and convert them if so
# If they can't be converted return false
# Other wise return the converted int or float 
# Floats should only have one decimal point in them 

def convert_to_number(s):
    if s.isdigit() or (s[0] == '-' and s[1:].isdigit()):
        return int(s)
    if s.count('.') == 1:
        try:
            float_value = float(s)
            return float_value
        except ValueError:
            return False
    return False

print("*" * 75)


# Point-slope y = mx + b
# This is used in mathematics to determine what the value y would be for any given x
# Where b is the y-intercept, where the line crosses the y-axis (x = 0)
# m is the slope of the line, the rate of change, how steep the line is
# x is the variable, and is determined by which point on the graph you wish to evaluate
# Create a function slope_intercept that takes in four parameters
    # m, the slope
    # b, the intercept
    # a lower x bound
    # an upper x bound
# Return a list for all values of y for the given x range, inclusive (whole number X's only)
# Check to make sure that the lower bound is less than or equal to the upper bound
# m, b can be floats or integers
# the bounds must be integers, if not return false

# Create a while loop to prompt users for their input for the four variables
# Exit on the word exit
# Remember all inputs are strings, but the function needs ints or floats
# Call your function and print the resulting list

def slope_intercept (m, b, lower_x, upper_x):
    if not isinstance(lower_x, int) or not isinstance(upper_x, int):
        return False
    
    y_values = []
    x = lower_x
    while x <= upper_x:
        y = m * x + b
        y_values.append(y)
        x += 1
    return y_values
def get_input():
    while True:
        m_input = input("Enter the slope (m) as a number (float or int), or 'exit' to quit: ")
        if m_input.lower() == 'exit':
            break
        b_input = input("Enter the Y-intercept (b) as a number (float or int), or 'exit' to quit: ")
        if b_input.lower() == 'exit':
            break
        lower_x_input = input("Enter the lower x bound as an integer, or 'exit' to quit: ")
        if lower_x_input.lower() == 'exit':
            break
        upper_x_input = input("Enter the upper x bound as an integer, or 'exit' to quit: ")
        if upper_x_input.lower() == 'exit':
            break
        try:
            m = float(m_input)
            b = float(b_input)
            lower_x = int(lower_x_input)
            upper_x = int(upper_x_input)
        except ValueError:
            print("Invalid input. Please make sure the values are numbers.")
            continue
        result = slope_intercept(m, b, lower_x, upper_x)
        if result is False:
            print("Invalid bounds or input types. Please try again.")
        else:
            print("The y values for the given x range are:", result)
            break
get_input()

print("*" * 75)


# Write a function to solve the quadratic formula
# https://en.wikipedia.org/wiki/Quadratic_formula
# Accept inputs for a, b, c
# Remember that this returns two values
# Create a loop like above to prompt the user for input for the three values
# Create a second function that just does the square root operation 
    # If the number you are trying to take the square root of is negative, return null

import math
def sqrt_operation(value):
    if value < 0:
        return None
    return math.sqrt(value)
def solve_quadratic(a, b, c):
    discriminant = b**2 - 4*a*c
    sqrt_discriminant = sqrt_operation(discriminant)
    if sqrt_discriminant is None:
        return None
    root1 = (-b + sqrt_discriminant) / (2 * a)
    root2 = (-b + sqrt_discriminant) / (2 * a)
    return root1, root2
def get_input():
    print("Starting the input loop...")
    while True:
        a_input = input("Enter the value for a (or 'exit' to quit): ")
        if a_input.lower() == 'exit':
            break
        b_input = input("Enter the value for b (or 'exit' to quit): ")
        if b_input.lower() == 'exit':
            break
        c_input = input("Enter the value for c (or 'exit' to quit): ")
        if c_input.lower() == 'exit':
            break
        try:
            a = float(a_input)
            b = float(b_input)
            c = float(c_input)
        except ValueError:
            print("Invalid input. Please make sure the values are numbers.")
            continue
        result = solve_quadratic(a, b, c)
        if result is None:
            print("The euqation has no real solution.")
        else:
            root1, root2 = result
            print(f"The solutions are: {root1} and {root2}")
get_input()
