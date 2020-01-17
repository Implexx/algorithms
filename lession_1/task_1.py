"""
Задание 1
https://drive.google.com/file/d/1lmUebi6gGXK6OeAX-bDrUL3R3FU6YhN6/view?usp=sharing
Найти сумму и произведение цифр трехзначного числа, которое вводит пользователь.
"""

number = input("Введите трехзначное число: ")
num_1 = int(number[0])
num_2 = int(number[1])
num_3 = int(number[2])

result_sum = num_1 + num_2 + num_3
result = num_1 * num_2 * num_3

print('Сумма цифр = ', result_sum)
print("Произведение цифр = ", result)
