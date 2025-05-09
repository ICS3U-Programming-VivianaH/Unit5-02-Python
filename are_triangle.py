#!/usr/bin/env python3
# Created by: Viviana Hurtado
# Date: april, 2025
# The program
# Function to calculate and print the area of a triangle
def cal_area(height, base):
    # Calculate area using the triangle formula: (base × height) / 2
    area = (base * height) / 2
    # Print the result with 2 decimal places
    print("The area of the triangle is {:.2f} cm².".format(area))


# Main function where the program starts
def main():
    # Ask the user to input the base of the triangle
    base_str = input("Enter the base of the triangle in centimeters: ")
    # Ask the user to input the height of the triangle
    height_str = input("Enter the height of the triangle in centimeters: ")

    try:
        # Convert the input strings to float values
        base = float(base_str)
        height = float(height_str)

        # Check if both inputs are positive numbers
        if base > 0 and height > 0:
            # Call the function to calculate and display the area
            cal_area(base, height)
        else:
            # Display error message if numbers are zero or negative
            print("Error: Both the base and height must be positive numbers.")
    except Exception:
        # Handle invalid input (e.g., letters, symbols)
        print("Error: You must enter valid numeric values.")


# Run the main function when the script is executed
if __name__ == "__main__":
    main()
