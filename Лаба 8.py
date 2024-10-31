# #1
# # Входные данные
# input_data = ['1', 'a', '3', '4', 'b', '6']

# # Инициализация списков для букв и цифр
# letters = []
# numbers = []

# # Разделение на буквы и цифры
# for item in input_data:
#     if item.isdigit():
#         numbers.append(item)
#     else:
#         letters.append(item)

# # Вывод результатов
# for number in numbers:
#     print(number)
# for letter in letters:
#     print(letter)

# #2
# import random

# # Заданные числа
# input_numbers = {1, 45, 34, 23, 31, 45}

# # Генерация случайных чисел
# lottery_numbers = set()
# while len(lottery_numbers) < 6:
#     lottery_numbers.add(random.randint(1, 49))

# # Проверка на совпадение
# matches = input_numbers.intersection(lottery_numbers)

# print("Сгенерированные номера:", lottery_numbers)
# print("Совпадения:", matches)

# #3
# # Входные данные
# numbers = [1, 5, 2, 4, 3]
# output = []

# # Проходим по списку и сравниваем с предыдущим элементом
# for i in range(1, len(numbers)):
#     if numbers[i] > numbers[i - 1]:
#         output.append(numbers[i])

# # Вывод результата
# print(output)

# #4
# # Инициализация списка для ввода чисел
# numbers = []

# # Запрос чисел у пользователя
# while True:
#     num = input("Введите число (или нажмите Enter для завершения): ")
#     if num == "":
#         break
#     numbers.append(float(num))

# # Вычисление среднего значения
# mean_value = sum(numbers) / len(numbers) if numbers else 0

# # Формирование списков ниже и выше среднего
# below_mean = [n for n in numbers if n < mean_value]
# above_mean = [n for n in numbers if n > mean_value]

# # Вывод результатов
# print(f"Среднее значение: {mean_value}")
# print("Числа ниже среднего:", below_mean)
# print("Числа выше среднего:", above_mean)

#5
# # Входные данные
# heights = [215, 207, 196, 176, 168, 166]
# andrey_height = 176

# # Сортируем массив для правильного определения позиции
# heights.sort(reverse=True)

# # Определяем позицию Андрея
# position = 0
# for height in heights:
#     if height > andrey_height:
#         position += 1
#     elif height == andrey_height:
#         position += 1  # Андрей встает после людей с одинаковым ростом
#         break

# # Позиция Андрея - это номер в массиве + 1
# andrey_position = position + 1

# print(andrey_position)

#6
# import random

# def simulate_coin_toss():
#     count = 0
#     consecutive_heads = 0
#     consecutive_tails = 0

#     while consecutive_heads < 3 and consecutive_tails < 3:
#         toss = random.choice(['O', 'P'])
#         print(toss, end=' ')
#         count += 1
        
#         if toss == 'O':
#             consecutive_heads += 1
#             consecutive_tails = 0
#         else:
#             consecutive_tails += 1
#             consecutive_heads = 0

#     print(f"\nПопыток: {count}")

# simulate_coin_toss()

#7
# def luhn_check(card_number):
#     # Преобразуем номер карты в список цифр
#     digits = [int(d) for d in str(card_number)]
#     # Удвоим каждую вторую цифру, начиная с последней
#     for i in range(len(digits) - 2, -1, -2):
#         digits[i] *= 2
#         if digits[i] > 9:
#             digits[i] -= 9
#     # Суммируем все цифры
#     total_sum = sum(digits)
#     # Проверяем, делится ли сумма на 10
#     return total_sum % 10 == 0

# # Входные данные
# card_numbers = [
#     427644003366511,
#     427644003366512,
#     427613366513
# ]

# # Проверяем номера карт
# for number in card_numbers:
#     if luhn_check(number):
#         print(f"{number}: Корректный номер")
#     else:
        # print(f"{number}: Некорректный номер")