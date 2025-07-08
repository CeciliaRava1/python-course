my_dict = dict()
my_other_dict = {}
my_dict = {
    'Name': 'Luciana', 
    'Age': 13, 
    'Languages': {'Python', 'Swift'}
    }

print(my_dict['Name'])
my_dict['Age'] = 20
my_dict['Country'] = 'Chile'

del my_dict['Age']
print(my_dict)
print('Name' in my_dict)

print(my_dict.items())
print(my_dict.keys())
print(my_dict.values())

# Create new dicts without values
my_new_dict = dict.fromkeys(('Name', 1, 'City'))
print(my_new_dict)

# Create new dict using a list
my_list = ['blue', 'red', 'violet']
my_new_dict = dict.fromkeys((my_list))
print(my_new_dict)