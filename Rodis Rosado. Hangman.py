import random
import string
Word = ["Jaw", "hey", "zoo", "china", "california", "car", "red", "job", "jar", "sam"]
letter = list(string.ascii_letters)
secretWord = random.choice(Word)
print(len(Word))

guesses_left = 8

playing = True
while guesses_left > 0 and playing:

    while guesses_left > 0 and playing:
        letter = int(input("Type in a letter"))
        if letter > Word:
            print("TRY AGAIN")
            guesses_left -= 1
        elif guess < Word:
            print("guess higher")
            guesses_left -= 1
    else:
        print ("You win!!!!")
        playing = False



