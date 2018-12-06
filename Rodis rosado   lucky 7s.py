import random
money_left = 15
rounds_played = 0
while money_left > 0:



    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)
    add = dice1 + dice2
    rounds_played += 1
    money_left -= 1
    if add == 7:
        money_left +=3
        print(money_left)
        print("You have lost %s rounds "  %  rounds_played)

