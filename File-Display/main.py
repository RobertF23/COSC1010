#
# Robert F
# 04/01/25
# File Display Programming Project
# COSC 1010
#
# Use comments liberally throughout the program. 

# Open the file.
myfile = open('numbers.txt', 'r')

# Read and display the file's contents.
for line in myfile:
    number = int(line)
    print(number)

# Close the file.
myfile.close

