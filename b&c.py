# for i in range(12): 
#     print("5x",i+1, '=',5*(i+1))
#     if i == 9 :
#         break
# print("End of loop")    


# for i in range(15):
#     print("5x",i+1, '=',5*(i+1))
#     if i==12 :
#         continue
#     print("End of loop")


#Functions:


# a=5
# b=10
# gmean=a*b/(a+b)
# print(gmean)
# c=8
# d=7
# gmean1=c*d/(c+d)
# print(gmean1)

                                  #OR



# def calculategmean(a,b):
#     gmean=a*b/(a+b)
#     print(gmean)


# a=5
# b=10
# calculategmean(a,b)

# c=8
# d=7
# calculategmean(c,d)




# def findgreater():  # No need to pass a and b as parameters
#     a = int(input("The value of a is: "))  # Prompt the user for input
#     b = int(input("The value of b is: "))  # Prompt the user for input
#     if a > b:  # Compare a and b
#         print('a is greater')  # Print the greater value
#     else:
#         print('b is greater')  # Print the greater value

        

# # Call the function
# findgreater()  # Execute the function to find the greater value
    


    
#Passing
# def findlesser():
#     pass # ye hold kar deta hai or phir ham ispe vapis baad me aa skte hai or jo karna tha vo kar skte hai
#     a=22
#     b=33
#     findlesser()

# def average(a,b):
#     print('the average is', (a+b)/2)
# average(4,6)


# def name(fname, mname, lname):
#     print("hello",fname, mname, lname)

# # Call the function with arguments
# name("Uday", "G", "Sharma")


# def name(fname, mname = 'jhon', lname = 'whatson'):
#     print("hello,", fname, mname, lname)
# name("JJ")

# def name(fname, mname = 'jhon', lname = 'whatson'):
#      print("hello,", fname, mname, lname)
# name('JJ', 'Sharma')

# def name(fname, mname = 'jhon', lname = 'whatson'):
#      print("hello,", fname, mname, lname)
# name('JJ', 'joshi', 'jackson' )


# def name(fname, mname = 'jhon', lname = 'whatson'):
#      print("hello,", fname, mname, lname)
# name('disco', 'jackson', 'dancer')


# def average(a=9, b=1):
#     print('the average is', (a+b)/2 )
# average()
# average(b=9)
# average(b=9, a=21)
# average(5, 8)

# def name(fname, mname, lname):
#     print('hello', fname, mname, lname)
# name("peter", "quill")  #The issue is that the function name is defined to accept three arguments (fname, mname, and lname)
#You are only passing two arguments ("peter" and "quill"). Since the function expects three arguments and no default value is provided for lname, Python raises a TypeError stating that a required positional argument (lname) is missing.


# def average(*numbers):
#      sum=0
#      for i in numbers:
#          sum=sum+i
#      print('average is:', sum/len(numbers))
# average(4,7,9,8,9)
            #Or
#     return sum/len(numbers)
# c=average(4,7,9,8,9)
# print(c)