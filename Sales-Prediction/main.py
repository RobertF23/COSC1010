#
# Robert Freitas
# 02/15/2025
# Sales Prediction Programming Project
# COSC 1010
#

# Variables to hold the sales total and the profit
total_sales = 0.0
PROFIT = 0.23

# Get the amount of projected sales.
total_sales = float(input('Enter the projected sales:'))

# Calculate the projected profit.
profit = total_sales * 0.23

# Print the projected profit.
print('The profit is $', format(profit, ',.2f'))
