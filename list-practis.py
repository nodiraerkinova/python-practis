# ismlar = ['Abror', 'Maxmur', 'Bobur']
# print(f"Salom {ismlar[0]}, bugun choyxona bormi?\n{ismlar[1]} choyxonaga boramizmi?")

# sonlar = [12, 15, 0, 89, -15,75, 0, 158.89]
# print(sonlar[3] / sonlar[1]) # 89 / 15
# # 0 => -8
# sonlar[2] = -8
# print(sonlar) 

# historical_people = ['Amir Temur', 'Al Xoramiy', 'Julia Sezer']
# modern_people = ['Bell Geyts', 'Ilon Musk', 'Pavel Durov', 'Steve Jobs'] 
# print(f"""Men tarixiy shaxslardan {historical_people[1]} bilan,
# zamonaviy shaxslardan {modern_people[1]} bilan
# suhbat qilishni istar endim""")

frieds = ['mahliyo', 'nodira', 'lobar', 'dilmira', 'zebo']
# frieds.append("yulduz")
# frieds.insert(0, 'maftuna')
# print(frieds)
# element = frieds.pop(1)
# print(element) 
# print(frieds) 

# list.sort()
# frieds.sort() # alifbo(english) bo'yicha tartiblaydi
# print(frieds)
# frieds.sort(reverse=True)
# print(frieds) 
# sorted() function
sorted_list = sorted(frieds, reverse=True)
print(frieds)
print(sorted_list)

nums = [12, -5, 0, 8.75, 99, 10]
# nums.sort() # o'sish tartibi
# print(nums)
# print(sorted(nums, reverse=True)) # kamayish tartibi


# list.reverse()
nums.reverse()
print(nums)

# list() funksion
users = ['john', 'alisa', 'aziz', 'alex']
cars = list(('bmw', 'audi', 'ford', 'mers'))
print(cars)
# range() - ma'lum bir oraliqdagi sonlarni shakllashtirish uchun ishlatiladi
# range(start, stop, step)
# range(1, 10) # [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(list(range(1, 10)))
even_nums = list(range(2, 20, 2))
print(even_nums)
odd_nums = list(range(1, 20, 2))
print(odd_nums)

# SONLI RO'YXAT USTIDA SODDA AMALLAR
narxlar = [12000, 22500, 23456, 9800, 5600, 9934, 32874]
# min() / max() / sum()
eng_arzoni = min(narxlar)
eng_qimmati = max(narxlar)
yigindi = sum(narxlar)
print(eng_arzoni, eng_qimmati, yigindi)

# Ro'yxatni kesib olish
students = ['Akmal', 'jasur', 'asal', 'kumush', 'maftuna', 'elbek']
# new_list = list[start : end]
# 1-case
students1 = students[2 : 5] 
students2 = students[0 : 2]
print(students1, students2) 
# 2-case
students3 = students[1 : ] # start_index dan boshlab oxirigacha kesib oladi
print(students3)
# 3 - case
students4 = students[ : 4] # ro'yxat boshidan end_index gacha kesadi
print(students4)

# 0 dan boshlab indexlanadi
# manfiy index -1 dan boshlanadi (-1. -2, -3)
print(students[-1])
print(students[-2])
print(students[-5])
print(students[-4 : -2])

# RO'YXATDAN NUSXA(COPY) OLISH
# 1. Shallow(sayoz) copy
sonlar = [1, 5, -5, 12]
sonlar2 = sonlar
sonlar2.append(77)
sonlar.insert(2, -8)
print(sonlar2)
print(sonlar)
# 2. Deep(chuqur) copy
sonlar3 = sonlar[:]
sonlar3.append(8)
print(sonlar3)
print(sonlar)

# deep copy using copy library
import copy
orginal_list = [1, 2, [3, 4], 5]
deep_copy = copy.deepcopy(orginal_list)

deep_copy[2].append(99)
print(deep_copy)
print(orginal_list)

# Tuple - o'zgarmas ro'yxat
toys = ('bus','car','bear','dino','snake','lizard')
print(toys[0])
print(toys[-1])
print(toys[2:5])
# toys[1] = 'dragon'
# print(toys) # error

toys = list(toys)
toys[1] = 'dragon'
toys.remove('dino')
toys.append('mcqueen')
toys = tuple(toys)
print(toys)

# 
sonlar = list(range(120, 1200, 2))
# boshidan 20 ta element
print(sonlar[ : 20])
# oxirdagi 20 ta element
print(sonlar[-20 : ])
# o'rtasidan 20 ta element
length = len(sonlar)
start_index = length // 2 - 10
end_index = length // 2 + 10
print(sonlar[start_index : end_index])
