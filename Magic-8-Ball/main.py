#
# Robert Freitas
# 04/03/2025
# Magic 8 Ball Programming Project
# COSC 1010
#
# Use comments liberally throughout the program. 

# Import Random module.
import random

# Variable
repeat = 'y'

# Open a file
infile = open('8_ball_responses.txt', 'r')

# Read the file's contents.
ball_responses = infile.readlines()

# Close the file.
infile.close()

while repeat == 'y':
    question = input('what is your question: ')
    # Print the random response.
    response = random.choice(ball_responses)
    print(response)    

    # Want to do this again?
    print('Do you want to ask another question?')
    repeat = input('y = yes, anything else = no: ')
