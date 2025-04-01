#
# Robert Freitas
# 04/01/25
# Average of Numbers Programming Project
# COSC 1010
#
# Use comments liberally throughout the program.

# Calculate the average of a list of numbers
def main():
    numbersFile = open( "numbers.txt", "r" )

# Declare Variables 
    total = 0
    numberOfLines = 0
    line = numbersFile.readline()

# Implement while loop to move between lines in file.
    while line != "":
        numberOfLines += 1
        total += int( line )
        line = numbersFile.readline()
# Calculate the average.
    average = total / numberOfLines

# Use print function to show average.
    print( "The average is", average )

# Call main function.
main()   
