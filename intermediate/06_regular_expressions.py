### regular expressions ###

# Inspection strings
import re

my_string = 'This is the: number six 6 lesson'
my_other_string = 'This is not the number five lesson'

# match (search from the init)
match = re.match('This is the number', my_string, re.I)
print(match)
# start, end = match.span()
# print(my_string[start:end])

match = re.match('This is the number', my_other_string)
if not(match == None):
    print(match)
    start, end = match.span()
    print(my_string[start:end])


# search
search = re.search('lesson', my_string, re.I)
print(search)
start, end = search.span()
print(my_string[start:end])


# findall
find_all = re.findall('lesson', my_string, re.I)
print(find_all)


# split
print(re.split(':', my_string))


# sub
print(re.sub('lesson', 'LESSON', my_string))


# patterns
pattern = r'[lL]esson'
print(re.findall(pattern, my_string))

pattern = r'[lL]esson|number'
print(re.findall(pattern, my_string))
print(re.match(pattern, my_string))

pattern = r'[0-9]'
print(re.findall(pattern, my_string))
print(re.search(pattern, my_string))

pattern = r'\d'
print(re.findall(pattern, my_string))

pattern = r'\D'
print(re.findall(pattern, my_string))

pattern = r'[l].*'
print(re.findall(pattern, my_string))

# email validation regex 
email = 'mouredev@mouredev.com'
pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
print(re.match(pattern, email))
print(re.search(pattern, email))
print(re.findall(pattern, email))

email = 'mouredev@mouredev.com.mx'
print(re.findall(pattern, email))
