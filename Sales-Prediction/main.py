#
# Robert Freitas
# 02/12/2025
# Sales Prediction Programming Project
# COSC 1010
#

# Variables to hold the sales total and the profit
sales_total = 533.00
profit = 0.00

# Get the amount of projected sales.
sale_total = float(input('Enter the projected sales:'))

# Calculate the projected profit.
profit = sales_total * 0.23

# Print the projected profit.
print('The profit is $', format(profit, ',.2f'))
