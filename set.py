                                   #Sets
s={2,4,2,9,7,6,4,9}      #(sets don't take repeteted value and don't maintain the order )
print(s)                  #(sets are unchangable you cannot change items inside set once created and sets also do not contain duplicate items )
info={'carla',19,'false',5.9,19}
print(info)
#quick quiz :-
#try to create an empty set and check by type() that weather the type of your veriable is a set or not.
# t={}
# print(t)
# print(type(t))  # This will show a dict as the brackates used for dict and sets are same {}.
#To create an empty set we will have to do the following things :-
# p=set()
# print(p)
# print(type(p))                                   


# for value in info :
#     print(value)

# for value in s :
#     print(value)



# Set methods :-
p1={1,2,3,5,4,8,6,9,0,7}
p2={3,4,6,2,2,7}
# print(p1.union(p2)) #(union) #all the elements of p1 and p2 .
# print(p1.intersection(p2)) #(intersection)  #all the common elements that are present in both p1 and p2 .
# p1.update(p2)  # all the values of p2 will merge with p1 here update means union
# print(p1)
# p1.intersection_update(p2)
# print(p1)

#Simmetric difference :-       vo saari values jo ki common nhi hai
#(p1 U p2) - (p1 ∩ p2)

# o=p1.symmetric_difference(p2)
# print(o)

# f=p1.symmetric_difference_update(p2)
# print(p1)


# The difference btw symmetric_difference() and symmetrc_difference_update() is that
#symmetric_difference() returns a new set whereas symmetrc_difference_update() updates the original one .



# Disjoint sets are the sets which are not related to each other .
#  p1 and p2 are not disjoint sets as they both have value in common .
print(p1.isdisjoint(p2))


#Superset :-
# A superset is a mathematical concept used in set theory. If we have two sets, say A and B, then A is called a superset of B if A contains all the elements of B, and possibly more. This is written as A ⊇ B.
#For example:-
#If A = {1, 2, 3, 4} and B = {1, 2}, then A is a superset of B because A contains everything in B and additional elements.
# print(p1.issuperset(p2))
# print(p2.issubset(p1))

p1.add(100)
print(p1)

p1.remove(100)
print(p1)
        #Or
p1.discard(p1)
print(100)


#remove() raises a KeyError if the element is not found in the set.
#discard() does nothing if the element is not found.
#example:-

my_set = {1, 2, 3}

# Using remove() (raises KeyError if element is not found)
my_set.remove(2)  # Works fine
# my_set.remove(4)  # Raises KeyError: 4

# Using discard() (does nothing if element is not found)
my_set.discard(3)  # Works fine
my_set.discard(4)  # Does nothing, no error

#pop()
#pop() removes and returns a random element from a set (or the last element from a list). If the set is empty, it raises a KeyError.
J=p1.pop()
print(J)

# del p1 # del deletes the entire set object, completely removing it from memory.
# print(p1)

# clear() removes all elements from a set, but the set itself remains in memory as an empty set
p1.clear()
print(p1)