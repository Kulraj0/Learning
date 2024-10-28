import random

Options = ["rock", "paper", "scissors"]

print("Game begins! \n To stop playing enter Q anytime you want \n What do you choose")

while True:
    user_guess = input("What do you choose")
    user_guess = user_guess.lower()
    if user_guess not in Options:
        print("Enter a valid input")

    comp_guess = Options[random.randint(0,2)]

    user_wins = 0
    comp_wins = 0

    if user_guess == "q":
        print(f"You won {user_wins} times and Computer won {comp_wins} times")
        quit()
    elif user_guess == "rock" and comp_guess == "scissors" :
        print(f"Computer chose {comp_guess} \n You win!")
        user_wins += 1
    elif user_guess == "paper" and comp_guess == "rock" :
        print(f"Computer chose {comp_guess} \n You win!")
        user_wins += 1
    elif user_guess == "scissors" and comp_guess == "paper" :
        print(f"Computer chose {comp_guess} \n You win!")
        user_wins += 1
    elif user_guess == comp_guess:
        print("Its a draw")
    else:
        print(f"Computer chose{comp_guess} \n You lost!")
        comp_wins += 1

    
