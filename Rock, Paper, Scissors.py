'''
Author: Caleb Goldman
Date: 11/30/2023
Description: Play a game of rock, paper, scissors
Challenges: I did none
Sources: Ms. Marciano
'''
import random# puts in random into the code

options = ["rock", "paper", "scissors"]# Give the options for the code

print("Welcome to Rock, Paper, Scissors!")# Prints the sentence
user_choice = input("Choose rock, paper, or scissors: ").lower()#the three options the user can chose from

while user_choice not in options:# User doesn't chose rock, paper, or scissors
     print("Invalid choice, please choose again.")# Prints this sentence
     user_choice = input("Choose rock, paper, or scissors: ").lower()#the three 

computer_choice = random.choice(options)# Computer chooses randomly from list

print(f"You chose {user_choice}, the computer chose {computer_choice}.")# Prints the choices
 
if user_choice == computer_choice: # If your choice is same as computer
    print("It's a tie!")# Prints the sentence
elif user_choice == "rock":# If your choice is rock
     if computer_choice == "scissors":# If computer chooses scissors
         print("You win!")# Prints the sentence
     else:# Another option
         print("You lose.")# Prints the sentence
elif user_choice == "paper": # If your choice is paper
     if computer_choice == "rock":# If computer choice is rock
         print("You win!")# Prints this sentence
     else:# Another option
         print("You lose.")# Prints this sentence
elif user_choice == "scissors":# If your choice is scissors
     if computer_choice == "paper":# If computer choice is paper
         print("You win!")# Prints this sentence
     else:# Another option
         print("You lose.")# Prints this sentence
