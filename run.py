import random
import time
from diagrams import attemps_diagrams, num_attemps


# List of words
colors = ["green", "orange", "pink", "brown", "black", "white", "purple", "blue",
          "yellow", "gray", "red", "beige", "violet"]
fruits = ["kiwi", "apple", "apricot", "banana", "blacberry", "blueberry", "cherry", 
          "coconut", "fig", "grape", "lychee", "mango", "orange", "papaya", "peach", 
          "pear", "plump", "pineaple", "strawberry", "watermelon"]
animals = ["dog", "lion", "pig", "rabbit", "duck", "fox", "horse", "cow", "deer",  
           "snake", "panda", "frog", "cat", "scorpion", "bee", "sheep", "otter", "bison",
           "owl", "ladybug", "bat", "hippo", "elephant", "tiger", "Kangaroo", "dolphin", 
           "beer", "wale", "eagle", "turtle", "monkey", "zebra", "gerraf"]

category = [colors, fruits, animals]


def welcome():
    """
    Show a welcome message and ask the user name
    """

    print("""

    █╗  ██╗ █████╗ ███╗   ██╗ ██████╗ ███╗   ███╗ █████╗ ███╗   ██╗
    ██║  ██║██╔══██╗████╗  ██║██╔════╝ ████╗ ████║██╔══██╗████╗  ██║
    ███████║███████║██╔██╗ ██║██║  ███╗██╔████╔██║███████║██╔██╗ ██║
    ██╔══██║██╔══██║██║╚██╗██║██║   ██║██║╚██╔╝██║██╔══██║██║╚██╗██║
    ██║  ██║██║  ██║██║ ╚████║╚██████╔╝██║ ╚═╝ ██║██║  ██║██║ ╚████║
    ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝ ╚═════╝ ╚═╝     ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝

    """)

    print("============================")
    print("Welcome to the hangman game!")
    print("============================")

    user_name = input("Please enter your name: \n")
    print(f"Welcome to the hangman game, {user_name}")
    pause()


def instructions():
    """
    Show a message askin if the user needs instructions
    """
    print("Do you know how to play or would you like a brief instruction on how to do it?")
    instruction_on = input("Press y if you would like to read the instructions, any other key to play game : \n")
    if instruction_on.lower() == "y":
        instructions_needed()
        print("Are you ready to play?")
        game_start = input("Press Any key to start the game\n")
    else:
        pass


def instructions_needed():
    """
    Display instructions
    """
    print("This is how you can play \n"
          "1. Choose a category\n"
          "2. You will see underscores '_' the number of underscores represent \n"
          "   the letters of the word.\n"
          "3. Start guessing letters\n"
          "4. If your guess correctly,the letter will be displayed\n"
          "   instead of the underscore'_'.\n"
          "5. If your guess is incorrect, part of hangman will be display\n"
          "6. If you guess all the letters, you win the game\n"
          "7. You have an attemps limit, if you reach this limit\n"
          "   and the hangman image is completed...the game is over!")


def select_category():
    """
    The user has to select a category in order to start the game
    """
    print("Please choose a category \n")
    print("1. Colors\n"
          "2. Fruits\n"
          "3. Animals\n"
          "4. Mixed\n")
    category_num = 0
    while not 1 <= category_num <= 4:
        try:
            category_num = int(input("Please enter 1, 2, 3 or 4\n"))
            if 1 <= category_num <= 4:
                return category_num
            else:
                pass
        except ValueError as e:
            print("Invalid number, please enter a valid number... 1, 2, 3 or 4 accepted")


def select_word():
    """
    A word will be selected from the list and will be displayed on the screen.
    Instead of letters, a underscore will appear
    """
    pause()
    category_chosen = select_category()
    num_category = category_chosen - 1
    print(f"You have selected {category_chosen} category")
    if category_chosen == 4:
        category_item = random.choice(category)
        word = random.choice(category_item)
        return (word)
    else:
        category_item = category[num_category]
        word = random.choice(category_item)
        return (word)


def hangman():
    """
    This function will ask for an input from the user, will check the answer and count the attempts.
    """
    incorrect = 0
    correct_attempt = set([])
    word = select_word()
    check_letter = word.replace(" ", "")
    answer = [i for i in check_letter]
    wrong_attempt = []
    while incorrect < num_attemps:
        attempt_message()
        for i in word:
            if i == " ":
                print(i, end="  ")
            elif i in correct_attempt:
                print(i.upper(), end=" ")
            else:
                print("_ ", end=" ")
        print('\n')
        guessed = input("Enter a letter \n").lower()
        if guessed in answer:
            if guessed in correct_attempt:
                display_already_used()
                pause()
            else:
                print(f"{guessed.upper()} is correct")
                correct_attempt.add(guessed)
                word_letters = word.replace(" ", "")
                if correct_attempt == set(word_letters):
                    print(word.upper())
                    print(f"Exelent! you guessed the word! {word.upper()}")
                    break
                pause()
        else:
            if len(guessed) > 1:
                print("Please input one letter at a time ")
            else:
                print(f"the word does not contains letter '{guessed.upper()}'")

            incorrect += 1
            print("\n".join(attemps_diagrams[:incorrect]))
            print("\n")
            wrong_attempt.append(guessed.upper())
            print(f"Your incorrect guesses: {wrong_attempt} ")
            pause()
    if incorrect == num_attemps:
        print(f"Answer is {word.upper()}")
        game_over()

    pause()
    replay()


def attempt_message():
    print("\n")
    print("Can you guess the word?")
    print("Enter one letter to see if you are right!")


def display_already_used():
    print("you used this before")


def game_over():
    """
    GAME OVER ascii art
    """
    print(""" 
    ██████╗  █████╗ ███╗   ███╗███████╗     ██████╗ ██╗   ██╗███████╗██████╗ 
    ██╔════╝ ██╔══██╗████╗ ████║██╔════╝    ██╔═══██╗██║   ██║██╔════╝██╔══██╗
    ██║  ███╗███████║██╔████╔██║█████╗      ██║   ██║██║   ██║█████╗  ██████╔╝
    ██║   ██║██╔══██║██║╚██╔╝██║██╔══╝      ██║   ██║╚██╗ ██╔╝██╔══╝  ██╔══██╗
    ╚██████╔╝██║  ██║██║ ╚═╝ ██║███████╗    ╚██████╔╝ ╚████╔╝ ███████╗██║  ██║
    ╚═════╝ ╚═╝  ╚═╝╚═╝     ╚═╝╚══════╝     ╚═════╝   ╚═══╝  ╚══════╝╚═╝  ╚═╝
    """)


def replay():
    print("Would you like to play again?")
    print("Enter y or press RUN PROGRAM button above to play again."
          "or press any other key to exit the game.")
    play_again = input(
        "Please press y to play, any other key to exit the game \n")
    if play_again.lower() == "y":
        hangman()
    else:
        print("Thank you for playing the game")


def pause():
    time.sleep(0.2)


def main():
    welcome()  # greeting function
    instructions()  # display instruction if user chooses
    hangman()


main()