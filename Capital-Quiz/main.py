#
# Robert Freitas
# 04/24/25
# Capital Quiz Programming Project
# COSC 1010
#
# Use comments liberally throughout the program. 

import random
# Constant for the number of states to quiz the user on.
NUM_STATES = 5

def main ():
    # Initialize the state_caps dictionary.
    state_caps = state_cap_dictionary()
    
    # Initial variables to keep count of the number of correct and incorrect answers.
    correct = 0
    incorrect = 0

    # Quiz the user.
    for count in range (NUM_STATES):
        # Get a random entry from the dictionary.
        state, capital = random.choice(list(state_caps.items()))
        

        # Quiz the user.
        print('What is the capital ', state, '? ', end='')
        responses = input()

        # Is the user correct?
        if responses.lower() == capital.lower():
            correct += 1
            print ('Correct!')
        else:
            incorrect += 1
            print('Incorrect.')

    # Display the results.
    print('Correct responses:', correct)
    print ('Incorrect responses:', incorrect)

# The state_cap_dictionary function builds a dictionary containing the names of the U.S. states and their capitals.
# The function returns a reference to the dictionary.
def state_cap_dictionary():
    sc = {  'Alabama':'Montgomery', 'Alaska':'Juneau',
            'Arizona':'Phoenix', 'Arkansas':'Little Rock',
            'California':'Sacramento', 'Colorado':'Denver',
            'Connecticut':'Hartford', 'Delaware':'Dover',
            'Florida':'Tallahassee', 'Georgia':'Atlanta',
            'Hawaii':'Honolulu', 'Idaho':'Boise',
            'Illinois':'Springfield', 'Indiana':'Indianapolis',
            'Iowa':'Des Moines', 'Kansas':'Topeka',
            'Kentucky':'Frankfort', 'Louisiana':'Baton Rouge',
            'Maine':'Augusta', 'Maryland':'Annapolis',
            'Massachusetts':'Boston', 'Michigan':'Lansing',
            'Minnesota':'Saint Paul', 'Mississippi':'Jackson',
            'Missouri':'Jefferson City', 'Montana':'Helena',
            'Nebraska':'Lincoln', 'Nevada':'Carson City',
            'New Hampshire':'Concord', 'New Jersey':'Trenton',
            'New Mexico':'Santa Fe', 'New York':'Albany',
            'North Carolina':'Raleigh', 'North Dakota':'Bismarck',
            'Ohio':'Columbus', 'Oklahoma':'Oklahoma City',
            'Oregon':'Salem', 'Pennsylvania':'Harrisburg',
            'Rhode Island':'Providence', 'South Carolina':'Columbia',
            'South Dakota':'Pierre', 'Tennessee':'Nashville',
            'Texas':'Austin', 'Utah':'Salt Lake City',
            'Vermont':'Montpelier', 'Virginia':'Richmond',
            'Washington':'Olympia', 'West Virginia':'Charleston',
            'Wisconsin':'Madison', 'Wyoming':'Cheyenne'}
    return sc

# Call the main function
main()
