import random
attempt=1
secret=random.randint(1,100)
print("WELCOME TO NUMBER GUESSING NUMBER GAME!...")
while attempt<4:
    user=int(input("Enter your guessed number from(1 to 100) ---- "))
    if user<secret:
        print("Your guessed number is TOO LOW compared to computer's secret number")
        print(f"You have another {3-attempt} chance to guess number! Try again ----")
        attempt=attempt+1
    elif user>secret:
        print("Your guessed number is TOO HIGH compared to computer's secret number")
        print(f" You have another {3-attempt} chance to guess number! Try again ----")
        attempt=attempt+1
    else:
        print("CONGRATS! You guessed correct number")
        break
else:
    print("You are out of Chance! Better luck next time")
        

