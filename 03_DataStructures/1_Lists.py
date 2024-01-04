#Program demonstrates use of Lists
'''List
Lists are used to store multiple items in a single variable.
Lists are one of 4 built-in data types in Python used to store collections of data.
Lists are created using square brackets:'''

#Create a List:
mylist = ["apple", "cherry", "banana", "kiwi", "melon"]
#Print the number of items in the list
print(mylist)


#len returns the numbers of elements in the list, not the number of characters
print(len(mylist))

#Range of Indexes
#You can specify a range of indexes by specifying where to start and where to end the range.
slice=mylist[2:5]
print(slice)

#Negative indexing means start from the end
# -1 refers to the last item, -2 refers to the second last item 
my_character=mylist[-1]
print()

#lists are mutable, individual items may be indexed and selectively edited
mylist[1:2] = ["blackcurrant", "watermelon"]
print(mylist)

#Append Items
mylist.append("mango")
print(mylist)

#Insert Items
#To insert a list item at a specified index, use the insert() method.
mylist.insert(1, "orange")
print(mylist)

#Remove Specified Item
#The remove() method removes the specified item.
mylist.remove("banana")
print(mylist)

#Remove Specified Index
#The pop() method removes the specified index.
mylist.pop(1)
print(mylist)

#sort() method that will sort the list alphanumerically, ascending, by default:
mylist.sort()
print(mylist)

#list_of_values=mylist.split(",")
#print(list_of_values)

#concatenate list
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]
concatenated_list = list1 + list2
print(concatenated_list)