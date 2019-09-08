import random

def guessingGame():
    MIN = 0
    MAX = 20
    number = random.randint(MIN, MAX)
    #print(number)
    guesses = 0
    
    while (guesses < 5):
        print("Guess a number between 0 - 20")
        try:
            guess = int(input())
            if guess < MIN:
                continue
            elif guess > MAX:
                continue
            # our way
            else:
                if(guess == number):
                    print("Correct. You are a champion!")
                    return
                else:
                    print("Wrong. Try again.")
                guesses += 1
        except:
            print("Use numbers dummy!")
    # Losers end point
    print("Game Over!")

guessingGame()





