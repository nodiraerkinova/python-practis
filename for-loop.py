# # Takrorlanish operatorlari
# # loop - sikl
# # 1. for loop
# # 2. while loop
# students = ['Elbek', 'Maftuna', 'Gulomjon', 'Maxliyo', 'Dilbek']
# # hard coding
# # print(students[0])
# # print(students[1])
# # print(students[2])
# # print(students[3])
# # print(students[4])
# for student in students:
#     print(student)
    
# for guest in students:
#     print(f"Hurmatli {guest}, sizni intervivga taklif qilmoqchiman.")
#     print("Hurmat bilan, Al-Xorazmiy vorislari loyihasi.") 

# # Sonlar ro'yxati uchun for loop
# even_number = list(range(2, 50, 2)) # 2 dan 50 gacha bo'lgan juft sonlar ro'yxati
# for number in even_number:
#     print(number)

# print("Dastur tugadi.")

# # 1 ning kvadrati 1 ga teng 
# # 2 ning kvadrati 4 ga teng
# sonlar = list(range(1, 11)) # 1 dan 10 gacha bo'lgan sonlar ro'yxati
# for son in sonlar:
#     print(f"{son} ning kvadrati {son ** 2} ga teng.")

# for son in range(1, 11):
#     print(son) 

# s = 0
# numbers = [12, 5, 18, 25, 23]    
# # print(sum(numbers))
# for number in numbers:
#     s += number # s = s + number
# print(s) 

# # 1 dan 50 gacha bo'lgan toq sonlar yig'indisi
# summa = 0
# for son in range(1, 50, 2):
#     summa += son
# print(summa) 

# numbers = [12, 5, 18, 25, 23, 88] 
# # o'rta arifmetik = s / length
# s = 0
# for number in numbers:
#     s += number

# d = s / len(numbers) 
# print(d)   

# 1 dan 20 gacha bo'lgan juft sonlarni o'rta arifmetigini toping
# s = 0
# for number in range(1, 21, 2):
#     s += number

# nums = list(range(1, 21, 2))
# average_value = s / len(nums)
# print(average_value)

# n! = 1 * 2 * 3 * ... * (n - 1) * n
# k = 1
# for son in range(1, 20):
#     k *= son 

# print(k)

# # o'rta geometrik = s / length
# import math
# numbers = [12, 5, 18, 25, 23, 88] 
# l = len(numbers)
# k = 1
# for number in numbers:
#     k *= number

# a = math.pow(k, 1 / l)
# print(a) 

# s = 0
# k = 1
# for number in range(1, 21):
#     if number % 2 == 0:
#         k *= number
#     else:
#         s += number

# y = k / s
# print(y)

# s = 0
# counter = 0
# numbers = [7, 97, -58, 90]
# for number in numbers:
#     if number % 2 == 0:
#         s += number
#         counter += 1

# print(s / counter) 
# s = 0
# numbers = [97, 97, -92, 14, 22]
# for number in numbers:
#     if number % 2 == 0 or number % 3 == 0 or number % 5 == 0:
#         s += number 
# print(s) 

# s = 0
# c = 0
# numbers = [76, 12, 51, 50, 98]
# for number in numbers:
#     if number % 2 == 1: 
#         s += number 
#         c += 1
# print(s / c)

# 122
# s = 0
# a = 0
# numbers = [44, 59, -75, 73]
# for number in numbers:
#     s += number ** 2
#     a += number
# c = a / len(numbers)
# print(s , c) 

# 115
# M = int(input("son kiriting: "))
# numbers = [85, 15, 57, 68, 18, 67, 7, 45, 69, 21, 1, 5, 98, 34]
# s = 0
# for number in numbers:
#     if M > number:
#         s += number ** 2
# print(s)

# 114
# import math
# s = 1
# numbers = [44, 34, 42, 83, 43, 64]
# for number in numbers:
#     if number % 2 == 0 or number % 5 == 0:
#        s *= number
# a = math.sin(s)
# print(a) 

# import math
# numbers = [7, 24, -5, 23, 99, -3, 24, 51]
# s = 0
# for number in numbers:
#     s += number

# length = len(numbers)
# average_value = s / length
# log_value = math.log(average_value)
# print(average_value)

# for index in range(0, length):
#     if numbers[index] < 0:
#      numbers[index] = log_value

# print(numbers)

# 127
# numbers = [46, 23, -52, 34, 6, -18, 52]
# a = min(numbers)
# for index in range(0, len(numbers)):
#      if numbers[index] < 0:
#           numbers[index] = a ** 2

# print(numbers)

# 104
# numbers = [74, 0, 1, 33]
# m = min(numbers)

# for x in range(len(numbers)):
#     if numbers[x] == m:
#         numbers[x], numbers[-1] = numbers[-1], numbers[x]
      
# print(*numbers) 

# # 10
# a = [7, 11, 83, 18, 31]
# m = int(input())
# k = int(input())
# s = 1
# for x in a:
#     if x == k or x == m:
#         s *= x

# print(s) 

# numbers = [29, 50, -14, 4, 27, -56]
# k = int(input())
# max_value = max(numbers)
# max_index = numbers.index(max_value)
# k_index = k - 1
# numbers[max_index] = numbers[k_index]
# numbers[k - 1] = max_value

# print(numbers) 
