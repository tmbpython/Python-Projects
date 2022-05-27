
import random

upper_range = input("Input a number: ")

if upper_range.isdigit():
    upper_range = int(upper_range)

    if upper_range <= 0:
        print("Please input a value greater than 0 next time. ")
        quit()
else:
    print("Please input a number next time! ")
    quit()

random_number = random.randint(0, upper_range)
guesses = 0

while True:
    guesses += 1
    player_guess = input("Make a guess: ")
    if player_guess.isdigit():
        player_guess = int(player_guess)
    else:
        print("Please input a number next time! ")
        continue
    
    if player_guess == random_number:
        print("You guessed correct!")
        break
    else:
        if player_guess > random_number:
            print("You guess was above the number!")
        else:
            print("You were below the number!")

print("You got it in", guesses, "guesses")



