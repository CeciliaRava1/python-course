# unordered (no index), unique items
my_set = set()
my_other_set = {}

my_other_set = {'hello', 'world', 21}
print(type(my_other_set))

my_other_set.add('bye')
print(my_other_set)

print('world' in my_other_set)
my_other_set.remove('world')
my_other_set.clear() # Clear object
del my_other_set # Delete object
