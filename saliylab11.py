#1
dictionary = {".,?!:":'1',
              "abc":'2',
              "def":'3',
              "ghi":'4',
              "jkl":'5',
              "mno":'6',
              "pqrs":'7',
              "tuv":'8',
              "wxyz":'9',
              " ":'0',}
# Hello, World!
word = "Hello, World!" #str(input("Введите сообщение:\n"))

for i in word.lower():
    for j in dictionary.keys():
        if i in j:
            n = j.find(i)
            print(dictionary[j]*(n+1),end="")


            
