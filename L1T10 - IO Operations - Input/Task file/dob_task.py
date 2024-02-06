# Read the file 'DOB.txt' 
file = open('DOB.txt', 'r').read()

# Split the file contents into sentences based on newline characters '\n'
sentences = file.split('\n')
sentences_count = len(sentences)

# Print Name as a title
print("Name:") 

#Iterate through each sentence
for i in range(sentences_count):
    # Extract each sentence
    sentence = sentences[i]
     # Split each sentence into words
    words = sentence.split()
     # Extract and join the first two words as name
    name = ' '.join(words[0:2])
    print(name)

print('\n')
# Print Birthday as a title
print("Birthday:")

#Iterate through each sentence
for i in range(sentences_count):
    # Extract each sentence
    sentence = sentences[i]
    # Split each sentence into words
    words = sentence.split()
    # Extract and join the second three words as dob
    dob = ' '.join(words[2:5]) 
    print(dob)


    


