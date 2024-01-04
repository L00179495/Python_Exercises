my_list = []
my_string = "Happy Newyear!"

#Append string
for letter in my_string:
    my_list.append(letter)
print(my_list)

# iterable object
my_string = "Happy Newyear!"
my_list = [letter for letter in my_string]
print(my_list)

#Range of Index
my_list = [number for number in range(0,20)]
print(my_list)

my_list = [number * 10 for number in range(0,20)]
print(my_list)

my_list = [number * 10 for number in range(0,20) if number < 10]
print(my_list)


#convert feet to meters, rounded to 2 decimal places.
conversion = 0.3048
my_depth_in_feet = [12.3, 13.8, 15.3, 12.1, 8.8]
my_depth_in_meters = [(round(depth * conversion, 2)) for depth in my_depth_in_feet] 
print(my_depth_in_meters)