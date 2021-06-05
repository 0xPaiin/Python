print("Welcome! Guess The Number Between 10 To 30. There is only 8 attempts.")
xs = 15
n = 0
guess_it = n + 1
while(guess_it <= 8 ):
    input1 = int(input())
    if input1 < xs:
        print("You have entered lesser Number.", "\nNumber of Attempts",guess_it , "Enter The Correct Number:")
    elif input1 > xs:
        print("You have entered greater Number.", "\nNumber of Attempts",guess_it , "Enter The Correct Number:")
    else:
        print("You won the game. Number of Guesses = ", guess_it)
        break
    guess_it = guess_it + 1
if guess_it > 8:
    print("Game Over")
