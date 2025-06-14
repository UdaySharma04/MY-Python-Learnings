# Q1.) How would you print each character in the string fruit = "apple" using a for loop ?
# ANS1.)  
# fruit = "apple"
# for characters in fruit :
#     print(characters) 

# Q2.) Write a for loop to print only vowels from the word = "education"
# ANS2.) 
# word = "education"
# vowels = 'euaio'
# for characters in word:
#     if characters in vowels:
#         print(characters)

# Q3.) Create a string that says "Welcome John!", then replace "John" with "Jane" using a method.
# ANS3.)
# a = 'Welcome John!'
# print(a.replace('John','Jane'))

# Q4.) Check if the string " \n\t" consists of only whitespace using an appropriate method.
# ANS4.)
# b = "\n\t"
# print(b.isspace())

# Q5.) Write a Python program that takes an integer input from the user and checks if the number is:
#Positive
#Negative
#Zero
# ANS5.) 
# x = int(input('the value of x is :'  ))
# if x>0:
#     print('x is a positive number')
# elif x<0 :
#     print('x is a negative number')
# else:
#     print('x is zero')
 


# Q6.)  Write a Python program that takes a student's score (0 to 100) as input and prints their grade based on the following conditions:
#90 to 100 → Grade A
#80 to 89 → Grade B
#70 to 79 → Grade C
#60 to 69 → Grade D
#Below 60 → Grade F
#If the score is not in the range 0–100, print "Invalid score".

# ANS6.)  
# score = int(input('Students Marks:'  ))
# if 90 <= score <= 100:
#     print('Grade A')
# elif 80 <= score <= 89:
#   print('Grade B')    
# elif 70 <= score <= 79:
#    print('Grade C')
# elif 60 <= score <= 69:
#  print('Grade D')      
# elif 0<= score < 60:
#    print('Grade F')
# else:
#    print('Invalid Score')



# Q7.) Ask the user for a number.
# If it is divisible by 5, print "Divisible by 5".
# If divisible by 11, print "Divisible by 11".
# If divisible by both, print "Divisible by 5 and 11".

# ANS7.) 

# Ask the user for a number
# num = int(input("Enter a number: "))

# # Check divisibility
# if num % 5 == 0 and num % 11 == 0:
#     print("Divisible by 5 and 11")
# elif num % 5 == 0:
#     print("Divisible by 5")
# elif num % 11 == 0:
#     print("Divisible by 11")
# else:
#     print("Not divisible by 5 or 11")



# Q8.) Discount Calculator
# Ask the user for the total shopping amount.
# If the amount > 5000, apply a 20% discount.
# If amount > 2000, apply a 10% discount.
# Otherwise, no discount.

# ANS8.)

# totalamount = float(input('The total amount is : '))
# if totalamount>=5000:
#     discount = totalamount*0.20
#     finalamountafterdiscount = totalamount-discount
#     print('The final amount is : ', finalamountafterdiscount )
# elif totalamount>2000 and totalamount<5000:
#     discount = totalamount*0.10
#     finalamountafterdiscount = totalamount-discount
#     print('The final amount after discount is : ', finalamountafterdiscount)
# else:
#     print('No discount')

#Q9.) Create a program capable of greeting you with Good Morning/Afternoon/Evening.
# ANS9.) 

# import time
# timestamp=time.strftime('%H:%M:%S') 
# print(timestamp)
# hour=int(time.strftime('%H'))
# name=input("What is your name : ")
# if   0<=hour<12:
#     print('Good Morning',name, '!')
# elif  12<=hour<=4:
#     print('Good Afternoon',name, '!')
# else:
#     print('Good Night',name, '!' )




#Q10.) Define a circle class to create a circle with radius r using the constructer.
# Define an Area() method of the class which calculates the area of the circle.
# Define a perimeter() method of the class which allows you to calculate the perimeter of the circle.


# ANS10.)
# class Circle:
#     def __init__(self, radius):
#         self.radius = radius

#     def area(self):
#         return (22/7) * self.radius * self.radius

#     def perimeter(self):
#         return 2 * (22/7) * self.radius

# circle1 = Circle(10)
# print('The area of the circle is:', circle1.area())
# print('The perimeter of the circle is:', circle1.perimeter())
    





#Q11.) Write a Library class with no_of_books and books as two instance variables. Write a program to create a library from this Library class and show how you can print all books, add a book and get the number of books using different methods. Show that your program doesnt persist the books after the program is stopped . 


# ANS11.)
class Library:
    def __init__(self):
        self.books = []
        self.no_of_books = 0

    def add_book(self, book):
        self.books.append(book)
        self.no_of_books += 1

    def print_books(self):
        print("Books in library:")
        for book in self.books:
            print("-", book)

    def get_no_of_books(self):
        return self.no_of_books

# Program starts here
lib = Library()

lib.add_book("Harry Potter")
lib.add_book("The Alchemist")

lib.print_books()
print("Number of books:", lib.get_no_of_books())
