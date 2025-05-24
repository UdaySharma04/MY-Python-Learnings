# String concatenation
# String concatenation is the process of joining two or more strings together.

# name="harry"
# friend="rohit"
# anotherfriend ="sachin"
# print("hello", name)
# apple= 'He said,\n"I want to eat an orange"'
# print(apple)

hello = '''hi how are you i hope u are doing good 
yeah i am doing good and i hope u are also doing good'''

# print(hello)


name = "harry"
# #        01234
# print(name[0])
# print(name[1])
# print(name[2])
# print(name[3])
# print(name[4])
#print(name[5]) #this will throw an error since the index is out of range 

#alternative way to print the string
# using for loop
# for character in name:
#     print(character)

# print("lets use a for loop\n")

# for character in apple:
#         print(character)



# String Slicing
# String slicing is the process of extracting a portion of a string.
# place='james,bond'
#print(place[0:n]) #it will print the first n characters of the string
# where n is the number of characters to be printed
# for example if n=5 then it will print the first 5 characters of the string
# print(place[0:5])
# print(place[6:10])

# print(len(place)) #it will print the length of the string
# len1 =len(place)-5
# print("mango is a",len1,"letter word")
# print(place[0:4])
# print(place[6:10])
# print(place[:5])

# #negetive slicing
# # negative slicing is the process of extracting a portion of a string from the end of the string.

# print(place[-1]) #it will print the last character of the string
# print(place[0:-3]) # ye puri string likh dega except last 3 characters
# print(place[-5:-1]) #-5 position to -2 position tak ki string dega
# print(place[-5:]) # ye puri string likh dega except last 5 characters  
# print(place[-4:2]) # isme kuch nhi aayega kyuki -4 se 2 right --> left jaa raha hai jabki string left --> right hoti hai


# #  j   a   m   e   s   ,   b   o   n   d
# #  0   1   2   3   4   5   6   7   8   9   (positive indices)
# # -10 -9  -8  -7  -6  -5  -4  -3  -2  -1   (negative indices)



# alphabets="ABCDE"
# for i in alphabets:
#     print(i) # here i is the variable which will take the value of each character in the string alphabets one by one
     
# # Quick Quiz
# #nm="harry"
# #print(nm[-4:-2])

# # h  a  r  r  y
# # 0  1  2  3  4
# # -5 -4 -3 -2 -1
# # nm[-4:-2] = a r

# #Strings are immutable
# # Strings are immutable means that once a string is created, it cannot be changed.
# a="harry"
# print(a.upper()) #it will convert the string into uppercase
# print(a.lower()) #it will convert the string into lowercase
# print(a.title()) #it will convert the first character of each word into uppercase and rest into lowercase
# print(a.capitalize()) #it will convert the first character of the string into uppercase and rest into lowercase


# str1= 'QRTwffwhqFGGGF'
# print(str1.lower())
# print(str1.upper())

# q='??????????? ?????Harry??????? ??????' 
# print(q)
# print(q.rstrip('?')) #it will remove the ? from the right side of the string
# print(q.lstrip('?')) #it will remove the ? from the left side of the string
# print(q.strip('?')) #it will remove the ? from both the sides of the string
# print(q.replace("Harry","jhon")) #it will replace the Harry with jhon in the string
# print(q.split(" ")) #it will split the string into a list of words
# print(q.split("?")) #it will split the string into a list of words using ? as the separator
# print(q.count("?")) #it will count the number of ? in the string
# print(q.count("Harry")) #it will count the number of Harry in the string
# print(q.endswith('?')) #it will check if the string ends with ? or not
# print(q.startswith('?')) #it will check if the string starts with ? or not
# print(q.find("?")) #it will find the first occurrence of ? in the string and return its index
# print(q.find("Harry")) #it will find the first occurrence of Harry in the string and return its index



# blogheading = "pythoN iN 100 DayS ?"
# print(blogheading.capitalize()) #it will convert the first character of the string into uppercase and rest into lowercase
# print(blogheading.title()) #it will convert the first character of each word into uppercase and rest into lowercase
# print(blogheading.center(50)) #it will center the string in a field of 50 characters
# print(blogheading.center(50,'*')) #it will center the string in a field of 50 characters and fill the remaining space with *
# print(blogheading.capitalize().center(50, '*')) #it will center the string in a field of 50 characters and fill the remaining space with * after converting the first character of the string into uppercase and rest into lowercase
# print(blogheading.title().center(50, '*')) #it will center the string in a field of 50 characters and fill the remaining space with * after converting the first character of each word into uppercase and rest into lowercase
# print(blogheading.endswith('?')) #it will check if the string ends with ? or not
# print(blogheading.startswith('q')) #it will check if the string starts with q or not
# print(blogheading.find('i')) #it will find the first occurrence of i in the string and return its index
# print(blogheading.endswith('100',4,13)) #it will check if the string ends with 100 or not in the range of 4 to 13
# print(blogheading.startswith('d',0,15)) #it will check if the string starts with d or not in the range of 0 to 15  its false as d is not in the range of 0 to 15 but D is in the range of 0 to 15
# print(blogheading.index('i')) #it will find the first occurrence of i in the string and return its index
# print(blogheading.isalpha()) #it will check if the string is alphanumeric or not
# print(blogheading.isalnum()) #it will check if the string is alphanumeric or not
# print(blogheading.isdigit()) #it will check if the string is digit or not
# print(blogheading.isnumeric()) #it will check if the string is numeric or not
# print(blogheading.isdecimal()) #it will check if the string is decimal or not
# print(blogheading.islower()) #it will check if the string is lowercase or not
# print(blogheading.isupper()) #it will check if the string is uppercase or not   
# print(blogheading.isprintable()) #it will check if the string is printable or not
# print(blogheading.isspace()) #The isspace() method in Python checks whether a string consists of only whitespace characters. If the string contains only whitespace characters (such as spaces, tabs, or newlines), it returns True. Otherwise, it returns False.
# #Whitespace Characters:
# # ' ' (space)
# # '\t' (tab)
# # '\n' (newline)
# # '\r' (carriage return)
# # '\f' (form feed)
# # '\v' (vertical tab)


# print(blogheading.isidentifier()) #it will check if the string is a valid identifier or not

# print(blogheading.istitle()) #it will check if the string is a title or not
# print(blogheading.startswith('p')) #it will check if the string starts with p or not
# print(blogheading.endswith('s')) #it will check if the string ends with s or not
# print(blogheading.swapcase()) #it will swap the case of the string
# print(blogheading.swapcase().title()) #it will swap the case of the string and then convert the first character of each word into uppercase and rest into lowercase

