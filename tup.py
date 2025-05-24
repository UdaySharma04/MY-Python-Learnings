# tup=(1,5,6,4,8,7)         
# print(type(tup),tup)
# tup1=(1)
# print(type(tup1))
# tup2=(1,)
# print(type(tup2))
# tup3=tup[1:5]
# print(tup3)
# countries1=('shri lanka', 'afganistan')
# countries2=('virtnam', 'india','china')
# southeastasia= countries1 + countries2
# print(southeastasia)
# tuple1=(0,1,2,4,2,3,4,3,2,3,4,6,8,3)
# w=tuple1.count(3)
# print('The numner of 3 in this tuple is : ', w)
# r=tuple1.index(3)
# print('The first occurence of 3 is at',r)
# # In Python, the notation (a:b:c) is used in slicing, and it represents the start, stop, and step/Skip values for slicing a sequence (like a list, tuple, or string).
# d=len(tuple1)
# print('The len of tuple1 is', d)




                         # String formatting 


# letter='hey my name is {} and i am from {}'
# country = 'india'
# name = 'jj'
# print(letter.format (name ,country))

# price=23.343233
# txt='for only {price:.2f} dollars!'  # :.2f is used if anyone wants to put only 2 decimal places.
# print(txt.format(price=price))

# This was a little confusing that's why f-strings were introduced . 


                         # f-string


# print(f"hey my name is { name } and i am from {country}")
# txt=f'for only {price:.2f} dollars!'   
# print(txt)
# print(f"hey my name is {name} and i am from {country} and i am using f-string here")
# print(f"hey my name is {{name}} and i am from {{country}}") # If we want to  show the curly brackets we have to apply them twice and it will also not take the values than


                     # Doc-strings
# Doc-strings are used to **Doc-strings** (short for documentation strings) are used in Python to provide documentation for modules, classes, methods, or functions. They describe what the code does and how it works, making it easier for others (or yourself) to understand the purpose of the code.

# Doc-strings are used to describe what the code does and how it works, making it easier for others (or yourself) to understand the purpose of the code.
# It provide documentation for modules, classes, method, or functions.


# def square(n): #doc-string are written just after function
#     '''Takes in a number n , and returns the square of n '''    
#     print(n**2)
# square(3)
# print(square.__doc__)



                         #PEP8 
                    #(Python enhancement proposel)
#PEP8 is a document that provides guidlines and best practices on how to write python code.


# Zen of python
#The Zen of Python is a collection of guiding principles for writing computer programs in the Python language. 
# import this 


                                  # Recursion
# function inside the function
#factorial = n(n-1)(n-2).......1 = n(factorial of n-1)
# #0!=1
# def factorial(n):
#     if n==0 or n==1 :
#         return 1
#     else:
#         return n*factorial(n-1)
# print(factorial(10))


# Fibunacci sequence :
#f0 = 0
#f1 = 1
#f2 = f1+f0 = 1
#f3 = f2+f1 = f1+f0+f1 = 2
#fn = f(n-1) + f(n-2)


#write a program to print fibunacci sequence  
# f0 = 0
# f1 = 1
# # f2 = f1+f0 = 1
# # f3 = f2+f1 = f1+f0+f1 = 2
# #fn = f(n-1) + f(n-2)
# def fibunacci(n):
#     if n==0:
#         return 0
#     elif n==1:
#         return 1
#     else:
#         return fibunacci(n-1)+fibunacci(n-2)   
# print(fibunacci(8))



