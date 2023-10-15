import random
import art
list = list(range(1,101))

def easy():
    numberOfAttempts = 10
    print("You have 10 attempts remaining to guess the number")
    number = int(random.choice(list))
    guessed_number = int(input("Make a guess: "))
    while numberOfAttempts > 0:
        if(guessed_number != number):
            if(guessed_number < number):
                print("Too low")
                print("Guess Again")
                numberOfAttempts -= 1
                print(f"You have {numberOfAttempts} remaining to guess the number")
                if(numberOfAttempts > 0):                  
                    guessed_number = int(input("Make a guess: "))
            elif(guessed_number > number):
                print("Too high")
                print("Guess Again")
                numberOfAttempts -= 1
                print(f"You have {numberOfAttempts} remaining to guess the number")
                if(numberOfAttempts > 0):                  
                    guessed_number = int(input("Make a guess: "))
        else:
            print(f"You got it, the guess was {guessed_number}!")
            return
    print("You lost all your attempts!")
    return
    


def difficult():
    numberOfAttempts = 5
    print("You have 5 attempts remaining to guess the number")
    number = int(random.choice(list))
    guessed_number = int(input("Make a guess: "))
    while numberOfAttempts > 0:
        if(guessed_number != number):
            if(guessed_number < number):
                print("Too low")
                print("Guess Again")
                numberOfAttempts -= 1
                print(f"You have {numberOfAttempts} remaining to guess the number")
                if(numberOfAttempts > 0):                  
                    guessed_number = int(input("Make a guess: "))
            elif(guessed_number > number):
                print("Too high")
                print("Guess Again")
                numberOfAttempts -= 1
                print(f"You have {numberOfAttempts} remaining to guess the number")
                if(numberOfAttempts > 0):                  
                    guessed_number = int(input("Make a guess: "))
        else:
            print(f"You got it, the guess was {guessed_number}!")
            return      
    print("You lost all your attempts!")
    return
    

def main():
    print(art.logo)
    print("Welcome to the number Guessing game")
    print("I'm thinking of a number between 1 and 100")
    level = input("Choose a difficulty level. Type 'easy' or 'hard': ")
    if(level.lower()) == 'easy':
        easy()
    elif(level.lower() == 'hard'):
        difficult()
    else:
        print("Invalid Input")


main()

# def easy():
#     print("H")



#     print("Welcome to the Number Guessing Game!")
#     print("I'm thinking of a number between 1 and 100")
#     string = input("Choose a difficulty. Type 'easy' or 'hard': ")
#     if(string == 'easy'):
#         difficulty()
#     else:
#         easy()

# main()
