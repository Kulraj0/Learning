import random

range = input("Input a number for the range in which you want to play \n")

if range.isdigit():
    range = int(range)
    if range<0:
        print("Number should be greater than 0")
        quit()
else:
    print("Enter a valid number")
    quit()

number = random.randint(1, range + 1)

tries = 0

while True:
    guess = input(f"Guess the number between 1 and {range} \n")
    if guess.isdigit():
        guess = int(guess)
        tries += 1
        if guess == number:
            print("You got it! in ", tries, "tries")
            break
        else:
            print("you got it incorrect,try again")
            if guess>number:
                if guess>number/2:
                    print("Your guess is too great than number \n")
                else:
                    print("your guess is greater than number \n")
            else:
                if guess<number*2:
                    print("Your guess is too lower than number \n")
                else:
                    print("your guess is lower than number \n")
            continue
            
    else:
        print("Enter a valid number.")
