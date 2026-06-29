# Quest 18: The Loop of Riddles
secret_number = 7
print("I'm thinking of a number between 1 and 10. Can you guess it?")
guess = None
while guess != secret_number:
    user_input = input("Enter your guess: ")
    guess = int(user_input)
    if guess == secret_number:
        print("Well done, adventurer! You guessed correctly!")
    else:
        print("Wrong! Try again...")
