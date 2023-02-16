# this programm demonstrates a guessing game
# get user input
#generate a random number
#using a while loop check if user input is equal to generated number
from random import randint
user_name=input ("what's your name")
print("hello there"+ user_name + "!")
# generate a random number
random_number=45
number=randint(10,50)
counter=0
while counter < 5:
      user_number =  eval(input("enter a number"))
      counter=counter+1
      if user_number<random_number: 
            print("your guess is too slow")
      elif user_number>random_number:
            print("your guess is too high")
      elif user_number ==random_number:
            print("you win")

            break
      print("game over")
if user_number==random_number:
      print("you win")
else:print("game over the correct is ")
print(random_number)
















