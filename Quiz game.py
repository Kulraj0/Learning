print("Welcome to my quiz game")

playing = input("do you want to play the game? ")

if playing.lower() != "yes":
    quit()

name = input("What's your name?")
print("Let's begin the game")

print("There will be 10 questions,first 5 questions will be for 1 point each and next 5 will be for 2 points each, to win you have to get 10 points. Goodluck!")

score = 0

answer = input("1. Which planet is known as the Red Planet?")
if answer.lower() == "mars":
    score += 1

answer = input("2. Who was the first woman to fly solo across the Atlantic Ocean?")
if answer.lower() == "amelia earhart":
    score += 1

answer = input("3. What is the largest mammal in the world??")
if answer.lower() == "blue whale":
    score += 1

answer = input("4. In which year did India gain independence from British rule?")
if answer.lower() == "1947":
    score += 1

answer = input("5. Who wrote the play Romeo and Juliet?")
if answer.lower() == "william shakespeare":
    score += 1

print ("2 marks questions begin,your current score is ",score)

answer = input("6. What is the chemical symbol for the element gold?")
if answer.lower() == "au":
    score += 2

answer = input("7. Which country is known as the Land of the Rising Sun?")
if answer.lower() == "japan":
    score += 2

answer = input("8. What is the capital city of Australia?")
if answer.lower() == "canberra":
    score += 2

answer = input("9. Who was the first person to reach the South Pole?")
if answer.lower() == "roald amundsen":
    score += 2

answer = input("10. What is the smallest country in the world by area?")
if answer.lower() == "vatican city":
    score += 2

print (" Your score is ",score)
if score > 10:
    print("You pass! congratulations")

else:
    print("You failed,try again")