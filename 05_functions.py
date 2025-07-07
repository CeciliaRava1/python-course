def my_function():
    print('I am a function')
my_function()

def sum(firstValue, secondValue):
    sum = firstValue + secondValue
    return sum
sum(2, 3)

def print_name (name, surname):
    print(f'{name} {surname}')
print_name(name = 'Kiara', surname = 'Lopez')

def print_name_default (name = 'Default name'):
    print(f'{name}')
print_name_default()

# Function with Arbitrary Parameters
def print_texts(*text):
    print(text)
print_texts('Hello', 'Python')