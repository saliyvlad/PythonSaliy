#1
days = int(input("Enter days: "))
hours = int(input("Enter hours: "))
minutes = int(input("Enter minutes: "))
seconds = int(input("Enter seconds: "))

total = seconds
total += minutes * 60
total += hours * 60 * 60
total += days * 24 * 60 * 60
print("Total:", total, "seconds")

#2
N = int(input("Enter a number (N): "))
K = int(input("Enter a number (K): "))

print("The last K digits on N are:", N % (pow(10, K)))

#3
num = int(input("Enter a number: "))

sum = 0
for digit in str(num):
    sum += int(digit)

print("The sum of the digits is:", sum)

#4
from random import randint

playing = True

while playing:
    safe_choice = randint(1, 2)

    # Вывести вступление
    print('''Вы находитесь в землях, заселенных драконами. Перед собой вы
видите две пещеры.
В одной из них — дружелюбный дракон, который готов поделиться с
вами своими сокровищами.
Во второй — жадный и голодный дракон, который мигом вас съест.
В какую пещеру вы войдете? (нажмите клавишу 1 или 2)''')
    choice = int(input("> "))
    
    while choice != 1 and choice != 2:
        print("В какую пещеру вы войдете? (нажмите клавишу 1 или 2)")
        choice = input("> ")

    print('''Вы приближаетесь к пещере...
Ее темнота заставляет вас дрожать от страха...
Большой дракон выпрыгивает перед вами! Он раскрывает свою
пасть и...''')
    if choice == safe_choice:
        print("...делится с вами своими сокровищами!")
    else: 
        print("...моментально вас съедает!\n")

    print("Хотите ли вы сыграть снова? (да, нет)")
    playing = input("> ").lower() == "да"

#5
a = int(input("Введите длину стороны a: "))
b = int(input("Введите длину стороны b: "))
c = int(input("Введите длину стороны c: "))

print("Этот треугольник...")
if (a == b and b == c):
    print("Равносторонний")
elif (a == b or b == c or c == a):
    print("Равнобедренный")
else:
    print("Разносторонний")
    
#6
retry = True
while retry:
    retry = False
    
    month = input("Введите название месяца: ")
    match month.lower():
        case "январь":
            print("31")
        case "февраль":
            print("28 (29)")
        case "март":
            print("31")
        case "апрель":
            print("30")
        case "май":
            print("31")
        case "июнь":
            print("30")
        case "июль":
            print("31")
        case "август":
            print("31")
        case "сентябрь":
            print("30")
        case "октябрь":
            print("31")
        case "ноябрь":
            print("30")
        case "декарь":
            print("31")
        case _:
            retry = True
            print("Нет месяца с таким названием")

#7
num = input("Введите номерной знак: ")

# Old AAA000
# New 0000AAA

is_correct = False

if len(num) == 6:
    is_old = num[0:3].isupper() and num[-3:].isdigit()
    if is_old:
        is_correct = True
        print("Старый формат")
elif len(num) == 7:
    is_new = num[0:4].isdigit() and num[-3:].isupper()
    if is_new:
        is_correct = True
        print("Новый формат")

if not is_correct:
    print("Не соответствует формату")
