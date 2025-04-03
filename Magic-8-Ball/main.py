#
# Robert Freitas
# 04/03/2025
# Magic 8 Ball Programming Project
# COSC 1010
#
# Use comments liberally throughout the program. 

# Import Random module.
import random

# Declare name variable
name = "Robert"

# Declare variable for a "Yes" or "No" question to ask the Magic 8 ball.
question = "Will I ever be rich?"

# Declare answer variable (holds answer for Magic 8 ball)
answer = ""

# Declare variable to store randomly generated value, then assign it randint function.
random_number = random.randint(1,12)

# Implement if statement so that if random number is equal to 1 the answer will be "Yes, of course!"
if random_number == 1:
    answer = "Yes, of course!"

# Use elif statement so that if the random number is equal to 2 the answer will be "Without a doubt, yes."
elif random_number == 2:
    answer = "Without a doubt, yes."

# Continue using elif statements to assign remaining answers to values 3 through 12.
elif random_number == 3:
    answer = "You can count on it."

elif random_number == 4:
    answer = "For sure!"

elif random_number == 5:
    answer = "Ask me later."

elif random_number == 6:
    answer = "I'm not sure."

elif random_number == 7:
    answer = "I can't tell you right now."

elif random_number == 8:
    answer = "I will tell you after my nap."

elif random_number == 9:
    answer = "No way!"  
   
elif random_number == 10:
    answer = "I don't think so."

elif random_number == 11:
    answer = "Without a doubt, no."

elif random_number == 12:
    answer = "The answer is clearly NO."  

# Use else statement to assign the answer to the the phrase "Error" if the number is accidentally outside of the range of answers.
else:
    answer = "Error"

# Use print statement to output users name and question.
print(name + " asks: " + question)

# Add another print statement to output Magic 8-Ball's answer.
print("Magic 8-Ball's answer: " + answer)
