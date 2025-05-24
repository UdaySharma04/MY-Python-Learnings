                                         # OOP in Python
# OOP is a programming in which we uses objects and classes to structure code.
# It allows for better organization, reusability, and maintainability of code.

 
    
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




# class person():
#     name='jjqc'
#     occupation='software dev'
#     networth = 10000
#     def info(self):
#         print(f"{self.name} is a {self.occupation}")

# a=person()
# a.name='jack'
# a.occupation='accountant'
# # print(a.name,'is a',a.occupation)
# a.info()


# b=person()
# b.name = 'jasper'
# b.occupation = 'HR'
# b.info()

# c = person()
# c.info()





# Constructers

class person():
    def __init__(self,name,occ):
      self.name=name
      self.occ=occ
    def info(self):
        print(f"{self.name} is a {self.occ}")

a = person('peter','Lawyer')
a.info()
