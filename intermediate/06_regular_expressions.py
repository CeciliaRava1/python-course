# Inspection strings
import re

my_string = 'This is the: number six lesson'
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