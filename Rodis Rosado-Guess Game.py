import random
r = random.randint(1,10)
guesses_left = 5
playing = True
while guesses_left > 0 and playing:

    print("Type in a number 1-10")

    while guesses_left > 0 and playing:
        guess = int(input("Guess="))
        if guess > r:
            print("Lower")
            guesses_left -= 1
        elif guess < r:
            print ("guess higher")
            guesses_left -= 1
    else:
        print ("You win!!!!")
        playing = False
    