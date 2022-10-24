import random
import time

#List of words

colors = ["green", "orange", "pink","brown","black","white","purple","blue",
          "yellow", "gray", "red", "beige", "violet", ]
fruits = ["kiwi", "apple", "apricot", "banana", "blacberry", "blueberry", "cherry",
          "coconut", "fig", "grape", "lychee", "mango", "orange", "papaya", "peach",
          "pear", "plump", "pineaple", "strawberry", "watermelon"]
animals = ["dog", "lion", "pig", "rabbit", "duck", "fox", "horse", "cow", "deer", 
           "snake", "panda", "frog", "cat", "scorpion", "bee", "sheep", "otter", "bison",
           "owl", "ladybug", "bat", "hippo", "elephant", "tiger", "Kangaroo", "dolphin", 
           "beer", "wale", "eagle", "turtle", "monkey", "zebra", "gerraf"]


#Title


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
    print(f"~~~~~~  Welcome to hangman game, {user_name} ~~~~~~")
    pause()


def instructions():
    """
    Show a message askin if the user needs instructions
    """
    print("Do you know how to play or would you like a brief instruction on how to do it?")
    instruction_on = input("Press y if yes, any other key to play game : \n")
    if instruction_on.lower() == "y":
        instructions_text()
        print("Are you ready to play?")
        game_start = input("Press Any key to start a game >> \n")
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
          "7. If you guess all the letters, you win the game\n"
          "8. You have an attemps limit, if you reach this limit\n"
          "   and the hangman image is completed...the game is over!")



def main():
    welcome()  # greeting function
    instructions()  # display instruction if user chooses


main()