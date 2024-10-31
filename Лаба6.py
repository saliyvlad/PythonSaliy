# #1
# # Инициализация переменных
# heights = []
# max_height = None
# min_height = None

# # Ввод данных
# while True:
#     height = int(input("Введите рост (или 0 для завершения): "))
#     if height == 0:
#         break
#     if height > 0:  # Игнорируем отрицательные значения
#         heights.append(height)

# # Проверка введенных данных
# if len(heights) < 2:
#     print("Некого сравнивать")
# else:
#     max_height = max(heights)
#     min_height = min(heights)
#     print(f"Самый высокий человек с ростом: {max_height}")
#     print(f"Самый низкий человек с ростом: {min_height}")

#2
# total = 0
# for i in range(2, 101, 2):
#     total += i
# print(total)

# #3
# def sum_of_squares(n):
#     return (n * (n + 1) * (2 * n + 1)) // 6

# # Входные данные
# inputs = [6, 2, 100]
# outputs = [sum_of_squares(n) for n in inputs]

# # Вывод результатов
# for n, result in zip(inputs, outputs):
#     print(f"Для n = {n}, y = {result}")

# #4
# n = int(input("Введите высоту елочки: "))

# # Рисуем верхнюю часть елочки
# for i in range(n):
#     print(' ' * (n - i - 1) + '*' * (2 * i + 1))
# # Рисуем ствол елочки
# print(' ' * (n - 1) + '*')

#5
# def dog_age_to_human_years(dog_years):
#     if dog_years < 0:
#         return "Ошибка!"
#     elif dog_years < 2:
#         return dog_years * 10.5
#     else:
#         # Если собака старше 2 лет
#         human_years = 10.5 * 2 + (dog_years - 2) * 4
#         return human_years

# # Примеры входных данных
# input_ages = [1, 3, -7]
# output_ages = []

# for age in input_ages:
#     output_ages.append(dog_age_to_human_years(age))

# print(output_ages)

# #6
# import random
# secret = random.randint(1,10)  
# while True:
#     num = int(input("Введите число от 1 до 10: "))
#     if num == secret:
#         print("Поздравляю! Вы угадали!")
#         break
#     else:
#         print("Нет, ты не угадал. Попробуй снова")

#7
## Ввод данных
# ticket = input("Введите шестизначный номер билета: ")

# # Проверка на корректность
# if len(ticket) != 6 or not ticket.isdigit():
#     print("Некорректный билет")
# else:
#     # Разделение на половины
#     first_half = ticket[:3]
#     second_half = ticket[3:]

#     # Сумма цифр
#     sum_first = int(first_half[0]) + int(first_half[1]) + int(first_half[2])
#     sum_second = int(second_half[0]) + int(second_half[1]) + int(second_half[2])

#     # Проверка на "счастливый" билет
#     if sum_first == sum_second:
#         print("Поздравляю! Ваш билет - счастливый!")
#     else:
#         print("Обычный билет")

#8
# # Ввод двоичного числа как строки
# binary_number = input("Введите двоичное число: ")

# # Инициализация переменных
# decimal_number = 0
# power = 0

# # Перебор двоичного числа с конца
# for i in range(len(binary_number) - 1, -1, -1):
#     if binary_number[i] == '1':
#         decimal_number += 2 ** power
#     power += 1

# # Вывод результата
# print("Десятичное число:", decimal_number)