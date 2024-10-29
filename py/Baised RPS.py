import random

Options = ["rock", "paper", "scissors"]

print("Game begins! \n To stop playing enter Q anytime you want \n ")

user_wins = 0
comp_wins = 0
i = 1
while True:
    user_guess = input(f"Round {i}. What do you choose \n")
    i += 1
    user_guess = user_guess.lower()

    if user_guess == "q":
        print(f"You won {user_wins} times and Computer won {comp_wins} times")
        quit()
    elif user_guess not in Options:
        print("Enter a valid input")
        continue
    elif user_guess == "rock":
        comp_guess = random.choices(Options, weights = [0.3,0.5,0.2], k=1)[0]
    elif user_guess == "paper":
        comp_guess = random.choices(Options, weights = [0.2,0.3,0.5], k=1)[0]
    elif user_guess == "scissors":
        comp_guess = random.choices(Options, weights = [0.5,0.2,0.3], k=1)[0]
    
    if user_guess == "rock" and comp_guess == "scissors" :
        print(f"Computer chose {comp_guess} \nYou win!")
        user_wins += 1

    elif user_guess == "paper" and comp_guess == "rock" :
        print(f"Computer chose {comp_guess} \nYou win!")
        user_wins += 1

    elif user_guess == "scissors" and comp_guess == "paper" :
        print(f"Computer chose {comp_guess} \nYou win!")
        user_wins += 1
    
    elif user_guess == comp_guess:
            print(f"computer chose {comp_guess}, Its a draw")

    else:
        print(f"Computer chose{comp_guess}\nYou lost!")
        comp_wins += 1

    
