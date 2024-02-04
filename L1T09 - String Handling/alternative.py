sentence = "I enjoy coding and working with computer."
final_sentence = ""

for i in range(len(sentence)):                        # Loop through each character in the sentence
    if i % 2 == 1:                                    # Check if the index is odd
        final_sentence += sentence[i].lower()         # If it's odd, make the character lowercase and add it to the final sentence
    else:
        final_sentence += sentence[i].upper()         # If it's even, make the character uppercase and add it to the final sentence
print(final_sentence)

words = sentence.split()        # Split the sentence into words
words_count = len(words)

for i in range(words_count):                # Loop through each word in the sentence
    if i % 2 == 1:                          # Check if the index is odd
        words[i] = words[i].lower()         # If it's odd, make the word lowercase
    else:
        words[i]= words[i].upper()          # If it's even, make the word uppercase
print(' '.join(words))          # Rejoin and Print the modified words as a sentence
    


