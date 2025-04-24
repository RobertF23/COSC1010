#
# Robert Freitas
# 04/23/2025
# Pig Latin Programming Project
# COSC 1010
#
# Use comments liberally throughout the program. 

# Define Function
def pig_latin_word_converter(word):
    # Define vowels and implement for loop. 
    vowels = 'aeiou'
    if word[0] in vowels:
        return word + 'way'
    else:
        #return word[1:] + word[0] + 'ay'
     for index, letter in enumerate(word):
             if letter in vowels:
                 return word[index:] + word[:index] + 'ay'
    return word + 'ay'

# Define function that takes in sentence and splits it into a list of individual words
def pig_latin_sentence_converter(sentence):
    words = sentence.split()
    output = []
    for word in words:
        output.append(pig_latin_word_converter(word))
# Use join function to concatenate output into single string with a space between each word.
    return " ".join(output)

# Define main function and apply while loop for sentence translation. 
def main():
    while True:
        sentence = input("Enter a sentence to translate to pig latin: ")
        print(f'Pig Latin translation: {pig_latin_sentence_converter(sentence)}')

main()
