#1
alph1 = ".,?!:"
alph2 = "abc"
alph3 = "def"
alph4 = "ghi"
alph5 = "jkl"
alph6 = "mno"
alph7 = "pqrs"
alph8 = "tuv"
alph9 = "wxyz"
alph0 = " "

dictionary = {alph1:'1',
              alph2:'2',
              alph3:'3',
              alph4:'4',
              alph5:'5',
              alph6:'6',
              alph7:'7',
              alph8:'8',
              alph9:'9',
              alph0:'0',}
# Hello, World!
word = "Hello, World!" #str(input("Введите сообщение:\n"))

for i in word.lower():
    for j in dictionary.keys():
        if i in j:
            n = j.find(i)
            print(dictionary[j]*(n+1),end="")


            
