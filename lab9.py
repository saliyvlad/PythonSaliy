# 1
# def f(x):
#     return x ** 2

# def trapezoidal_integration(a, b, N):
#     h = (b - a) / N
#     integral = (f(a) + f(b)) / 2  # Начальная сумма
#     for i in range(1, N):
#         integral += f(a + i * h)  # Суммируем значения f(x)
#     integral *= h  # Умножаем на шаг h
#     return integral

# a = 0  
# b = 1  

# # Вычисляем интегралы для N = 10, 100, 1000
# for N in [10, 100, 1000]:
#     result = trapezoidal_integration(a, b, N)
#     print(f"Значение интеграла для N = {N}: {result}")




# 2
# import random

# def generate_magic_square(n):
#     # Создаем пустой n x n квадрат
#     magic_square = [[0] * n for _ in range(n)]
#     # Начальные координаты для 1
#     row, col = 0, n // 2
#     for num in range(1, n * n + 1):
#         magic_square[row][col] = num
#         # Переход к следующей позиции
#         new_row = (row - 1) % n
#         new_col = (col + 1) % n
#         # Если следующая позиция уже занята, перемещаемся вниз
#         if magic_square[new_row][new_col] != 0:
#             row += 1
#         else:
#             row, col = new_row, new_col

#     return magic_square
# def shuffle_magic_square(square):
#     # Получаем все элементы в одном списке
#     flat_list = [num for row in square for num in row]
#     # Перемешиваем элементы
#     random.shuffle(flat_list)
#     # Заполняем магический квадрат перемешанными элементами
#     n = len(square)
#     for i in range(n):
#         for j in range(n):
#             square[i][j] = flat_list[i * n + j]
# # Размер магического квадрата (должен быть нечетным)
# n = 3
# magic_square = generate_magic_square(n)

# # Перемешиваем его
# shuffle_magic_square(magic_square)

# # Вывод результата
# for row in magic_square:
#     print(*row)    

# 3



# # Функция для вычисления расстояния
# def distance(coord1, coord2):
#     return ((coord1[0] - coord2[0]) ** 2 + (coord1[1] - coord2[1]) ** 2) ** 0.5

# # Ввод количества сокровищ
# n = int(input("Введите количество сокровищ: "))

# # Ввод координат сокровищ
# treasure_map = []
# for i in range(n):
#     coords = input(f"Введите координаты сокровища {i + 1} (x, y): ")
#     x, y = map(int, coords.split(' '))
#     treasure_map.append((x, y))

# # Ввод координат Александра
# sasha_coords = input("Введите координаты Александра (x, y): ")
# sasha_x, sasha_y = map(int, sasha_coords.split(' '))
# sasha_coordinates = (sasha_x, sasha_y)

# # Поиск ближайшего сокровища
# closest_treasure = None
# min_distance = float('inf')

# for treasure in treasure_map:
#     dist = distance(sasha_coordinates, treasure)
#     if dist < min_distance:
#         min_distance = dist
#         closest_treasure = treasure

# # Вывод результата
# print("Координаты ближайшего сокровища:", closest_treasure)

# #4
# menu = [
# ["Пицца Маргарита", ["мука", "томаты", "сыр", "базилик"], 10],
# ["Салат Цезарь", ["салат", "курица", "сыр", "сухарики"], 8],
# ["Суп Томатный", ["томаты", "лук", "морковь", "картофель"], 6]
# ]
# task = int(input("Введите 1 если хотите увидеть меню\nВведите 2 если хотите начать поиск блюда\nВведите 3 если хотите добавить новое блюдо\nВведите 4 если хотите изменить цену блюда\n"))

# if task == 1:#Вывод меню
#     print("Меню:")
#     for i in range(len(menu)):
#         print(*menu[i])

# elif task == 2:#Поиск блюда
#     search = str(input())
#     for i in range(len(menu)):
#         if menu[i][0] == search:
#             print(*menu[i])

# elif task == 3:#Добавить блюдо
#     name_food = str(input())
#     ingredients_food = str(input().split(" "))
#     cost_food = int(input())
#     menu.append([name_food,ingredients_food,cost_food])
#     print(*menu)

# elif task == 4:#Изменить цену
#     search = str(input())
#     for i in range(len(menu)):
#         if menu[i][0] == search:
#             new_cost = int(input())
#             menu[i][2] = new_cost
#             print(*menu[i])

# #5
# n,m = map(int, input("Введите размер матрицы nXm").split(" "))
# matrix =[]

# for i in range(n):
#     row = input().split()
#     for i in range(len(row)):
#         row[i] = int(row[i])
#     matrix.append(row)
# matrix_t = [[0] * n for _ in range(m)]
# for i in range(i):
#     for j in range(len(matrix[i])):
#         matrix_t[j][i] = matrix[i][j]
# print(*matrix)    
# print(*matrix_t)

# #6
# n = int(input("Введите количество строк и столбцов (n): "))

# matrix = []
# print("Введите элементы матрицы построчно:")
# for i in range(n):
#     stroke = list(map(int, input().split()))
#     matrix.append(stroke)


# for i in range(n):
    
#     matrix[i][i], matrix[i][n - 1 - i] = matrix[i][n - 1 - i], matrix[i][i]


# print("Измененная матрица:")
# for stroke in matrix:
#     print(stroke)

#7

# n, m = map(int, input().split())
# seats = [list(map(int, input().split())) for _ in range(n)]
# k = int(input())

# for i in range(n):
#     count = 0
#     for j in range(m):
#         if seats[i][j] == 0:
#             count += 1
#             if count == k:
#                 print(i + 1)
#                 break
#         else:
#             count = 0
#     else:
#         continue
#     break
# else:
#     print(0)

# #8
# n = int(input("Введите количество строк (n): "))
# m = int(input("Введите количество столбцов (m): "))


# matrix = [[0] * m for _ in range(n)]


# for i in range(n):
#     for j in range(m):
#         if i == 0 or j == 0:
#             matrix[i][j] = 1
#         else:
#             matrix[i][j] = matrix[i-1][j] + matrix[i][j-1]


# for row in matrix:
#     print(" ".join(f"{element:6d}" for element in row))

# #9
# import random

# def initialize_game():
#     field = [['.' for _ in range(4)] for _ in range(4)]
#     ships = 4
#     bomb_position = (random.randint(0, 3), random.randint(0, 3))
    
#     while ships > 0:
#         ship_position = (random.randint(0, 3), random.randint(0, 3))
#         if field[ship_position[0]][ship_position[1]] == '.':
#             field[ship_position[0]][ship_position[1]] = 'S'  # S for Ship
#             ships -= 1

#     return field, bomb_position

# def display_field(field):
#     for row in field:
#         print(' '.join(row))
#     print()

# def make_guess(field, guess, bomb_position):
#     x, y = guess
#     if guess == bomb_position:
#         print("Вы проиграли! Попали на бомбу.")
#         return False
#     elif field[x][y] == 'S':
#         field[x][y] = 'X'  # Hit
#         print("Попали в корабль!")
#     else:
#         print("Промах!")
#     return True

# def play_game():
#     field, bomb_position = initialize_game()
#     attempts = 0
#     while True:
#         display_field(field)
#         guess = (int(input("Введите координату X (0-3): ")), int(input("Введите координату Y (0-3): ")))
#         attempts += 1
#         if not make_guess(field, guess, bomb_position):
#             break
#         if all(cell != 'S' for row in field for cell in row):
#             print(f"Поздравляем! Вы нашли все корабли за {attempts} шагов.")
#             break

# play_game()
