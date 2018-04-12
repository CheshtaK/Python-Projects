import random

guesses = []
cpu_num = random.randint(1, 100)
player_num = int(input("Enter a number between 1 and 100: "))
guesses.append(player_num)

while player_num != cpu_num:
    if player_num > cpu_num:
        print("Too high!")
    else:
        print("Too low!")
    player_num = int(input("Enter again: "))
    guesses.append(player_num)
else:
    print("Well done!!")
    print("It took you %i guesses: " % len(guesses))
    print("Here are your guesses: ")
    print(guesses)
