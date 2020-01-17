"""
Задача 6
https://drive.google.com/file/d/1lmUebi6gGXK6OeAX-bDrUL3R3FU6YhN6/view?usp=sharing
Пользователь вводит номер буквы в алфавите. Определить, какая это буква.
"""


alphabet = 'abcdefghijklmnopqrstuvwxyz'
number = int(input('Введите порядковый номер буквы в алфавите: '))
char = alphabet[number - 1]
print('Ваша буква: ', char)
