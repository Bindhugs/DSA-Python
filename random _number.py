import random

# Number Guessing Game (1–50)
# The program generates a random number and asks the user to guess it.

while True:
    target = random.randint(1, 50)
    while True:
            user_choice = int(input("Guess the target (1-50): "))

            if user_choice == target:
                print("Success: Correct Answer")
                break
            elif user_choice < target:
                print("Take a bigger guess")
            else:
                print("Take a smaller guess")
    # Replay option
    play_again = input("\nPlay again? (y/n): ").lower()
    if play_again != "y":
        print("Thanks for playing!")
        break
