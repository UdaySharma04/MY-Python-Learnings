# This is a simple program to demonstrate the use of if-else statements in Python.



# a=int(input())
# print("your age is",a)
# print(a==18)
# print(a!=18)
# print(a<18)
# print(a>18) 
# print(a<=18)
# print(a>=18)
# if a>=18:
#     print("you are eligible to vote") 
#     print("you are eligible to drive")
# else:
#     print("you are not eligible to vote") 
#     print("you are not eligible to drive")
    
    #Conditional Operators
    # == (equals to)
    # != (not equals to)
    # <
    # >
    # <=
    # >=


# Appleprice=(int(input("Price of 1 kg apple: ")))
# budget=200
# if Appleprice<=budget:
#      print('Hey! siri add 1 kg apples to my cart')
# else:
#      print('Hey! siri do not add 1 kg apples to my cart')




# appleprice =  int(input("Price of 1 kg apple: "))
# budget = 200
# if appleprice <= budget:
#     print("Add 1 kg apples to my cart")
# elif appleprice <= budget + 10 :
#     print("Warning adding 1 kg apples in your cart even through it is eceeding your budget")
#     answer= input("Do you want to add the apples to your cart? (yes/no):")
#     if answer==('yes'):
#          print("Adding 1 kg apples to your cart")
#          print("Added 1 kg apples to your cart")
#     else:
#          print("Did not add 1 kg apples to your cart")
# else:
#     print(" You do not have enough money to buy 1 kg apples")



# num = int(input("Enter a number: "))
# if num==0:
#     print("The number is zero")

# elif num>0:
#         print("The number is positive")


# else:
#         print("The number is negative")
# print("I am happy now")



#num=18 
# if(num<0):
#     print("The number is negative")
# elif(num>0):
#     if (num<=10):
#         print("the number is between 1-10")
#     elif(num>10 and num<=20):
#         print("the number is between 11-20")
#     else:
#         print("the number is zero")






import time
# Get current hour (in 24-hour format)
current_hour = time.localtime().tm_hour

# Greet based on the time of day
if current_hour < 12:
    print("Good morning!")
elif current_hour < 18:
    print("Good afternoon!")
else:
    print("Good evening!")
