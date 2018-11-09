import random
answer = random.randint(0,10)

print("Guess Game!")
print()

playing = True
guesses_left = 5

while guesses_left > 0 and playing:
    name = input("guess a number 1-10:")
    if name == answer:
        print("You Win!!! YaY!!!!")
        playing = False
    else:
        guesses_left -= 1

