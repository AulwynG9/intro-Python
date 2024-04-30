# Quiz rules:

# This quiz is open book/ open note: you may use class notes, notes from the instructor github, w3schools.com as well as google to search for relevant articles
# You MAY NOT use chatgpt or any AI software for this quiz. Any usage of AI tools will result in an automatic failure.

# No phones are allowed during the quiz. Failure to put your phone away will result in an automatic failure.

# There is no talking during the quiz. 

# You will have the entire class period to complete the quiz. 

# To recieve full credit please show your work by providng clues, keywords, and notes you wrote down to solve
# the problem.  

# 1. What is a while loop, what is a for loop, and what is the difference between the two.
# Please write your response using complete sentences. 
# A while loop is used to repeat a section of code an unknown number of times until a specific condition is met.
# 2. Name and describe three python operator families. Plese write your response using complete
# sentences.
#Arithmatic operater -The arithmetic operators are addition (+), subtraction (-), multiplication (*), division (/), exponent (**), floor division (//) and modulus (%). 
#Assignment Operator - They assign a certain value to a variable.
#Comparison Operators - You can use comparison operators to compare the values of variables.
# 3. Create a function that will accept 3 arguements. 
# This function should multiply the first 2 arguments and then
# subtract the last argument from the sum of the first 2. 

# 4. Research the range() function. Then create a function that takes 2 arguements. 
# Your function should take the range of the first argument and multiply those numbers by the second 
# argument. 
type(range(100))
range
range(10)
range(0, 10)
for seq in range(10):
    print(seq)
0
1
2
3
4
5
6
7
8
9
len(list(range(10)))
10
range(5,10)
for seq in range(5,10):
    print(seq)
5
6
7
8
9
for seq in range(-5,0):
    print(seq)
-5
-4
-3
-2
-1
[10, 11, 12, 13, 14, 15, 16, 17, 18, 19]


# 5. Create a function that will ask the user guess the correct number.
# Your function should take a user input which will be their guess. Your function should 
# generate a random number between 1 and 5. If the user guesses the number correctly, the program
# will inform the user they guessed correctly and end the game. If the user guesses incorrectly, they
# will be informed their guess is incorrect and to guess again. The user should only be able to guess
# incorrectly 3 times. If they get the 3rd attempt wrong, the program should inform they user they have lost
# the game.
import random

options = ("1", "2", "3")
running = True

while running:

    player = random.choice(options)
    computer = random.choice(options)


    while player not in options:
        player = input("Enter a choice (1, 2, 3): ")

    print(f"Player: {player}")
    print(f"Computer: {computer}")

    if player == computer:
        print("You Win!!")
    elif player == "1" and computer == "1":
        print("You win!")
    elif player == "2" and computer == "2":
        print("You win!")
    elif player == "3" and computer == "3":
        print("You win!")
    else:
        print("You lose!")

    if not input("Play again? (y/n): ").lower() == "y":
        running = False
print("Thanks for playing!")
#First step is importing the word random 
#Second step would be to randomize the players choices as well as the computers without doing that you won't be able to do anything with the problem
#Third step would be to add your choices of numbers you need these choices to be able to randomize between you and the computer.
#Forth step would be to add how you would win you can't win if the numbers do not add up also print messages like you would if you were playing a game
#Last step would be to add the option to play again because who would only want to play a game and lose and then not continue until you wanna win
# 6. Create a function that will act as a saving calculator. Your function should take several inputs from
# the user. Your program should ask the user what they are saving up for, how much does it cost, and how much 
# they want to deposit this week. Your program should repeat asking the user how much would they like to
# save this week, until the goal amount has been satisfied. Each time the user makes a deposit, your
# program should inform them how many weeks they have left, how much money they have deposited, and how
# much money their is remaining to reach their goal. 

# Ex. if my goal is to save $500, and deposit $20 dollars for that week, it should tell me that 
# It will take me 25 weeks to reach my goal based on the 20 dollar deposit, I have $20 saved,
# and that I need $480 more dollars.

# If I deposit $40 dollars the next week it should tell me
# it will take 10 weeks to reach my goal based on the $40 dollar deposit, I have $60 saved, and that I need 
# $440 more dollars to reach my goal.
# You would first start by making a calculator and add however much you wanna put money into then print a message saying you need this much left
#Like if you need 1000 dollars and you put 20 in every week then you should print it to say you need 980 left to go and how long it would take to make that amount