##1
#def remove_povtor_words(text):
    #words = text.split()  # Разделяем текст на слова
    #result = []           # Список для хранения уникальных слов
    #pred_word = None  # Переменная для хранения предыдущего слова

    #for word in words:
        ## Проверяем, является ли текущее слово повтором предыдущего
        #if word != pred_word:
            #result.append(word)  
        #pred_word = word     

    ## Объединяем слова обратно в строку
    #return ' '.join(result)


#text1 = "Довольно распространённая ошибка ошибка это лишний повтор повтор слова слова Смешно не не правда ли Не нужно портить хор хоровод"
#output_text = remove_povtor_words(text1)
#print(output_text)


##2
#def perever(textt):
    ## Разделяем фразу на слова
    #words = textt.split()  
    
    ## Проверяем количество слов
    #if len(words) != 2:
        #return "Ошибка! Некорректное количество слов"
    
    ## Меняем местами слова
    #return f"{words[1]} {words[0]}"

## Входные данные
#inputt = ["фразу перевернуть","тайна раскрыта","привет","привет всем присутствующим"]

## Обрабатываем каждую фразу
#for php in inputt:
    #result = perever(php)
    #print(result)
    
##3
#def edit_text(sob1):
    ## Если сообщение пустое или состоит из одного символа, возвращаем его без изменений
    #if len(sob1) <= 1:
        #return sob1
    
    ## Используем метод join для вставки точки между символами
    #return '.'.join(sob1)

## Входные данные
#textt = ["Python", "h","", "hello world"]

## Обрабатываем каждое сообщение
#for sob1 in textt:
    #result = edit_text(sob1)
    #print(result)

# #4
# def edit_text(sob1):
#     cp1 = "не плохой"
#     cp2 = "не плоха"
#     if cp1 in (sob1):
#         return sob1.replace("не плохой", "хороший")
#     elif cp2 in sob1:
#         return sob1.replace("не плоха", "хороша")
    
# textt = ["Фильм не плохой.", "Книга плохая!", "Еда не плоха, но могла бы быть лучше."]

# print(textt)
# for sob1 in textt:
#     result = edit_text(sob1)
#     print(result)

#5
##gl="аеёиоуэюя"
##i = input("Type text here:\n")
##i=i.split("/")
##counter=0
##m=[]
##for k in i:
##    for n in range(len(k)):
##        if k[n].lower() in gl:
##            counter+=1
##    m.append(counter)
##    counter=0
##if m==[5,7,5]: print("Хокку")
##else:
##    if len(i)!=3:
##        print("Не хокку((( должно быть 3 строки")
##    else:
##        print("Не хокку(((")

#6
# msg = input("введите сообщение для расшифровки:\n ")
# ans = msg[0:-1:2]+msg[1:-1:2][::-1]
# if (msg[-1]=="#") and (msg[:-2].isalpha()):
#    print("расшифрованное сообщение:", ans)
# else:
#    print("Ошибка, отсуствует символ #")

#7
##import random as r
##
##options=[]
##
##upLetters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
##lowLetters=upLetters.lower()
##digits="0123456789"
##SpS="!@#$%^&*_-+="
##length = int(input("input length:\n"))
##
##options.append(input("capital needed? y/n:\n"))
##options.append(input("lower needed? y/n:\n"))
##options.append(input("digits needed? y/n:\n"))
##options.append(input("special symbols needed? y/n:\n"))
##
##pas =""
##
##for x in range(len(options)):
##    if options[x].lower() in ["y","yes"]:
##        options[x]=1
##    else:
##        options[x]=0
##total= upLetters*options[0]+lowLetters*options[1]+digits*options[2]+SpS*options[3]
##for i in range(length):
##    pas += r.choice(total)
##print(pas)
