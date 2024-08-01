"""
komentariya
"""
# komentariya

# print("tug'ilgan yilingizni aniqlang yoshingizni kiriting")
# a = int(input())
# b = 2024
# c = b - a
# print(f"Siz taxminan {c} yilda tug'ilgansiz shunyadmi?")


# username = input("dastur tog'ri javob berdimi y | n: ")
# if username == "y":
#     print("demak dasturimiz ish berdi")
# elif username == "n":
#     print("unday bolsa dastur kamchiliklari haqida bizga habar bering ")
# else:
#     print("siz noto'g'ri buyruqni kiritdingiz!")




                # WHILE TSIKLI MISOLLARI

# n = 423
# summa = 0
# print(summa)
# while n > 0:
#       x = n % 10
#       summa = summa + x
#       n = n //10
#       print(summa)
# print(summa) # 9

# a = 423
# b = 10
# qoldiq = a % b
# print(qoldiq)

# n = int(input())
# flag = True
# i = 5
# while flag:
#     if n % i == 0:
#         flag = False
#         print(i)
#     elif i > n // 2:
#         print(n)
#         flag = False
#     i += 1
# #    print(i)







# text = 'salom duyo qalesan bolyaptimi ishlar'
# print(len(text))    # 36
# print(text[:])      # salom duyo qalesan bolyaptimi ishlar
# print(text[19:])    # bolyaptimi ishlar (19- elementdan oxirigacha)
# print(text[:2])     # sa (2-chi elementgacha)
# print(text[:-2])    # salom duyo qalesan bolyaptimi ishl
# print(text[-2:])    # ar (oxiridan 2-chi xarifdan uyog'iga)
# print(text[2:15])   # lom duyo qale (2-dan 15-gacha bolgan element)
# print(text[::5])    # s  sotir (xar 5- element)





                # FOR TSIKLI MISOLLARI


# a = 'qwerty'

# for i in a:
#     print(i)

# a = ['olma', 'banan', 'gilos']

# for i in a:
#     print(i)

# a = ['olma', 'banan', 'gilos']

# for index, i in enumerate(a):
#     print(f"{index}: {i}")



# for i in range(100, -10, -10):
#        print(i)

        # bu kodda raqamlar bilam ishlash 100 dan 0 gacha bolgan 
        # raqamlarni 10 qadamdan yurib ekrancga chiqaradi
        # 100 (start) - boshlang'ich qiymat (ixtiyoriy, standart qiymati 0)
        # -10 (stop) - to'xtash qiymati (ushbu qiymatning o'zi generatsiya qilinmaydi)
        # -10 (step) - qadam (ixtiyoriy, standart qiymati 1) 
        # qadam (step) shart yozish vaqtida yozilmagan bolsa kompiyuter 
        # buni avtomatik ravishda ijobiyga (+) tomonga hisoblaydi 
        # minusga hisoblash uchun qadam (step) yozilishi kerak



# line = ""
# for i in range(5):
#     line = ""  
#     for j in range(5):
#         line += "*"
#     print(line)

#     # for tsikili ichida tsikil bu jarayoni tashqi tsikil boshlaydi 
#     # va ichki tsikil davom etiradi toki ichki tsikil ozini ishin tugatmaguncha 
#     # tashqi tsikl boshlagan ishini tugata olmaydi yani birinchi urinishdayoq kutadi 
#     # toki ichki tsikl qancha aylanish olgan bolsa shuni bitirmaguncha 






