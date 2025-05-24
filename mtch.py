#In this we will learn how to use the match statement   And loops :

# x = int(input("Enter a number: "))

# match x:
#     case 0:
#         print('The number is zero')
#     case 90:
#         print('x is equal to 90')  # Handle 90 explicitly
#     case x if x > 0:
#         print('The number is positive')
#     case x if x < 0:
#         print('The number is negative')
    
        
    # isme system line se sab kuch check hota hai jaise ki if else me hota hai pehle case 0 hua phir 90 hua phir x>0 hua phir x<0 hua phir default case hua 
    #default case hamesha last me hota hai kyuki ye sabse pehle nhi ho skta check hota hai
    # or if waale cases hamesha 0 90 jaise cases ke baad check hote hai 






    # loop :

# for i in range(1, 11):
#         print(i)

# name = "John"
# for i in name:
#     print(i)


# name1 = "GGTOPGG"
# for i in name1:
#       print(i)
#       if(i == 'G'):
#           print(" means gangster ")



# Colours = ['red:', 'green:', 'blue:', 'yellow:']
# for i in Colours:
#     print(i)
#     if i == 'red:':
#         print("Red is an aggressive colour")
#     elif i == 'green:':
#         print("Green is a peaceful colour")
#     elif i == 'blue:':
#         print("Blue is a calm colour")
#     elif i == 'yellow:':
#         print("Yellow is a bright colour")






# for i in range(1, 110):
#      print(i+1)




# for k in range(5):
#      print(k)    



# for j in range(1,55,2):
#         print(j) # here 2 is the step size in simple words we can say that it is common difference like we studied in arithmetic progression in maths
# # here 1 is the starting point and 55 is the ending point.

# i=0
# while i<10:
#     print(i)
#     i+=1

# i=int(input(print('the value of i is')))
# while(i<12):
#     i=int(input(print('the value of i is')))
#     print(i)
    

# print('Done with the loop')

# count=10
# while(count>0):
#     print(count)
#     count-=1
# else: 
#     print("Countdown in progress.")



#Do while loop in python
# In python there is no do while loop but we can use while loop to achieve the same functionality

# while True:
#     number=int(input("Enter a positive number "))
#     print(number)
#     if not number >0:
#         break #if the number is not greater than 0 then break the loop


# i=0
# while True :

#     print(i)
#     i=i+1
#     if (i%100 > 0):
        # break  # tab break karo jab i 100 se divide ho jaye bina remainder ke
    # yha pe i ki value 0 se lekar 100 tak chalegi or jab i ki value 100 ho jayegi tab break ho jayega loop
