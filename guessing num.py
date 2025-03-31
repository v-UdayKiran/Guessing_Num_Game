import random

def number_guessing_game():
    print("May I ask you for your name?")
    player_name = input().strip()
    print(f"{player_name}, we are going to play a game. I am thinking of a number between 1 and 200")
    print("Go ahead. Guess!")
    
    lower_bound = 1
    upper_bound = 200
    secret_number = random.randint(lower_bound, upper_bound)
    attempts = 0
    
    while True:
        try:
            guess = int(input("Guess: "))
            attempts += 1
            
            if guess < lower_bound or guess > upper_bound:
                print("Silly Goose! That number isn't in the range!")
                print(f"Please enter a number between {lower_bound} and {upper_bound}")
            elif guess < secret_number:
                print("The guess of the number that you have entered is too low")
                print("Try Again!")
            elif guess > secret_number:
                print("The guess of the number that you have entered is too high")
                print("Try Again!")
            else:
                print(f"Nope. The number I was thinking of was {secret_number}")
                break
        except ValueError:
            print("Invalid input! Please enter a valid integer.")
    
    play_again = input("Do you want to play again? (yes/no): ").strip().lower()
    if play_again == "yes":
        number_guessing_game()

if __name__ == "__main__":
    number_guessing_game()
