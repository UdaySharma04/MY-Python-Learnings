                                         # OOP in Python
# OOP is a programming in which we uses objects and classes to structure code.
# It allows for better organization, reusability, and maintainability of code.

 # There are four main principles of OOP:
# Abstraction , Encapsulation , Inheritence , Polymorphism
    
# 🌟 What is OOP?
# OOP = Object Oriented Programming
# It's a style of coding where you organize your code into blueprints (classes) and real things (objects).
# Helps make big code clean and easy to manage.  
# Also used to create our own methods . 

            

# 🧱 What is a Class?
# A class is like a blueprint for creating objects./User defined data types.

# 🧍 What is an Object?
# An object is a real thing made using the class.

# 🧠 Tip to Remember:
# Class = Blueprint/template
# Object = Real thing built from blueprint
# If Student is the plan, then s1 and s2 are actual students



#Ceating a class
# class student:
#     name = "John"
#     age = 20

# In this above lines name and age are class attributes.
#     # This is a class named student with two attributes: name and age.

# # Creating an object(instance) of the class
# s1 = student()  # s1 is an object of the class student
# print(s1)  # This will print the memory address of the object s1
# # Accessing attributes of the object
# print(s1.name)  # Accessing the name attribute of the object s1
# print(s1.age)   # Accessing the age attribute of the object s1




#Constructers in Python
# A constructor is a special method that is automatically called when an object is created.
# All classes have a function called __init__() which is always executed when an object is created.

# class student:
#     college_name = "ABC University"  # This is a class attribute this will be common for all objects of the class student until we change it in objects.
#     name = 'anonymous'  # Class attribute 
#     # Defult constructor
#     def __init__(self):
#         pass
#     # Parameterized constructor
#     def __init__(self,name,age):
#         print('init method called every time we use () to create an object')
#         print(self)
#         self.name =name
#         self.age = age
# # The self parameter refers to the instance of the class itself, allowing access to its attributes and methods.
# s1=student('John',20)  # s1 is an object of the class student
# s2=student('Doe',22)  # s2 is another object of the class student
# print(s1.name)  # Accessing the name attribute of the object s1
# print(s1.age)   # Accessing the age attribute of the object s1
# print(s2.name)  # Accessing the name attribute of the object s2
# print(s2.age)   # Accessing the age attribute of the object s2

# Here john and doe are object attributes of the class student.


# Object atrributes>>>>>>>>>>Class atrributes
# Object attributes are specific to each object, while class attributes are shared by all objects of the class.
# Class attributes are defined directly within the class, while object attributes are defined within the constructor or methods.


# Methods
# class student:
#     def __init__(self,fullname):
#         self.name = fullname
#     def hello(self):
#             print('hello',self.name)
        
# s1 = student('harry')
# s1.hello()



# Practice :-    
# Create a class student that takes name & marks of 3 subjects as arguments in constructor .
# Then create a methid to print average .

# class student:
#     def __init__(self,name,physics_marks,chemistry_marks,maths_marks):
#         self.name = name
#         self.physics_marks = physics_marks
#         self.chemistry_marks = chemistry_marks
#         self.maths_marks = maths_marks
#     def avg(self):
#             avg = (self.physics_marks + self.chemistry_marks + self.maths_marks)/3
#             print('The average of marks of',self.name,'is',avg)
# s1 = student('harry', 85, 90, 95)
# s1.avg()


# Static Method (methods that don't use the self parameter[works at class level])   # It is a decorator
# Static methods are methods that belong to the class rather than any specific object.
# They can be called on the class itself without creating an instance of the class.
# class student:
#     @staticmethod
#     def college():
#         print('ABC University')
# s1 = student()
# s1.college()  # Calling the static method on the object



#Abstraction
#Hiding the implimentation details of a class and showing only the essential features to the user.

# class car:
#     def __init__(self):
#         self.acc = False
#         self.brake = False
#         self.clutch = False
#     def start(self):
#      self.clutch = True
#      self.clutch =True
#      print('car started...')
# car1=car()
# car1.start()  # This will call the start method of the car class, which will print 'car started...'



# Encapsulation
# Wrapping data and function into a single unit(object).


#Practice :-
# Create account class with 2 attributes - balance and acc number.
# Create methods for debit , credit and printing the balance. 

# class account:
#    def __init__(self,balance,acc_number):
#       self.balance = balance
#       self.acc_number = acc_number

#    def debit(self,amount):
#       self.balance -=amount
#       print('Amount deducted:', amount)
#       print('Total balance =',self.get_balance())

#    def  credit(self ,amount):
#         self.balance += amount
#         print('Amount added:', amount)
#         print('Total balance =',self.get_balance())
        

#    def get_balance(self):
#       return self.balance
     
# acc1= account(1000, '1234567890')  # Creating an object of the account class with initial balance and account number
# acc1.debit(100)
# acc1.credit(200)  



# del keyword
# Used to delete an object or its properties.
# class student:
#     def __init__(self,name):
#         self.name = name

# s1=student('harry')
# # del s1.name 
# print(s1.name)  # This will raise an AttributeError because the name attribute has been deleted.
# print(s1)





