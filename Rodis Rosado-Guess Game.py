import random
answer = random.randint(0,10)

print("Guess Game!")
print()

playing = True
guesses_left = 5

real_guess = int(input ("Your answer is higher then")
hidden_guess = real_guess 5
print (hidden_guess)

while guesses_left > 0 and playing:
    name = input("guess a number 1-10:")
    if name == answer:
        print("You Win!!! YaY!!!!")
        playing = True
    else:
        guesses_left -= 1

