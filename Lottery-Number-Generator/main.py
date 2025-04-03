#
# Robert Freitas
# 04/03/2025
# Lottery Number Generator Programming Project
# COSC 1010
#
# Use comments liberally throughout the program. 

# Import Random module.
import random

# Create set of global constants
MAX_DIGITS = 7    
START = 0
END = 9

# Main function
def main ():
    # Create a list.
    numbers = [0] * 7

    # Populate the list with random numbers.
    for index in range (MAX_DIGITS):
        numbers[index] = random.randint(START, END)

    # Display the random numbers.
    print ('Here are your local lottery numbers:')
    for index in range (MAX_DIGITS):
        print (numbers[index], end='')
    print()

# Call the main function.
main()

