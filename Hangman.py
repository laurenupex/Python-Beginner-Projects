# word variable = word to guess, player input
# representation of word variable in dashes
# guess variable
# show correct letters + list of incorrectly guessed letters
# keep looping until correct guess or certain number of incorrect guesses

dash = []
guess = ""
incorrect = []
correct = 0

word = input("Player1, please enter word to guess: ")  # takes player input as word to guess
for i in range(len(word)):  # converts word to dashes for guess
    dash.append("_")

while correct < len(word):
    print(dash)

    guess = input("Player2, please guess a letter: ")  # takes player input as guess
    for i in range(len(dash)):  # checks each letter
        if word[i] == guess:
            dash[i] = word[i]  # if correct, adds letter to dash display
            correct = correct + 1  # measures if all letters are correct
    if guess not in word:
        incorrect.append(guess)  # creates list of incorrectly guessed letters
    if len(incorrect) > 9:  # stops after 10 incorrect guesses
        correct = len(word)
    print("The correct letters are:", dash)
    print("The incorrectly guessed letters are:", incorrect)

print("The correct word was", word)
