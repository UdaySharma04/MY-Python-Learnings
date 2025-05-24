# def double(x):
#     return x * 2

# double = lambda x : x*2
# cube = lambda y : y*y*y
# avg = lambda a, b : (a + b) / 2

# print(double(5))
# print(cube(5))
# print(avg(2,10))




# def appl(fx,value):
#     return 6+fx(value)
# print(appl(cube,2))
# print(appl(lambda x: x*2,2)) 






                     # Map Filter and Reduce
# def square(x):
#     return x*x
# print(square(5))

#MAP                    Takes a function and applies it to every item in a list.
l = [1,2,3,4,5]
# newl=[]
# for items in l:
#     newl.append(square(items))
# print(newl)

# newl=map(square,l)
# print(newl)
# print(list(newl))

# FILTER                      Picks only the items from a list that meet a condition.
# def filter_function(a):
#     return a>3
    
# newl=filter(filter_function,l)
# print(newl)
# print(list(newl))


# # REDUCE                           Combines all items in a list into a single result.
# from functools import reduce
# sum=reduce(lambda x,y:x+y,l) # reduce is used to apply a function of two arguments cumulatively to the items of an iterable, from left to right, so as to reduce the iterable to a single value.
# print(sum)






# is  and == 

# a=1
# b=1
# a=[1,2,31]
# b=[1,2,31]
# print(a is b) # is operator checks if two 'variables' point to the same object in memory .
# print(a==b) # == operator checks if the 'values' of two variables are equal .


