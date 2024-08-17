#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp


# Opens the names file and creates a list of names with list comprehension.
with open("Input/Names/invited_names.txt", mode="r") as names_file:
    names = [line.rstrip('\n') for line in names_file]

# Opens the starting letter, and puts it into a variable for use.
with open("Input/Letters/starting_letter.txt", "r") as starting_letter_file:
    letter = starting_letter_file.read()


# Iterates through the list of names, and creates a new file for each and REPLACES the [name] with the name from the list.
for name in names:
    with open(f"Output/ReadyToSend/letter_for_{name}", mode="w") as sending_letter_file:
        new_letter = letter.replace("[name]", f"{name}")
        sending_letter_file.write(new_letter)

