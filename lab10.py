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

#2

def find_word(word_to_find, file):
    try:
        with open(file, 'r') as file:
            sodergh = file.read()
            return word in sodergh
    except FileNotFoundError:
        return False




word = "Academy"
file5 = 'file5.txt'
file6 = 'file6.txt'
op1 = find_word(word,file5)
op2 = find_word(word,file6)

if op1:
    print(f'Слово "{word}" найдено в файле {file5}.')
elif op2:
    print(f'Слово "{word}" найдено в файле {file6}.')
else:
    print(f'Слово "{word}" не найдено ни в одном из файлов.')
