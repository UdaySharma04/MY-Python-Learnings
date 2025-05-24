                                      #SNAKE WATER GUN GAME


# Snake Water Gun is a veriation of the classic game Rock Paper Scissors.
# where players uses hand gestures to represent a snake , water or gun.
# The guns beats snake, snake beats water and water beats gun.

# Write a python program to create a snake water gun game in python using if else statements. 


import random
a='snake'
b='water'
c='gun'
user_input=input("Enter snake, water or gun: ")
if user_input not in [a,b,c]:
    print("Please enter a valid input")
    exit()
computer_input=random.choice([a,b,c])
print("Computer's choice: ",computer_input)
if computer_input==a and user_input==b:
    print('You lose! Water is drunk by the snake')
elif computer_input==a and user_input==c:
    print('You win! Snake is killed by the gun')
elif computer_input==b and user_input==c:
    print('You lose! Gun is drowned in the water')
elif computer_input==b and user_input==a:
    print('You win! Water is drunk by the snake')
elif computer_input==c and user_input==a:
    print('You lose! Snake is killed by the gun')
elif computer_input==c and user_input==b:
    print('You win! Gun is drowned in the water')
if computer_input==user_input:
     print("it's a tie!")

