import random
attempt=1
score=0
print("WELCOME TO ROCK🌑 ,Paper📄, Sizzor✂ Game")
print("Rules of ROCK🌑, Paper📄, Sizzor✂  Game is explained below \n",
"1. Rock🌑 beats Sizzor✂\n",
"2. Paper📄 beats Rock🌑\n","3. Sizzor✂ beats Paper📄\n")
while attempt<11:
    computer=random.choice(("Rock","Paper","Sizzor"))
    user=input("Enter your choice among [Rock🌑, Paper📄, Sizzor✂]: ")
    if user==computer:
        print("It's a tie match")
        print("Your score= ",score)
        attempt=attempt+1
    
    elif (user== "Sizzor" and computer== "Rock") or  (user== "Paper" and computer== "Sizzor") or  (user== "Rock" and computer== "Paper"):
        print("You lost this match")
        print("Your score= ",score-1)
        score=score-1
        attempt=attempt+1
        
    elif (user== "Rock" and computer== "Sizzor") or (user== "Sizzor" and computer== "Paper") or (user== "Paper" and computer== "Rock"):
        print("You won this match")
        print("Your score= ",score+1)
        score=score+1
        attempt=attempt+1
        
    else:
        print("----ENTER CORRECT VALUE----")
else:
    print(f"Total score you scored in this Game is= {score} ")