str_manip = input("Please enter a sentence.")

print(len(str_manip))   # The length of the sentence

last_letter = str_manip[-1:]    # Find the last letter 

replaced_letter = str_manip.replace(last_letter, "@")    # Replace the last_letter with @
print(replaced_letter)

print(str_manip[-1:-4:-1])      # Print the last 3 characters backwards

first_three_characters = str_manip[0:3]   # Store the first three characters
last_two_characters = str_manip[-2:]   # Store the last two characters
five_letter_word = first_three_characters+last_two_characters      # Add the first three characters to the last two characters
print(five_letter_word)    # Print the final five-letter word