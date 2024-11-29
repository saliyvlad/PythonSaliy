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


            
