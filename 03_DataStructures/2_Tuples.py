#Program demonstrates use of Tuple
'''Tuple
Tuples are used to store multiple items in a single variable.
Tuple is one of 4 built-in data types in Python used to store collections of data.
A tuple is a collection which is ordered and unchangeable(immutable).
Tuples are written with round brackets.'''

#Create a tuple:
mytuple = ("apple", "banana", "cherry")
#Print the number of items in the tuple
print(mytuple)

#Tuples allow duplicate values:
mytuple = ("apple", "banana", "cherry", "apple", "cherry")
print(mytuple)

#Tuple Length
#len returns the numbers of elements in the list, not the number of characters
mytuple = ("apple", "banana", "cherry")
print(len(mytuple))

#A tuple can contain(String, int and boolean) different data types:
mytuple = ("abc", 34, True, 40, "male")
print(mytuple)

#Negative Indexing
print(mytuple[-1])

#Range of Indexes
mytuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
#specify a range of indexes by specifying where to start and where to end the range.
print(mytuple[2:5])

#Packing a tuple:
fruits = ("apple", "banana", "cherry")
#Unpacking a Tuple
(green, yellow, red) = fruits
print(green)
print(yellow)
print(red)


tuple1 = ("a", "b" , "c")
tuple2 = (1, 2, 3)
concatenated_tuple = tuple1 + tuple2
print(concatenated_tuple)