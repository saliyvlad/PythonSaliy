# Реши на питоне без библиотек
# preview
# def luhn_algorithm(card_number):
#     def digits_of(n):
#         return [int(d) for d in str(n)]
    
#     digits = digits_of(card_number)
#     odd_digits = digits[-1::-2]
#     even_digits = digits[-2::-2]
    
#     checksum = sum(odd_digits)
    
#     for d in even_digits:
#         checksum += sum(digits_of(d * 2))
    
#     return checksum % 10 == 0

# # Входные данные
# card_numbers = [
#     "4276440013361511",
#     "4276440013361512",
#     "42761336512"
# ]

# # Вывод результатов
# for number in card_numbers:
#     is_valid = luhn_algorithm(number)
#     print(f"{number}: {'Корректный номер' if is_valid else 'Некорректный номер'}")
# Этот код проверяет номера карт по алгоритму Луна и выдает, корректен ли каждый номер.

# GPT-4o
# Исправь код для корректного решения
# preview
# Вот исправленный код для проверки номера банковской карты по алгоритму Луна:

# def validate_card_number(card_number):
#     # Переводим номер карты в список чисел
#     digits = [int(d) for d in str(card_number)]
    
#     # Удваиваем каждую вторую цифру с конца и вычитаем 9, если результат больше 9
#     for i in range(len(digits) - 2, -1, -2):
#         digits[i] *= 2
#         if digits[i] > 9:
#             digits[i] -= 9
    
#     # Суммируем все цифры
#     total_sum = sum(digits)
    
#     # Проверяем, делится ли сумма на 10
#     return total_sum % 10 == 0

# # Примеры проверки
# card_numbers = [
#     "4276440013361511",
#     "4276440013361512",
#     "42761336512"
# ]

# for number in card_numbers:
#     if validate_card_number(number):
#         print(f"{number}: Корректный номер")
#     else:
#         print(f"{number}: Некорректный номер")
# Этот код проверяет номер карты и выводит, является ли он корректным согласно алгоритму Луна.

# GPT-4o
# Исправь код : def luhn_algorithm(card_number):
#     def digits_of(n):
#         return [int(d) for d in str(n)]
    
#     digits = digits_of(card_number)
#     odd_digits = digits[-1::-2]
#     even_digits = digits[-2::-2]
    
#     checksum = sum(odd_digits)
    
#     for d in even_digits:
#         checksum += sum(digits_of(d * 2))
    
#     return checksum % 10 == 0

# # Входные данные
# card_numbers = [
#     "4276440013361511",
#     "4276440013361512",
#     "42761336512"
# ]

# # Вывод результатов
# for number in card_numbers:
#     is_valid = luhn_algorithm(number)
#     print(f"{number}: {'Корректный номер' if is_valid else 'Некорректный номер'}")
# preview
# The provided code for the Luhn algorithm is mostly correct but needs a small adjustment to handle non-numeric card numbers. I'll fix it for you:

# def luhn_algorithm(card_number):
#     def digits_of(n):
#         return [int(d) for d in str(n)]
    
#     digits = digits_of(card_number)
#     odd_digits = digits[-1::-2]
#     even_digits = digits[-2::-2]
    
#     checksum = sum(odd_digits)
    
#     for d in even_digits:
#         checksum += sum(digits_of(d * 2))
    
#     return checksum % 10 == 0

# # Input data
# card_numbers = [
#     "4276440013361511",
#     "4276440013361512",
#     "42761336512"
# ]

# # Output results
# for number in card_numbers:
#     if number.isdigit():
#         is_valid = luhn_algorithm(number)
#         print(f"{number}: {'Корректный номер' if is_valid else 'Некорректный номер'}")
#     else:
#         print(f"{number}: Некорректный номер")
# # #1
# # # Входные данные
# # input_data = ['1', 'a', '3', '4', 'b', '6']

# # # Инициализация списков для букв и цифр
# # letters = []
# # numbers = []

# # # Разделение на буквы и цифры
# # for item in input_data:
# #     if item.isdigit():
# #         numbers.append(item)
# #     else:
# #         letters.append(item)

# # # Вывод результатов
# # for number in numbers:
# #     print(number)
# # for letter in letters:
# #     print(letter)

# # #2
# # import random

# # # Заданные числа
# # input_numbers = {1, 45, 34, 23, 31, 45}

# # # Генерация случайных чисел
# # lottery_numbers = set()
# # while len(lottery_numbers) < 6:
# #     lottery_numbers.add(random.randint(1, 49))

# # # Проверка на совпадение
# # matches = input_numbers.intersection(lottery_numbers)

# # print("Сгенерированные номера:", lottery_numbers)
# # print("Совпадения:", matches)

# # #3
# # # Входные данные
# # numbers = [1, 5, 2, 4, 3]
# # output = []

