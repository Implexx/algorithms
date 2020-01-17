"""
Задание 5
https://drive.google.com/file/d/1lmUebi6gGXK6OeAX-bDrUL3R3FU6YhN6/view?usp=sharing
Пользователь вводит две буквы. Определить, на каких местах алфавита они стоят, и сколько между ними находится букв.
"""


alphabet = 'abcdefghijklmnopqrstuvwxyz'

char_1 = input('Введите первую букву: ')
char_2 = input('Введите вторую букву: ')

num_1 = alphabet.find(char_1) + 1
num_2 = alphabet.find(char_2) + 1

result = abs(num_1 - num_2)

if result > 0:
    result -= 1
print('Между буквами {} и {} находится {} других букв'.format(char_1, char_2, result))
