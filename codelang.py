# Write a python program to translate a message into secret code language. Use the rules below to translate normal english into secret code language.

# Coding:
# If the word contains atleast 3 characters, remove the first letter and append it at the end of the word.
# Now append three random characters at the starting and end of the word.
# else:
# simply reverse the string.

# Decoding:
# If the word contains atleast 3 characters, reverse it.
# else:
# remove 3 random characters from start and end. Now remove the last letter 

# import random
# import string

# a=str(input("Enter the word to code : "))
# if len(a)>3:
#     first_three = ''.join(random.choices(string.ascii_letters,k=3))
#     last_three = ''.join(random.choices(string.ascii_letters,k=3))
    
#     a=first_three+a[1:]+a[0]+last_three
#     print(a)
# else:
#     a=a[::-1] #this will reverse the string
#     print(a)

# b=str(input("Enter the word to decode: "))
# if len(b)<=3:
#     b=b[::-1]
# else:
#     b=b[3:] # this will remove the first 3 characters
#     b=b[:-3] # this will remove the last 3 characters
#     b=b[-1] + b[:-1] # this will remove the last character and append it at the end
# print(b)


 

#                                      # Short hand if else statement
# a=int(input("Enter a number : "))
# b=int(input("Enter a number : "))

# print("A") if a>b else print("=") if a==b  else print("B")

# print(9) if a>b else ""

# c=10 if a>b else 0
# print(c)





                                            # Enumerate function
# enumerate() ek build in function hai jo kisi iterable object (jaise list, tuple, ya string) ko enumerate karta hai. Ye function har element ke sath uska index bhi return karta hai. Iska istemal loop ke andar index aur value dono ko ek sath access karne ke liye hota hai.
# marks = [12, 56, 32, 98, 25, 45, 1, 4]
# index = 0  # Initialize index outside the loop

# for mark in marks:
#     print(mark)
#     index += 1  # Increment index in each iteration
#     if index == 3:  # Check if the index is 3
#         print('harry, awesome')





# for index , mark in enumerate(marks ):
#      print(mark)
#      if (index == 2):
#             print('harry, awesome')



# for i, item in enumerate(["apple", "banana", "cherry"]):
#     print(i, item)






# Global and Local variables
#global variable is a variable that is declared outside of any function or class and can be accessed from anywhere in the code.

#  A local variable is a variable that is declared inside a function or class and can only be accessed within that function or class.

x=10 #global variable
print(x)   

def hello():
    # global x # this will make the x variable global
    x=5
    y=1
    print('the local x is' ,x) #local variable

hello()
# print(y) # This will throw an error since y is a local variable and cannot be accessed outside the function
print(x)