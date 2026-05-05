# lambda function - anonymous(maxfiy, noma'lum) funksiya
# syntax: 
# lambda argument: expression(ifoda)
# x = lambda a : a % 5
# print(x(12)) # 2

# import math as m
# uzunlik = lambda pi, r : 2 * pi * r
# print(uzunlik(m.pi, 5)) 

# product = lambda x, y : x ** y
# print(product(3, 2))
# print(product(5, 3))

# def daraja(n):
#     return lambda x : x ** n

# kvadrat = daraja(2)
# print(kvadrat(5)) # 25
# kub = daraja(3)
# print(kub(7)) # 343

# map() va filter()
# numbers = list(map(int, input().split()))
sonlar = [5, 8, -8, 0, 13]
# sonlar2 = []
# for son in sonlar:
#         sonlar2.append(son * 2)

# print(sonlar2)

# map(lambda x : x * 2, sonlar) 
print(list(map(lambda x : x * 2, sonlar))) # [10, 16, -16, 0, 26]

