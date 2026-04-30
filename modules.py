# pythonda modullar
# as operatori
# import math_operations as m
# print(math_operations.addition(7, 8))
# print(math_operations.multiplication(7, 8))
# print(math_operations.find_max(18, -8, 77, 1y, 16))
# print(m.subtraction(7, 5))

# 2.modul ichidan faqatgina  kerakli funksiyani import qilish
from math_operations import addition, subtraction, PI 
print(addition(7, 8))
print(subtraction(7, 5))
print(PI)

# 3. *
from math_operations import *
print(multiplication(4, 7))
print(addition(5, 4))
print(PI)

# 4. python random modul
import random as r
print(r.random()) # 0 dan 1 gacha bo'lgan tasodifiy son
print(r.randint(1, 10)) # 1 dan 10 gacha bo'lgan tasodifiy butun son


ismlar = ["Ali", "Vali", "Guli", "Soli"]
ism = r.choice(ismlar) # ismlar ro'yxatidan tasodifiy ism tanlash
print(ism)
print(r.choice(ism)) # ism ro'yxatidan tasodifiy harf tanlash
