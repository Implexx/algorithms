"""
Задание 9
https://drive.google.com/file/d/1lmUebi6gGXK6OeAX-bDrUL3R3FU6YhN6/view?usp=sharing
Вводятся три разных числа. Найти, какое из них является средним (больше одного, но меньше другого).
"""


num_1 = int(input("Введите первое число :"))
num_2 = int(input("Введите второе число :"))
num_3 = int(input("Введите третье число :"))

if (num_1 > num_2 > num_3) or (num_3 > num_2 > num_1):
    print('Среднее число: ', num_2)
elif (num_2 > num_1 > num_3) or (num_3 > num_1 > num_2):
    print("Среднее число: ", num_1)
else:
    print("Среднее число: ", num_3)
