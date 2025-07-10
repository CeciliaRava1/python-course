### lists ###

my_list = list()
my_list_two = []
my_list = [2, 3, 'hello']

my_list.append('bye') # Insert to end
my_list.insert(1, 'green')  # Insert (Index, item)
my_list.remove(2) # Remove first element
my_list.pop() # Remove last element
print(my_list.pop()) # Return deleted element
print(my_list.pop(0)) # Delete index element
del my_list[0] # Delete index element without return

my_list = [2, 3, 4, 5]
my_new_list = my_list.copy()
my_list.clear() # Delete list

# print(my_list.count('bye'))
print(my_list)
print(my_new_list)

my_new_list.reverse()
print(my_new_list)

my_list = [2, 1, 3, 0, 4, 5]
my_list.sort()
print(my_list)

# Sublist
print(my_list[0:3])