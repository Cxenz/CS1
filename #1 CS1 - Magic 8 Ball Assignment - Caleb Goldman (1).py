'''
Author: Caleb Goldman
Date: 11/13/2023
Description: Asks a rndom question and generates a random response (Magic 8 ball)
Challenges: I did none
Sources: https://www.w3schools.com/python/python_lists_access.asp
'''
import random# puts in random into the code
user = input("ask me a question")# asks a question
thislist = ["yes", "no", "maybe", "learn soon"]# gives random responses to the question
response = random.choice(thislist)# picks a random value from my list
print(response)# prints response to the question
       