# # # Проходим по списку и сравниваем с предыдущим элементом
# # for i in range(1, len(numbers)):
# #     if numbers[i] > numbers[i - 1]:
# #         output.append(numbers[i])

# # # Вывод результата
# # print(output)

# # #4
# # # Инициализация списка для ввода чисел
# # numbers = []

# # # Запрос чисел у пользователя
# # while True:
# #     num = input("Введите число (или нажмите Enter для завершения): ")
# #     if num == "":
# #         break
# #     numbers.append(float(num))

# # # Вычисление среднего значения
# # mean_value = sum(numbers) / len(numbers) if numbers else 0

# # # Формирование списков ниже и выше среднего
# # below_mean = [n for n in numbers if n < mean_value]
# # above_mean = [n for n in numbers if n > mean_value]

# # # Вывод результатов
# # print(f"Среднее значение: {mean_value}")
# # print("Числа ниже среднего:", below_mean)
# # print("Числа выше среднего:", above_mean)

# #5
# # # Входные данные
# # heights = [215, 207, 196, 176, 168, 166]
# # andrey_height = 176

# # # Сортируем массив для правильного определения позиции
# # heights.sort(reverse=True)

# # # Определяем позицию Андрея
# # position = 0
# # for height in heights:
# #     if height > andrey_height:
# #         position += 1
# #     elif height == andrey_height:
# #         position += 1  # Андрей встает после людей с одинаковым ростом
# #         break

# # # Позиция Андрея - это номер в массиве + 1
# # andrey_position = position + 1

# # print(andrey_position)

# #6
# # import random

# # def simulate_coin_toss():
# #     count = 0
# #     consecutive_heads = 0
# #     consecutive_tails = 0

# #     while consecutive_heads < 3 and consecutive_tails < 3:
# #         toss = random.choice(['O', 'P'])
# #         print(toss, end=' ')
# #         count += 1
        
# #         if toss == 'O':
# #             consecutive_heads += 1
# #             consecutive_tails = 0
# #         else:
# #             consecutive_tails += 1
# #             consecutive_heads = 0

# #     print(f"\nПопыток: {count}")

# # simulate_coin_toss()

# #7
# # def luhn_check(card_number):
# #     # Преобразуем номер карты в список цифр
# #     digits = [int(d) for d in str(card_number)]
# #     # Удвоим каждую вторую цифру, начиная с последней
# #     for i in range(len(digits) - 2, -1, -2):
# #         digits[i] *= 2
# #         if digits[i] > 9:
# #             digits[i] -= 9
# #     # Суммируем все цифры
# #     total_sum = sum(digits)
# #     # Проверяем, делится ли сумма на 10
# #     return total_sum % 10 == 0

# # # Входные данные
# # card_numbers = [
# #     427644003366511,
# #     427644003366512,
# #     427613366513
# # ]

# # # Проверяем номера карт
# # for number in card_numbers:
# #     if luhn_check(number):
# #         print(f"{number}: Корректный номер")
# #     else:
#         # print(f"{number}: Некорректный номер")

# #8
# # Входные данные
# #n = 3
# #words = ["word", "localization", "internationalization"]

# ## Функция для преобразования слова в аббревиатуру
# #def abbreviate(word):
# #    if len(word) > 10:
# #        return f"{word[0]}{len(word) - 2}{word[-1]}"
# #    return word

# ## Применяем функцию к каждому слову и выводим результат
# #result = [abbreviate(word) for word in words]
# #print(res
# def luhn_algorithm(card_number):
#     def digits_of(n):
#         return [int(d) for d in str(n)]
    
#     digits = digits_of(card_number)
#     odd_digits = digits[-1::-2]
#     even_digits = digits[-2::-2]
    
#     checksum = sum(odd_digits)
    
#     for d in even_digits:
#         checksum += sum(digits_of(d * 2))
    
#     return checksum % 10 == 0

# # Входные данные
# card_numbers = [
#     "4276440013361511",
#     "4276440013361512",
#     "42761336512"
# ]

# # Вывод результатов
# for number in card_numbers:
#     is_valid = luhn_algorithm(number)
#     print(f"{number}: {'Корректный номер' if is_valid else 'Некорректный номер'}")


############################################################
def luhn_check(card_number):
    card_number = [int(digit) for digit in str(card_number)]
    checksum = 0

    # Умножаем четные цифры на 2 и суммируем
    for i in range(-2, -len(card_number)-1, -2):
        doubled = card_number[i] * 2
        checksum += doubled if doubled <= 9 else doubled - 9

    # Суммируем нечетные цифры
    checksum += sum(card_number[-1::-2])

    # Проверяем, кратна ли сумма 10
    return checksum % 10 == 0

# Тестирование
card_numbers = [4276440013361511, 4276440013361512, 427613336512]
results = []

for number in card_numbers:
    if luhn_check(number):
        print(f"{number} Корректный номер")
    else:
        print(f"{number} Некорректный номер")
