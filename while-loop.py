# while(toki)
# Takrorlanish operatorlari
# 1. for loop
# 2. while(toki) loop
# 1 dan 10 gacha sonlarni sanash
# for son in range(1, 10):
#     print(son)

# son = 1
# while son < 10:
#     print(son)
#     son += 1

# Infinity loop - cheksiz sikl / abadiy sikl
# while True:
#     print("Infinity loop")

# while va input()
# print("Kiritilgan sonning kvadratini qaytaruvchi dastur.")
# savol = "Istalgan son kiriting "
# savol += "(dasturni to'xtatish uchun 'exit' deb yozing): "
# qiymat = ""
# while qiymat != 'exit':
#     qiymat = input(savol)
#     if qiymat != 'exit':
#         print(float(qiymat) ** 2)
#     else:
#         print("Dastur ishlashdan to'xtadi")


# print("Kiritilgan sonning kvadratini qaytaruvchi dastur.")
# savol = "Istalgan son kiriting "
# savol += "(dasturni to'xtatish uchun 'exit' deb yozing): "
# ishora = True
# while ishora:
#     qiymat = input(savol)
#     if qiymat == 'exit':
#         ishora = False
#     else:
#         print(float(qiymat)**2)

# break(sindirish) operator
# sonlar = list(range(1,11))
# for son in sonlar: 
#     if son == 5: # son 5 ga teng bo'lsa sikl to'xtaydi
#         break

#     print(f"{son} ning kvadrati {son**2} ga teng")

# print("Kiritilgan sonning kvadratini qaytaruvchi dastur.")
# savol = "Istalgan son kiriting "
# savol += "(dasturni to'xtatish uchun 'exit' deb yozing): "

# while True: # abadiy tsikl
#     qiymat = input(savol)
#     if qiymat == 'exit':
#         break # tsiklni to'xtatish
#     else:
#         print(float(qiymat)**2)

# continue(davom qilish) operator
# sonlar = list(range(1,11))
# for son in sonlar:
#     if son == 5: # son 5 ga teng bo'lsa tiskl boshiga qaytadi
#         continue
#     print(f"{son} ning kvadrati {son**2} ga teng")

# son = 0
# while son<10:
#     son += 1
#     if son%2!=0:
#         continue
#     else:
#         print(son)

# Abadiy sikl tuzog'i
# infinite loop
# son = 0
# while son<10:
#     son += 1
#     if son%2!=0:
#         continue
#     else:
#         print(son)

# son = 1
# while son < 100: 
#     son += 1
#     if son%2!=0:
#         continue
#     else:
#         print(son)


# while True:
#     yosh = input("Yoshingizni kiriting: ")
#     yosh += input("Dasturni to'xtatishni xohlasangiz 'quit' yoki 'exit' deb yozing") 
#     if yosh == 'exit' or yosh == 'quit':
#         break
#     yosh = int(yosh)
#     if yosh < 7:
#         print("2000 so'm")
#     elif yosh <= 18:
#         print("3000 so'm")
#     elif yosh <= 65:
#         print("10000 so'm")
#     else:
#         print("bepul")

