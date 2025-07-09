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
txt_file.close()
os.remove('intermediate/my_file.txt')


# .json
import json
json_file = open('intermediate/my_file.json', 'w+')
json_test = {
    'name': 'Luciana', 
    'age': 13, 
    'language': 'Python',
    'website': 'https//moure.dev'}
