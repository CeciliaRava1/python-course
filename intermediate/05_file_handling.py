'''
w+: Rewrite
r+: Read and write
'''


# .txt
import os
txt_file = open('intermediate/my_file.txt', 'w+')
txt_file.write('My name is Jeremias \nMy surname is Gutierrez \nIm 12 Years old \nMy favorite language is Python \n')

print(txt_file.read())
print(txt_file.read(10)) # Ten first char
print(txt_file.readline())
print(txt_file.readline())
for line in txt_file.readlines():
    print(line)

txt_file.write('This is a new text in my file \nThis is a new text in my file')
print(txt_file.readline())
# txt_file.close()
os.remove('intermediate/my_file.txt')


# .json
import json
json_file = open('intermediate/my_file.json', 'w+')
json_test = {
    'name': 'Luciana', 
    'age': 13, 
    'languages': ['Python', 'Swift', 'Kotlin'],
    'website': 'https//moure.dev'}

json.dump(json_test, json_file, indent= 4)
json_file.close()

with open('intermediate/my_file.json') as my_other_file:
    for line in my_other_file.readlines():
        print(line)

json_dict = json.load(open('intermediate/my_file.json'))
print(json_dict)
print(type(json_dict))
print(json_dict['name'])


# .xlsx
import xlrd 

# . xml
import xml

# .csv
import csv
csv_file = open('intermediate/my_file.csv', 'w+')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(["name", "surname", "age", "language", "website"])
csv_writer.writerow(["Luciana", "Gutierrez", 15, "Python", "moure.dev"])
csv_writer.writerow(["Roswell", "", 2, "COBOL", ""])


csv_file.close()

with open('intermediate/my_file.csv') as my_other_file:
    for line in my_other_file.readlines():
        print(line)
