def call():
    pass
    import random 

    attempts = 0

    number = random.randrange(1,100)
    guess = int(input("Guess a number between 1 and 100: "))
    while guess != number:
        if guess < 0 or guess > 100:
            print("invalid input. Try again")
            attempts = attempts +1
            guess = int(input("\nGuess a number between 1 and 100: "))
        if guess < number :
            print("Your guess is too low. ")
            attempts = attempts +1
            guess = int(input("\nGuess a number between 1 and 100: "))
        else:
            print("Your guess is too high. ")
            attempts = attempts +1
            guess = int(input("\nGuess a number between 1 and 100: "))
    print("You guessed correctly!")
    print("You guessed the answer in", attempts, "attempts.")
    guess = int(input("\nGuess a number between 1 and 100: "))

    return call()   
print(call())
print(call())   
print(call())
print(call())

