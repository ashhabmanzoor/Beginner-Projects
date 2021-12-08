import random
print("Welcome to GUESS THE NUMBER!\n")

number = random.randint(0, 10)
state = True
guesses = 3


def choice():
    global state, guesses
    if guesses > 0:
        user_choice = input("Guess the number: ")
        if user_choice.isdigit():
            user_choice = int(user_choice)

            if user_choice == number:
                print("Correct!")
                state = False

            elif user_choice > number:
                print("The number is lower!\n")
                guesses -= 1

            elif user_choice < number:
                print("The number is higher!\n")
                guesses -= 1
        else:
            print("Please enter number only!")

    elif guesses == 0:
        print("Sorry, No guesses left!")
        print(f"The number was {number}")
        print("Game Over!!!!")
        state = False


while state == True:
    choice()
