#
# Robert Freitas
# 02/27/2025
# Budget Analysis Programming Project
# COSC 1010
#
# Use comments liberally throughout the program.

# Variables to hold the budget total more expenses

more_expenses = 'y'
budget_total = 0.0

# Get the budget of the user
budget = float( input( "Please enter how much you've budgeted for the month: " ) )

# Process Expenses
while more_expenses == 'y':
    
    # Get Expenses
    userExpense = float( input( ' Enter an expense: ' ) )
    budget_total += userExpense
    # Get additional Expenses
    more_expenses = input( ' Does user have more expenses?: Enter y for yes, n for no: ' )

# Use print statement within if-elif-else statement to show if user is over, under or at exact budget.
if budget_total > budget:
    print( ' You were over your budget of','$' + format( budget, ',.2f' ),'by','$' + format( budget_total - budget, ',.2f'  ) )

elif budget > budget_total:
     print( ' You were under your budget of','$' + format( budget, ',.2f' ),'by','$' + format( budget - budget_total, ',.2f'  ) )

else:
    print( ' You used exactly your budget of','$' + format( budget , ',.2f'),'.')