# Private Attributes and Methods
# In Python, we can make attributes and methods private by prefixing their names with double underscores (__).
# This means they cannot be accessed directly from outside the class.
# class account:
#     def __int__(self,acc_no,acc_paas):
#         self.acc_no = acc_no
#         self.__acc_pass = acc_paas # by prefixing with __, we make it private.
# acc1 = account('1234567890', 'mypassword')
# print(acc1.acc_no)  # This will print the account number.
# print(acc1.__acc_pass)  # This will raise an AttributeError because __acc_pass is private and cannot be accessed directly.





# More simple example of private attributes and methods
# class person:
#     __name = 'anonymous'
# p1 = person()
# print(p1.__name)  # This will raise an AttributeError because __name is private and cannot be accessed directly.





# Inhertence :-
# When one class derives the properties & methods of another class .



# 💫⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐💫
# Types of Inheritance
# Single Inheritance
# A type of inheritance where a child class inherits from only one parent class.

# Multilevel Inheritance
# A type of inheritance where a class is derived from a class that is already derived from another class.

# Multiple Inheritance
# A type of inheritance where a child class inherits from more than one parent class.


# Hierarchical Inheritance:
# Multiple child classes inherit from a single parent class.

# Hybrid Inheritance:
# A combination of two or more types of inheritance, such as multiple and multilevel inheritance.
# 💫⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐💫


# Example of Single Inheritance
# class car:
#     color = 'black'
#     @staticmethod
#     def start():
#         print('car started ... ')

#         @staticmethod
#         def stop():
#          print('car stopped')

# class toyotacar(car):
#     def __init__(self,name):
#      self.name = name

# car1 = toyotacar('fortuner')
# car2 = toyotacar('prius')
# print(car1.start())
# print(car1.color)


# Example of Multilevel Inheritance
# class car:
#     color = 'black'
#     @staticmethod
#     def start():
#         print('car started ... ')

#     @staticmethod
#     def stop():
#         print('car stopped')

# class toyotacar(car):
#     def __init__(self, brand):
#         self.brand = brand

# class fortuner(toyotacar):
#     def __init__(self,type):
#         self.type = type

# car1 = fortuner('diesel')
# car1.start()




# Example of Multiple Inheritance
# class A:
#     varA = 'welcome to class A'
# class B:
#     varB = 'welcome to class B'
# class C(A, B):
#         varC = 'welcome to class C'
# c1=C()
# print(c1.varA)  # Accessing variable from class A
# print(c1.varB)  # Accessing variable from class B
# print(c1.varC)  # Accessing variable from class C




# Hierarchical Inheritance
class baseclass:
    pass
class childclass1(baseclass):
    pass
class childclass2(baseclass):
    pass
class childclass3(childclass1,childclass2):
    pass

# Hybrid Inheritance
# class parent1:
#     pass
# class parent2:
#     pass
# class child1(parent1):
#     pass
# class child2(parent2):
#     pass
# class child3(child1, child2):
#     pass



# Super() method
# It is used to access methods and properties of a parent class from a child class.
# class car:
#     def __init__(self,type):
#         self.type = type

#     @staticmethod
#     def start():
#         print('car started ... ')

#     @staticmethod
#     def stop():
#          print('car stopped')

# class toyotacar(car):
#     def __init__(self,name,type):
#      super().__init__(type)  # Calling the constructor of the parent class car
#      self.name = name
    

# car1 = toyotacar('fortuner','electric')
# print(car1.type)






# Class Method
# Class methods are methods that are bound to the class and not the instance of the class.
# class person:
#     name = 'anonymous'  # Class attribute
#     # def changename(self,name):
#     #     self.name = name
#     @classmethod
#     def changename(cls, name):
#         cls.name = name  # Changing the class attribute name
# p1 =person()
# p1.changename('pawan')
# print(p1.name)
# print(person.name)


# Property Decorator
# class student:
#     def __init__(self,phy,chem,maths):
#         self.phy = phy
#         self.chem = chem
#         self.maths = maths
#     # def calcpercentage(self):
#     #     self.percentage = (self.phy + self.chem + self.maths) / 3 + '%'    
#     @property
#     def percentage(self):
#          return (self.phy + self.chem + self.maths) / 3
# stud1 = student(98, 90, 95)
# print(stud1.percentage)

# stud1.phy=86
# print(stud1.percentage)




# Polymorphism : Operator Overloading
# When the same operator is allowed to have different meaning according to the context.
# For example, the '+' operator can be used to add numbers or concatenate strings.
# print(2 + 3)  # This will add two numbers
# print('Hello' + ' World')  # This will concatenate two strings.
class complex:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    def shownum(self):
        print(self.real, 'i'  ' +', self.imag, 'j')

    def __add__(self, num2):
        numreal = self.real + num2.real
        numimag = self.imag + num2.imag
        return complex(numreal, numimag)
    
num1 = complex(2, 3)
num1.shownum()
num2 = complex(4, 5)
num2.shownum()
num3 = num1.__add__(num2)
num3.shownum()  # This will print the sum of the two complex numbers

