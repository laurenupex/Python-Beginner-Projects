# create acronym of first letters of any phrase given by user

phrase = input("Enter the phrase to create an acronym: ")  # takes user input of phrase
remove = ["and ", "the ", "of ", "a ", "I ", "i ", "in ", "of ", "if ", "on "]  # filler words that won't be included
phrase2 = phrase  # creates unmodified copy of phrase to repeat at end statement

for word in remove:  # removes filler words from phrase
    phrase = phrase.replace(word, "")

acronym = phrase[0].upper()  # adds first letter of first word to acronym

for i in range(len(phrase)):  # adds avery letter after a space to acronym, as an uppercase character
    if phrase[i] == " ":
        acronym = acronym + phrase[i+1].upper()

print("The acronym of", phrase2, "is", acronym)  # repeats phrase and gives acronym to user
