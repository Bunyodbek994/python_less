# Birinchi tushunchalar

# list_1 = [36]
# list_2 = list(1, 4, 6, 9)
list_3 = []
print(*list_3)

# for i in range(11):
#     list_3.append(i)    # .append() bu mavjud masivlarga yana bir masiv qoshadi.
#     print(list_3)
# print(list_3)
# for i in range(10):
#     list_3.pop()  # bu esa mavjud masivlardan birini ochiradi
#     print(list_3)

# list_3 = [1, 2, 3, 4, 5, 6]
# print(list_3.insert(2, 50 ))   # bu (har qaysi masivni suirb) aynan ko'rsatilgan masivga yangi qiymat qoshaddi 
#                                #misol: 2- masivga 50 qiymatini qoshyapti

# print(list_3)


# Ikkinchi tushunchalar

# royxat_1= [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# print(royxat_1[0])      #1

# print(royxat_1[1])      #2

# print(royxat_1[-1])     # 10

# print(royxat_1[-5])     #6

# print(royxat_1[:])      # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# print(royxat_1[:2])     # [1, 2]

# print(royxat_1[len (royxat_1)-2:])      #[9, 10]

# print(royxat_1[2:9])        # [3, 4, 5, 6, 7, 8, 9]

# print(royxat_1[6:-18])      # []

# print(royxat_1[0:len (royxat_1):6])     # [1, 7]

# print(royxat_1[::6])        # [1, 7]



# Set operations in Python

a = {1, 2, 3, 5, 8}

b = {2, 5, 3,13,21}

c = a.copy()        # c = {1, 2, 3, 5, 8}  nusxalaydi

u = a.union(b)      # in = {1, 2, 3, 5, 8, 13, 21}  nusxalaydi va teshirib mavjudlarini birlashtiradi

i = a.intersection(b)        # i = {2, 3, 5} nusxasi borlarni topadi

dl = a.difference(b)        # dl = {8, 1} nusxasi yo'qlardi topadi

dr = b.difference(a)         #dr = {13, 21} nusxasi yo'qlardi topadi

q=a.union(b).difference(a.intersection(b))      # {8, 1, 21, 13} solishtiradi va nusxasi yo'qlardi topadi

print(dl)



# Uchini tushunchalar