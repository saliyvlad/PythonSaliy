# #1
# in_file = open('file4.txt', 'r', encoding='utf8')
# in_file2 = open('file4.txt', 'r', encoding='utf8')
# maxx = 0
# prizer_ball = 0
# prizer_ball1 = ""
# for i in in_file.readlines():
#     for j in (i[-3]+i[-2]):
#         l = int(str(i[-3]+i[-2]))
#         if maxx < int(l):
#             maxx = int(l)

# for m in in_file2.readlines():
#     for n in (m[-3]+m[-2]):
#         l = int(str(m[-3]+m[-2]))
#         if (l < maxx)and(prizer_ball < int(l)):
#             prizer_ball1 = m
#             prizer_ball = int(l)
# print(prizer_ball1)

# #2
# def find_word(word_to_find, file):
#     try:
#         with open(file, 'r') as file:
#             sodergh = file.read()
#             return word in sodergh
#     except FileNotFoundError:
#         return False
# word = "Academy"
# file5 = 'file5.txt'
# file6 = 'file6.txt'
# op1 = find_word(word,file5)
# op2 = find_word(word,file6)

# if op1:
#     print(f'Слово "{word}" найдено в файле {file5}.')
# elif op2:
#     print(f'Слово "{word}" найдено в файле {file6}.')
# else:
#     print(f'Слово "{word}" не найдено ни в одном из файлов.')



#3
# f = open("file6.txt").readline()
# count_e = 0
# count = 0
# for i in f.split(" "):
#     if "e" in i or "E" in i:
#         count_e += 1
#     count += 1
# print(round(((count_e/count)*100),2))

# #4
# n = int(input("Введите кол-во имен "))
# gen = ""
# num = "1234567890"
# count =0
# l = []
# while gen != "м" and gen != "ж":
#     gen = str(input("Введите пол м или ж "))
# if gen == "м":
#     fl = open("file8.txt", "r", encoding="utf8").readlines()
# elif gen == "ж":
#     fl = open("file7.txt", "r", encoding="utf8").readlines()
# for i in fl:
#     for c in num:
#         i = i.replace(c, "")
#     l.append(i)
#     count +=1
#     if count == n:
#         break
# print(*l)

# #5
# filename = 'newfile.txt'

# with open(filename, 'w') as f:
#     f.write("Первая строка\nВторая строка\nТретья строка\nЧетвертая строка")

# new_line = input("Введите новую строку текста: ")

# with open(filename, 'r') as f:
#     lines = f.readlines()

# lines.insert(len(lines)//2, new_line + '\n')

# with open(filename, 'w') as f:
#     f.writelines(lines)

# print("Новая строка добавлена в файл.")

# #6
# def decrypt_file(input_file):
#     with open(input_file, 'r') as file:
#         encrypted_text = file.read()
#     decrypted_words = [word[::-1] for word in encrypted_text.split()]
#     decrypted_text = ' '.join(decrypted_words)

#     print(decrypted_text)

# def encrypt_file(input_file, output_file):
#     with open(input_file, 'r', encoding="utf8") as file:
#         text = file.read()
#     encrypted_words = [word[::-1] for word in text.split()]
#     encrypted_text = ' '.join(encrypted_words)
    
#     with open(output_file, 'w') as file:
#         file.write(encrypted_text)
        
# encrypt_file('file8.txt', 'encrypted.txt')
# decrypt_file('encrypted.txt')

# #7
# import random

# def create_word_file(filename):
#     words = [
#         'Apple', 'Mountain', 'Sunflower', 'Adventure',
#         'Harmony', 'Galaxy', 'Whisper', 'Journey',
#         'Ocean', 'Dream']
    
#     with open(filename, 'w') as file:
#         for word in words:
#             file.write(word + '\n')

# create_word_file('words.txt')


# def generate_password(word_list, attempts=100):
#     for _ in range(attempts):
#         word1 = random.choice(word_list)
#         word2 = random.choice(word_list)

#         if word1 != word2 and len(word1) >= 3 and len(word2) >= 3:
#             password = word1.capitalize() + word2.capitalize()
#             if 8 <= len(password) <= 10:
#                 return password
#     return "Не удалось сгенерировать подходящий пароль."

# def read_words_from_file(filename):
#     with open(filename, 'r', encoding="utf8") as file:
#         words = [line.strip() for line in file if len(line.strip()) > 0]
#     return words

# word_list = read_words_from_file('words.txt')

# password = generate_password(word_list)
# print("Сгенерированный пароль:", password)

# #8
# n, m = map(int, input("Введите n(Строк) и m(Символов)").split())
# table = [['.' for _ in range(m)] for _ in range(n)]
# for r in range(n):
#     if r % 2 == 0:
#         for c in range(m):
#             table[r][c] = '#'
#     else:
#         if r % 4 == 1:
#             table[r][m - 1] = '#'
#         else:  
#             table[r][0] = '#'
# for row in table:
#     print(''.join(row))