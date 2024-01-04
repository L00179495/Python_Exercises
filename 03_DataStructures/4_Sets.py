# Program for Set

# Creating a set
fruits = {'apple', 'banana', 'orange'}

# Adding elements to a set
fruits.add('grape')
fruits.add('apple')  # Adding a duplicate element, it won't be added

# Removing an element from a set
fruits.remove('banana')

# Checking if an element exists in a set
print('apple' in fruits)   # True
print('banana' in fruits)  # False

# Iterating over a set
for fruit in fruits:
    print(fruit)

# Set operations
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

# Union of sets
union = set1.union(set2)
print(union)   # {1, 2, 3, 4, 5, 6, 7, 8}

# Intersection of sets
intersection = set1.intersection(set2)
print(intersection)   # {4, 5}

# Difference of sets
difference = set1.difference(set2)
print(difference)   # {1, 2, 3}

# Subset and superset
subset = {1, 2}.issubset(set1)
print(subset)   # True

superset = set1.issuperset({1, 2})
print(superset)   # True