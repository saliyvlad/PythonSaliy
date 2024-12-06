# # 1
# n = int(input("Введите количество людей в экипаже: "))

# women_and_children = []
# men = []
# cap = []
# for _ in range(n):
#     line = input().strip()
#     name, status = line.split()
    
#     if status in ['w', 'ch']:
#         women_and_children.append(name)
#     elif status == 'm':
#         men.append(name)
#     elif status == 'ca':
#         cap.append(name)
# evacuation_order = women_and_children + men + cap
# print("=================")
# for member in evacuation_order:
#     print(member)

# # # 2
# def is_dialog_valid(messages):
#     balance = 0 

#     for message in messages:
#         if message.lower() == 'q':
#             balance += 1  
#         elif message.lower() == 'a':
#             balance -= 1  
#         if balance < 0:
#             return False

#     return balance == 0

# n = int(input("Введите количество сообщений: "))
# messages = input("Введите последовательность сообщений (Q для вопроса, A для ответа): ").strip()

# if is_dialog_valid(messages):
#     print("+")
# else:
#     print("-")

# #3
# import PySimpleGUI as sg

# c_image = [[sg.Image("bio.png")]]
# c_input = [[sg.Text("Введите количество бактерий:", font="Arial 20"), sg.Input(font="Arial 20", size=(5, 0), key="micro")],
#            [sg.Text("K:", font="Arial 20"), sg.Input(font="Arial 20", size=(10, 0), key="k")],
#            [sg.Text("B:", font="Arial 20"), sg.Input(font="Arial 20", size=(10, 0), key="b")],
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
#             micro = int(value["micro"]) 
#             count = int(value["count"])  
            
#             k = int(value["k"])  
#             b = int(value["b"])
#             res = k*micro*count+b*micro*count

#             window["res"].update(res)

#         except ValueError:
#             sg.popup_error("Пожалуйста, введите корректные целые числа.")
# window.close()

# 4
import PySimpleGUI as sg

def binary_to_reverse(binary_str):
    binary_str = binary_str.zfill(8)
    binary_list = list(binary_str)
    reverse_code = ''.join('1' if bit == '0' or bit == 'b' else '0' for bit in binary_list)
    return int(reverse_code) 

def binary_to_dlc(binary_str):
    binary_str = binary_str.zfill(8)
    binary_list = list(binary_str)
    reverse_code = ''.join('1' if bit == '0' or bit == 'b' else '0' for bit in binary_list)
    dlc = bin(int(reverse_code, 2) + 1)[2:]
    dlc = dlc.zfill(8)[-8:]
    return int(dlc)

layout = [
    [sg.Text("Введите число от -128 до 127:", font="Arial 14"), sg.InputText(key="number")],
    [sg.Button("Преобразовать", font="Arial 14")],
    [sg.Text("Прямой код:", font="Arial 14"), sg.Text("", key="direct_code")],
    [sg.Text("Обратный код:", font="Arial 14"), sg.Text("", key="reverse_code")],
    [sg.Text("Дополнительный код:", font="Arial 14"), sg.Text("", key="dlc_code")],
    [sg.Button("Выход", font="Arial 14")]
]
window = sg.Window("Кодирование чисел", layout)
while True:
    event, values = window.read()
    if event in (sg.WIN_CLOSED, "Выход"):
        break
    if event == "Преобразовать":
        try:
            number = int(values["number"])
            if number < -128 or number > 127:
                sg.popup_error("Число должно быть в диапазоне от -128 до 127.")
                continue
            if number >= 0:
                binary_str = str(bin(number)).zfill(8)
                binary_list = list(binary_str)
                direct_code = binary_list#''.join('0' if bit == '0' or bit == 'b' else '1' for bit in binary_list)
                dlc_code = binary_to_dlc(str(bin(number)))
                reverse_code = binary_to_reverse(str(bin(number)))
            else:
                binary_str = str(bin(number)).zfill(8)
                binary_list = list(binary_str)
                direct_code = binary_to_dlc(str(bin(number)))
                dlc_code = binary_to_dlc(str(bin(number)))
                reverse_code = binary_to_dlc(str(bin(number)))
            window["direct_code"].update(direct_code)
            window["dlc_code"].update(dlc_code)
            window["reverse_code"].update(reverse_code)
        except ValueError:
            sg.popup_error("Пожалуйста, введите корректное целое число.")
window.close()





# def binary_to_reverse_and_twos_complement(binary_str):
#     # Убедимся, что входное двоичное число имеет 8 знаков
#     binary_str = binary_str.zfill(8)
    
#     # Преобразуем двоичную строку в список символов
#     binary_list = list(binary_str)
    
#     # Обратный код (инверсия битов)
#     reverse_code = ''.join('1' if bit == '0' else '0' for bit in binary_list)
    
#     # Дополнительный код (обратный код + 1)
#     # Преобразуем обратный код в десятичное число, добавляем 1 и возвращаем в двоичный вид
#     twos_complement = bin(int(reverse_code, 2) + 1)[2:]

#     # Убедимся, что дополнительный код также имеет 8 знаков
#     twos_complement = twos_complement.zfill(8)[-8:]

#     return reverse_code, twos_complement

# # Пример использования
# print(bin(-127))
# binary_input = '01111111'  # Входное двоичное число
# reverse_code, twos_complement = binary_to_reverse_and_twos_complement(binary_input)

# print(f"Двоичное число: {binary_input.zfill(8)}")
# print(f"Обратный код: {reverse_code}")
# print(f"Дополнительный код: {twos_complement}")
