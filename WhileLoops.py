### Part Two -- your code goes here. 
import random
SecretNo = random.randint(1, 100)#
#print(SecretNo)
NoGuessed = 0
while NoGuessed != SecretNo:
    NoGuessed = int(input("Please guess a number between 1 and 100"))
    if NoGuessed != SecretNo:
        print("You have guessed the wrong number")
    elif NoGuessed == SecretNo:
        print("You have guessed the correct number")
    else:
        print("Invalid answer")

    