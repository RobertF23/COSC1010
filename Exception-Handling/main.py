#
# Robert Freitas
# Dat04/02/25
# Exception Handling Programming Project
# COSC 1010
 

# Calculate the average of a list of numbers 
def main():

# Implement Try statement to run block of code below.
    try:
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
# Implement Exception for IOError. If error occurs print statement below will execute.
    except IOError as error:
        print( "An IOError occured:", error )
# Implement Exception for ValueError. If error occurs print statement below will execute.
    except ValueError as error:
        print( "A ValueError occured:", error)
# Apply else statement to print the average if above exceptions do not occur.
    else:
        print( "The average is", average )
# Final print statement to end program.
    finally:
        print( "End of program" )

# Call main function.
main() 