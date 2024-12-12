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





# # # 4
# import PySimpleGUI as sg

# c_input = [[sg.Text("Введите число [-127; 128]:", font="Arial 20"), 
#              sg.Input(font="Arial 20", size=(5, 0), key="number", enable_events=True)],
#             [sg.Text("Прямой:", font="Arial 20"), 
#              sg.Input(font="Arial 20", readonly=True, size=(10, 0), key="res")],
#             [sg.Text("Обратный:", font="Arial 20"), 
#              sg.Input(font="Arial 20", readonly=True, size=(10, 0), key="res_inverse")],
#             [sg.Text("Дополнительный:", font="Arial 20"), 
#              sg.Input(font="Arial 20", readonly=True, size=(10, 0), key="res_compliment")],
#             [sg.Button("Рассчитать", font="Arial 20")]]

# layout = [
#     [sg.Column(c_input, justification='right')]
# ]

# window = sg.Window("Калькулятор бинарных чисел", layout)

# while True:
#     event, value = window.read()

#     if event == sg.WIN_CLOSED:
#         break

#     # Input validation
#     if event == "number":
#         try:
#             number = int(value["number"])
#             if number < -127 or number > 128:
#                 window["number"].update(value["number"][:-1])  # Удаляем последний символ
#         except ValueError:
#             if len(value["number"]) == 1 and value["number"][0] == "-":
#                 continue
#             window["number"].update(value["number"][:-1])  # Удаляем последний символ

#     if event == "Рассчитать":
#         if value["number"]:  # Проверяем, что поле не пустое
#             try:
#                 number = int(value["number"])
#                 if number < -127 or number > 128:
#                     sg.popup_error("Число должно быть в диапазоне [-127; 128]")
#                     continue

#                 # Приведение числа к 8-битному представлению
#                 if number >= 0:
#                     # Прямой код для положительных чисел
#                     direct_code = number
#                 else:
#                     # Прямой код для отрицательных чисел
#                     direct_code = (-number & ((1 << 7) - 1)) | (1 << 7)  # Устанавливаем старший бит

#                 # Формируем прямой код
#                 window["res"].update(f"{direct_code:08b}")

#                 # Обратный код
#                 if number >= 0:
#                     inverse_code = direct_code
#                 else:
#                     inverse_code = (~direct_code & ((1 << 8) - 1)) | (1 << 7)  # Инвертируем все биты и устанавливаем старший бит

#                 window["res_inverse"].update(f"{inverse_code:08b}")

#                 # Дополнительный код
#                 if number >= 0:
#                     compliment_code = direct_code
#                 else:
#                     compliment_code = (inverse_code + 1) & ((1 << 8) - 1)  # Прибавляем 1

#                 window["res_compliment"].update(f"{compliment_code:08b}")

#             except ValueError:
#                 sg.popup_error("Пожалуйста, введите корректное число.")

# window.close()
