# 1
# # Чтение количества людей в экипаже
# n = int(input("Введите количество людей в экипаже: "))

# # Списки для хранения членов экипажа
# women_and_children = []
# men = []

# # Считывание данных о каждом члене экипажа
# for _ in range(n):
#     line = input().strip()
#     name, status = line.split()
    
#     if status in ['woman', 'child']:
#         women_and_children.append(name)
#     elif status == 'man':
#         men.append(name)

# # Вывод эвакуации
# evacuation_order = women_and_children + men
# for member in evacuation_order:
#     print(member)

# 2
# def is_dialog_valid(messages):
#     balance = 0  # Счетчик, который будет отслеживать количество вопросов и ответов

#     for message in messages:
#         if message == 'Q':
#             balance += 1  # Увеличиваем счетчик на 1 для вопроса клиента
#         elif message == 'A':
#             balance -= 1  # Уменьшаем счетчик на 1 для ответа специалиста
#         # Если в любой момент количество ответов становится больше количества вопросов, это ошибка
#         if balance < 0:
#             return False

#     # В конце балансы должны быть равными, чтобы все вопросы имели ответы
#     return balance == 0

# # Чтение количества сообщений
# n = int(input("Введите количество сообщений: "))
# messages = input("Введите последовательность сообщений (Q для вопроса, A для ответа): ").strip()

# # Проверка является ли диалог корректным
# if is_dialog_valid(messages):
#     print("+")
# else:
#     print("-")

# 3
# import PySimpleGUI as sg

# c_image = [[sg.Image("bio.png")]]
# c_input = [[sg.Text("Введите количество бактерий:", font="Arial 20"), sg.Input(font="Arial 20", size=(5, 0), key="micro")],
#            [sg.Text("Количество секунд:", font="Arial 20"), sg.Input(font="Arial 20", size=(5, 0), key="count")],
#            [sg.Text("Результат:", font="Arial 20"), sg.Input(font="Arial 20", readonly=True, size=(10, 0), key="res")],
#            [sg.Button("Рассчитать", font="Arial 20")]]

# layout = [
#     [sg.Column(c_image), sg.VSeperator(), sg.Column(c_input, justification='right')]
# ]

# window = sg.Window("Калькулятор бактерий", layout)

# while True:
#     event, value = window.read()

#     if event == sg.WIN_CLOSED:
#         break

#     if event == "Рассчитать":
#         try:
#             # Получаем входные данные
#             micro = int(value["micro"])  # Количество бактерий изначально
#             count = int(value["count"])   # Количество секунд для расчета
            
#             k = 2  # Задаем количество делений за секунду (например, 2)
#             b = 3  # Задаем количество бактерий, материализующихся каждую секунду (например, 3)

#             # Начинаем расчет
#             # Количество бактерий на N-й секунде
#             res = (micro * (k ** count)) + (b * ((k ** count) - 1) // (k - 1))

#             # Обновляем результат в поле
#             window["res"].update(res)

#         except ValueError:
#             sg.popup_error("Пожалуйста, введите корректные целые числа.")

# window.close()

# # 4
# import PySimpleGUI as sg

# def to_binary(n, bits=8):
#     """Преобразует целое число в двоичное представление с заданным количеством бит."""
#     if n < 0:
#         n = (1 << bits) + n
#     return format(n, '0{}b'.format(bits))

# def to_complement(n):
#     """Возвращает дополнительный код для данного числа."""
#     if n >= 0:
#         return to_binary(n)
#     else:
#         # Дополнительный код для отрицательного числа
#         return to_binary((1 << 8) + n)

# def to_reverse(n):
#     """Возвращает обратный код для данного числа."""
#     if n >= 0:
#         return to_binary(n)
#     else:
#         # Инвертируем биты для обратного кода
#         return format((1 << 8) + n ^ 0xFF, '08b')

# layout = [
#     [sg.Text("Введите число от -128 до 127:", font="Arial 14"), sg.InputText(key="number")],
#     [sg.Button("Преобразовать", font="Arial 14")],
#     [sg.Text("Прямой код:", font="Arial 14"), sg.Text("", key="direct_code")],
#     [sg.Text("Обратный код:", font="Arial 14"), sg.Text("", key="reverse_code")],
#     [sg.Text("Дополнительный код:", font="Arial 14"), sg.Text("", key="complement_code")],
#     [sg.Button("Выход", font="Arial 14")]
# ]

# window = sg.Window("Кодирование чисел", layout)

# while True:
#     event, values = window.read()
    
#     if event in (sg.WIN_CLOSED, "Выход"):
#         break

#     if event == "Преобразовать":
#         try:
#             number = int(values["number"])
#             if number < -128 or number > 127:
#                 sg.popup_error("Число должно быть в диапазоне от -128 до 127.")
#                 continue
            
#             direct_code = to_binary(number)
#             complement_code = to_complement(number)
#             reverse_code = to_reverse(number)
            
#             window["direct_code"].update(direct_code)
#             window["complement_code"].update(complement_code)
#             window["reverse_code"].update(reverse_code)
        
#         except ValueError:
#             sg.popup_error("Пожалуйста, введите корректное целое число.")

# window.close()


def binary_to_reverse_and_twos_complement(binary_str):
    # Преобразуем двоичную строку в список символов
    binary_list = list(binary_str)
    
    # Обратный код (инверсия битов)
    reverse_code = ''.join('1' if bit == '0' else '0' for bit in binary_list)
    
    # Дополнительный код (обратный код + 1)
    # Преобразуем обратный код в десятичное число, добавляем 1 и возвращаем в двоичный вид
    twos_complement = bin(int(reverse_code, 2) + 1)[2:]

    return reverse_code, twos_complement

# Пример использования
binary_input = "1010"
reverse_code, twos_complement = binary_to_reverse_and_twos_complement(binary_input)

print(f"Двоичное число: {binary_input}")
print(f"Обратный код: {reverse_code}")
print(f"Дополнительный код: {twos_complement}")
