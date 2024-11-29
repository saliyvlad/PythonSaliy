# #1
# dictionary = {".,?!:":'1',
#               "abc":'2',
#               "def":'3',
#               "ghi":'4',
#               "jkl":'5',
#               "mno":'6',
#               "pqrs":'7',
#               "tuv":'8',
#               "wxyz":'9',
#               " ":'0',}
# # Hello, World!
# word = "Hello, World!" #str(input("Введите сообщение:\n"))

# for i in word.lower():
#     for j in dictionary.keys():
#         if i in j:
#             n = j.find(i)
#             print(dictionary[j]*(n+1),end="")

# #2
# dictionary = {"aeilnorstu":'1',
#               "dg":'2',
#               "bcmp":'3',
#               "fhvwy":'4',
#               "k":'5',
#               "jx":'8',
#               "qz":'10',}
# word = "helloworld" #str(input("Введите сообщение:\n"))
# count = 0
# for i in word.lower():
#     for j,k in dictionary.items():
#         if i in j:
#             count += int(k)
# print(count,end="")

# #3
# emails = {'gryffindor.com': ['andrei_serov', 'alexander_pushkin', 'elena_belova', 'k_stepanov'],
# 'hufflepuff.com': ['alena.semyonova', 'ivan.polekhin', 'marina_abrabova'],
# 'hogwarts.com': ['sergei.zharkov', 'julia_lyubimova', 'vitaliy.smirnoff'],
# 'slytherin.com': ['ekaterina_ivanova', 'glebova_nastya'],
# 'ravenclaw.com': ['john.doe', 'mark.zuckerberg', 'helen_hunt']}
# for i,j in emails.items():
#     for k in j:
#         print(k,"@", i,sep="")

# 4
# import PySimpleGUI as mp
# import random

# # Определяем тему оформления
# mp.theme('LightBlue')

# # Задаем макет интерфейса
# layout = [
#     [mp.Text('Введите нижнюю границу:'), mp.InputText(key='lower_bound')],
#     [mp.Text('Введите верхнюю границу:'), mp.InputText(key='upper_bound')],
#     [mp.Text('Случайное число:'), mp.InputText(key='random_number', disabled=True)],
#     [mp.Button('Сгенерировать')],
#     [mp.Image(filename='C:/Users/saliy_03jey6u/Desktop/3de9c7cb6baa455bbee4e4f64b4cbe10.jpg')]  # Укажите путь к вашему изображению
# ]

# # Создаем окно
# window = mp.Window('Генератор случайных чисел', layout)

# # Основной цикл программы
# while True:
#     event, values = window.read()
    
#     if event == mp.WINDOW_CLOSED:
#         break
#     elif event == 'Сгенерировать':
#         try:
#             lower_bound = int(values['lower_bound'])
#             upper_bound = int(values['upper_bound'])
#             if lower_bound < upper_bound:
#                 random_number = random.randint(lower_bound, upper_bound)
#                 window['random_number'].update(random_number)
#             else:
#                 mp.popup_error('Нижняя граница должна быть меньше верхней границы!')
#         except ValueError:
#             mp.popup_error('Пожалуйста, введите целые числа!')

# # Закрываем окно
# window.close()
            
