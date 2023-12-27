# create variable of a string and for the alternative character string
sentence = input("Write a sentence please : ")
character = []

# create for loop with nested if function to choose .upper or .lower if the index is divisible by 2
for index in range(len(sentence)):
    if index % 2 == 0:
        character.append((sentence[index]).upper())
    else:
        character.append((sentence[index]).lower())
        
print("".join(character))



# create variable for the alternative word string
word = []

# split string every time a space occurs, i.e, a new word
split_sentence = sentence.split(" ")

# create for loop with nested if function to choose 
# .upper or .lower if the index is divisible by 2 
# (this time index goes word by word not character by character)
for index in range(len(split_sentence)):
    if index % 2 == 0:
        word.append((split_sentence[index]).upper())
    else:
        word.append((split_sentence[index]).lower())
        
print(" ".join(word))
